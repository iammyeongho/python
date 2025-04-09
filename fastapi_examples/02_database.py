# FastAPI 데이터베이스 연동 예제
# 작성일: 2024-04-09
# 목적: FastAPI와 SQLAlchemy를 사용한 데이터베이스 연동 예제 코드

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

# 데이터베이스 설정
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 데이터베이스 모델
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    
    # 관계 설정
    items = relationship("Item", back_populates="owner")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    # 관계 설정
    owner = relationship("User", back_populates="items")

# Pydantic 모델
class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool
    items: List[ItemResponse] = []

    class Config:
        orm_mode = True

# 데이터베이스 의존성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# FastAPI 애플리케이션 생성
app = FastAPI(
    title="FastAPI 데이터베이스 예제",
    description="FastAPI와 SQLAlchemy를 사용한 데이터베이스 연동 예제",
    version="1.0.0"
)

# 데이터베이스 테이블 생성
@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)

# 1. 사용자 생성
@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    새 사용자를 생성합니다.
    
    - user: 생성할 사용자 정보
    - db: 데이터베이스 세션
    """
    # 실제로는 비밀번호 해싱이 필요합니다
    db_user = User(email=user.email, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# 2. 사용자 조회
@app.get("/users/", response_model=List[UserResponse])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    사용자 목록을 조회합니다.
    
    - skip: 건너뛸 항목 수
    - limit: 반환할 항목 수
    - db: 데이터베이스 세션
    """
    users = db.query(User).offset(skip).limit(limit).all()
    return users

# 3. 특정 사용자 조회
@app.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    """
    특정 사용자를 조회합니다.
    
    - user_id: 조회할 사용자 ID
    - db: 데이터베이스 세션
    """
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다")
    return db_user

# 4. 아이템 생성
@app.post("/users/{user_id}/items/", response_model=ItemResponse)
def create_item_for_user(
    user_id: int, item: ItemCreate, db: Session = Depends(get_db)
):
    """
    특정 사용자의 아이템을 생성합니다.
    
    - user_id: 아이템을 생성할 사용자 ID
    - item: 생성할 아이템 정보
    - db: 데이터베이스 세션
    """
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다")
    
    db_item = Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# 5. 아이템 목록 조회
@app.get("/items/", response_model=List[ItemResponse])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    아이템 목록을 조회합니다.
    
    - skip: 건너뛸 항목 수
    - limit: 반환할 항목 수
    - db: 데이터베이스 세션
    """
    items = db.query(Item).offset(skip).limit(limit).all()
    return items

# 6. 특정 아이템 조회
@app.get("/items/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    """
    특정 아이템을 조회합니다.
    
    - item_id: 조회할 아이템 ID
    - db: 데이터베이스 세션
    """
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="아이템을 찾을 수 없습니다")
    return db_item

# 7. 아이템 업데이트
@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(
    item_id: int, item: ItemCreate, db: Session = Depends(get_db)
):
    """
    특정 아이템을 업데이트합니다.
    
    - item_id: 업데이트할 아이템 ID
    - item: 업데이트할 아이템 정보
    - db: 데이터베이스 세션
    """
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="아이템을 찾을 수 없습니다")
    
    for key, value in item.dict().items():
        setattr(db_item, key, value)
    
    db.commit()
    db.refresh(db_item)
    return db_item

# 8. 아이템 삭제
@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """
    특정 아이템을 삭제합니다.
    
    - item_id: 삭제할 아이템 ID
    - db: 데이터베이스 세션
    """
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="아이템을 찾을 수 없습니다")
    
    db.delete(db_item)
    db.commit()
    return None

# 9. 사용자 삭제
@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    특정 사용자를 삭제합니다.
    
    - user_id: 삭제할 사용자 ID
    - db: 데이터베이스 세션
    """
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="사용자를 찾을 수 없습니다")
    
    db.delete(db_user)
    db.commit()
    return None

# 서버 실행
if __name__ == "__main__":
    uvicorn.run("02_database:app", host="0.0.0.0", port=8000, reload=True) 