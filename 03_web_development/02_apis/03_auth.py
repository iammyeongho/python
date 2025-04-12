# FastAPI 인증 및 권한 부여 예제
# 작성일: 2024-04-09
# 목적: FastAPI의 인증 및 권한 부여 기능을 설명하는 예제 코드

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, timedelta
import uvicorn

# 보안 설정
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"  # 실제로는 환경 변수에서 가져와야 합니다
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 비밀번호 해싱 및 검증
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# 데이터 모델
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

# 가상의 사용자 데이터베이스
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": pwd_context.hash("secret"),
        "disabled": False,
    }
}

# 보안 유틸리티 함수
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
    return None

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# 의존성 함수
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="인증 정보가 올바르지 않습니다",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="비활성화된 사용자입니다")
    return current_user

# FastAPI 애플리케이션 생성
app = FastAPI(
    title="FastAPI 인증 예제",
    description="FastAPI의 인증 및 권한 부여 기능을 보여주는 예제",
    version="1.0.0"
)

# 1. 토큰 발급
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    사용자 인증 후 액세스 토큰을 발급합니다.
    
    - form_data: 사용자 이름과 비밀번호가 포함된 폼 데이터
    """
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="사용자 이름 또는 비밀번호가 올바르지 않습니다",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# 2. 현재 사용자 정보 조회
@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    """
    현재 로그인한 사용자의 정보를 조회합니다.
    
    - current_user: 현재 로그인한 사용자
    """
    return current_user

# 3. 사용자 등록 (관리자 전용)
@app.post("/users/", response_model=User)
async def create_user(
    username: str,
    password: str,
    email: Optional[str] = None,
    full_name: Optional[str] = None,
    current_user: User = Depends(get_current_active_user)
):
    """
    새 사용자를 등록합니다. (관리자 전용)
    
    - username: 사용자 이름
    - password: 비밀번호
    - email: 이메일 (선택적)
    - full_name: 전체 이름 (선택적)
    - current_user: 현재 로그인한 사용자 (권한 확인용)
    """
    # 실제로는 관리자 권한 확인 로직이 필요합니다
    if username in fake_users_db:
        raise HTTPException(
            status_code=400,
            detail="이미 존재하는 사용자 이름입니다"
        )
    
    hashed_password = get_password_hash(password)
    user_dict = {
        "username": username,
        "full_name": full_name,
        "email": email,
        "hashed_password": hashed_password,
        "disabled": False,
    }
    fake_users_db[username] = user_dict
    return User(**user_dict)

# 4. 사용자 비활성화 (관리자 전용)
@app.put("/users/{username}/disable")
async def disable_user(
    username: str,
    current_user: User = Depends(get_current_active_user)
):
    """
    사용자를 비활성화합니다. (관리자 전용)
    
    - username: 비활성화할 사용자 이름
    - current_user: 현재 로그인한 사용자 (권한 확인용)
    """
    # 실제로는 관리자 권한 확인 로직이 필요합니다
    if username not in fake_users_db:
        raise HTTPException(
            status_code=404,
            detail="사용자를 찾을 수 없습니다"
        )
    
    fake_users_db[username]["disabled"] = True
    return {"message": f"사용자 {username}이(가) 비활성화되었습니다"}

# 5. 사용자 활성화 (관리자 전용)
@app.put("/users/{username}/enable")
async def enable_user(
    username: str,
    current_user: User = Depends(get_current_active_user)
):
    """
    사용자를 활성화합니다. (관리자 전용)
    
    - username: 활성화할 사용자 이름
    - current_user: 현재 로그인한 사용자 (권한 확인용)
    """
    # 실제로는 관리자 권한 확인 로직이 필요합니다
    if username not in fake_users_db:
        raise HTTPException(
            status_code=404,
            detail="사용자를 찾을 수 없습니다"
        )
    
    fake_users_db[username]["disabled"] = False
    return {"message": f"사용자 {username}이(가) 활성화되었습니다"}

# 6. 사용자 목록 조회 (관리자 전용)
@app.get("/users/", response_model=List[User])
async def read_users(
    skip: int = 0,
    limit: int = 10,
    current_user: User = Depends(get_current_active_user)
):
    """
    사용자 목록을 조회합니다. (관리자 전용)
    
    - skip: 건너뛸 항목 수
    - limit: 반환할 항목 수
    - current_user: 현재 로그인한 사용자 (권한 확인용)
    """
    # 실제로는 관리자 권한 확인 로직이 필요합니다
    users = list(fake_users_db.values())
    return users[skip : skip + limit]

# 서버 실행
if __name__ == "__main__":
    uvicorn.run("03_auth:app", host="0.0.0.0", port=8000, reload=True) 