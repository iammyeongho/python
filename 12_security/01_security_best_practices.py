"""
Python 보안 베스트 프랙티스
=====================================
OWASP Top 10을 기반으로 한 보안 가이드
"""

# =============================================================================
# 1. SQL Injection 방지
# =============================================================================

print("=== SQL Injection 방지 ===")

# ❌ 취약한 코드
def get_user_vulnerable(user_id):
    """SQL Injection에 취약"""
    query = f"SELECT * FROM users WHERE id = {user_id}"
    # user_id = "1 OR 1=1" 입력 시 모든 데이터 노출
    return query

print(f"취약한 쿼리: {get_user_vulnerable('1 OR 1=1')}")


# ✅ 안전한 코드 - 파라미터화된 쿼리
def get_user_safe():
    """파라미터화된 쿼리 사용"""
    import sqlite3
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    user_id = "1 OR 1=1"  # 악의적 입력

    # 안전한 방법
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    # 입력값이 문자열로 처리됨


# ✅ SQLAlchemy ORM 사용 (권장)
"""
from sqlalchemy.orm import Session

def get_user_sqlalchemy(db: Session, user_id: int):
    # ORM이 자동으로 파라미터화
    return db.query(User).filter(User.id == user_id).first()

# Raw SQL이 필요한 경우
from sqlalchemy import text
result = db.execute(text("SELECT * FROM users WHERE id = :id"), {"id": user_id})
"""


# =============================================================================
# 2. XSS (Cross-Site Scripting) 방지
# =============================================================================

print("\n=== XSS 방지 ===")

import html

# ❌ 취약한 코드
def render_vulnerable(user_input):
    """XSS에 취약"""
    return f"<div>Hello, {user_input}</div>"

malicious_input = '<script>alert("XSS")</script>'
print(f"취약한 출력: {render_vulnerable(malicious_input)}")


# ✅ 안전한 코드 - HTML 이스케이프
def render_safe(user_input):
    """HTML 이스케이프"""
    escaped = html.escape(user_input)
    return f"<div>Hello, {escaped}</div>"

print(f"안전한 출력: {render_safe(malicious_input)}")


# ✅ Jinja2 템플릿 (자동 이스케이프)
"""
# 자동 이스케이프 활성화 (기본값)
from jinja2 import Environment, select_autoescape

env = Environment(autoescape=select_autoescape(['html', 'xml']))

# 템플릿에서 자동 이스케이프
template = env.from_string("<div>{{ user_input }}</div>")
result = template.render(user_input=malicious_input)
"""


# =============================================================================
# 3. CSRF (Cross-Site Request Forgery) 방지
# =============================================================================

print("\n=== CSRF 방지 ===")

"""
# FastAPI에서 CSRF 토큰 사용
from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.templating import Jinja2Templates
import secrets

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# CSRF 토큰 저장소 (실제로는 세션/Redis 사용)
csrf_tokens = {}


def generate_csrf_token(session_id: str) -> str:
    token = secrets.token_urlsafe(32)
    csrf_tokens[session_id] = token
    return token


def validate_csrf_token(session_id: str, token: str) -> bool:
    expected = csrf_tokens.get(session_id)
    return secrets.compare_digest(expected or "", token)


@app.get("/form")
async def show_form(request: Request):
    session_id = request.cookies.get("session_id")
    csrf_token = generate_csrf_token(session_id)
    return templates.TemplateResponse("form.html", {
        "request": request,
        "csrf_token": csrf_token
    })


@app.post("/submit")
async def submit_form(request: Request, csrf_token: str = Form(...)):
    session_id = request.cookies.get("session_id")
    if not validate_csrf_token(session_id, csrf_token):
        raise HTTPException(status_code=403, detail="Invalid CSRF token")
    # 처리 로직
"""


# =============================================================================
# 4. 비밀번호 해싱
# =============================================================================

print("\n=== 비밀번호 해싱 ===")

# ❌ 절대 하지 말아야 할 것
def bad_hash(password):
    """MD5, SHA1은 비밀번호에 부적합"""
    import hashlib
    return hashlib.md5(password.encode()).hexdigest()


# ✅ bcrypt 사용 (권장)
def hash_password_bcrypt(password: str) -> str:
    """bcrypt로 비밀번호 해싱"""
    import bcrypt
    salt = bcrypt.gensalt(rounds=12)  # cost factor
    return bcrypt.hashpw(password.encode(), salt).decode()


def verify_password_bcrypt(password: str, hashed: str) -> bool:
    """bcrypt 비밀번호 검증"""
    import bcrypt
    return bcrypt.checkpw(password.encode(), hashed.encode())


# ✅ passlib 사용 (여러 알고리즘 지원)
"""
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
"""

# 예제
# password = "mySecurePassword123"
# hashed = hash_password_bcrypt(password)
# print(f"해시된 비밀번호: {hashed}")
# print(f"검증 결과: {verify_password_bcrypt(password, hashed)}")


# =============================================================================
# 5. 입력 검증
# =============================================================================

print("\n=== 입력 검증 ===")

from pydantic import BaseModel, EmailStr, Field, field_validator
import re


class UserInput(BaseModel):
    """입력 검증 모델"""
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    age: int = Field(..., ge=0, le=150)
    phone: str

    @field_validator('username')
    @classmethod
    def username_alphanumeric(cls, v):
        if not re.match(r'^[a-zA-Z0-9_]+$', v):
            raise ValueError('Username must be alphanumeric')
        return v

    @field_validator('phone')
    @classmethod
    def phone_format(cls, v):
        if not re.match(r'^\d{3}-\d{4}-\d{4}$', v):
            raise ValueError('Phone must be in format: 010-1234-5678')
        return v


# 테스트
try:
    user = UserInput(
        username="alice123",
        email="alice@example.com",
        age=25,
        phone="010-1234-5678"
    )
    print(f"유효한 입력: {user}")
except Exception as e:
    print(f"검증 실패: {e}")


# =============================================================================
# 6. 파일 업로드 보안
# =============================================================================

print("\n=== 파일 업로드 보안 ===")

"""
from fastapi import FastAPI, UploadFile, HTTPException
import magic
import os
import uuid

ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.pdf'}
ALLOWED_MIMETYPES = {'image/jpeg', 'image/png', 'image/gif', 'application/pdf'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB


async def secure_upload(file: UploadFile):
    # 1. 파일 크기 검사
    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(400, "File too large")

    # 2. 확장자 검사
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(400, "File type not allowed")

    # 3. MIME 타입 검사 (실제 파일 내용 확인)
    mime = magic.from_buffer(contents, mime=True)
    if mime not in ALLOWED_MIMETYPES:
        raise HTTPException(400, "Invalid file content")

    # 4. 안전한 파일명 생성
    safe_filename = f"{uuid.uuid4()}{ext}"

    # 5. 웹 루트 외부에 저장
    upload_path = f"/var/uploads/{safe_filename}"
    with open(upload_path, 'wb') as f:
        f.write(contents)

    return {"filename": safe_filename}
"""


# =============================================================================
# 7. 환경 변수와 시크릿 관리
# =============================================================================

print("\n=== 환경 변수 관리 ===")

import os
from typing import Optional

# ❌ 코드에 하드코딩
# DATABASE_URL = "postgresql://user:password@localhost/db"

# ✅ 환경 변수 사용
DATABASE_URL = os.environ.get("DATABASE_URL")
SECRET_KEY = os.environ.get("SECRET_KEY")

# ✅ pydantic-settings 사용 (권장)
"""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    debug: bool = False
    allowed_hosts: list[str] = ["localhost"]

    class Config:
        env_file = ".env"

settings = Settings()
"""

# .env 파일 예제
"""
# .env (절대 git에 커밋하지 마세요)
DATABASE_URL=postgresql://user:password@localhost/db
SECRET_KEY=your-super-secret-key
DEBUG=false
"""

# .gitignore에 추가
"""
.env
.env.local
*.env
"""


# =============================================================================
# 8. JWT 보안
# =============================================================================

print("\n=== JWT 보안 ===")

"""
from datetime import datetime, timedelta
from jose import JWTError, jwt

SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None


# JWT 보안 체크리스트:
# ✅ 강력한 시크릿 키 사용
# ✅ 짧은 만료 시간
# ✅ HTTPS 필수
# ✅ HttpOnly 쿠키에 저장
# ✅ 민감한 정보 payload에 넣지 않기
"""


# =============================================================================
# 9. Rate Limiting
# =============================================================================

print("\n=== Rate Limiting ===")

"""
from fastapi import FastAPI, Request, HTTPException
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


@app.get("/api/resource")
@limiter.limit("10/minute")  # 분당 10회
async def get_resource(request: Request):
    return {"data": "resource"}


@app.post("/api/login")
@limiter.limit("5/minute")  # 로그인은 더 엄격하게
async def login(request: Request):
    return {"token": "..."}
"""


# =============================================================================
# 10. 보안 헤더
# =============================================================================

print("\n=== 보안 헤더 ===")

"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://myapp.com"],  # 특정 도메인만 허용
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


# 보안 헤더 미들웨어
class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = "max-age=31536000"
        response.headers["Content-Security-Policy"] = "default-src 'self'"
        return response

app.add_middleware(SecurityHeadersMiddleware)
"""


# =============================================================================
# 11. 보안 검사 도구
# =============================================================================

print("\n=== 보안 검사 도구 ===")

"""
# Bandit - Python 코드 보안 검사
pip install bandit
bandit -r your_project/

# Safety - 의존성 취약점 검사
pip install safety
safety check

# pip-audit - 의존성 감사
pip install pip-audit
pip-audit

# pre-commit에 통합
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.5
    hooks:
      - id: bandit
        args: ["-c", "pyproject.toml"]
"""


# =============================================================================
# 정리: 보안 체크리스트
# =============================================================================

"""
Python 보안 체크리스트:

1. 인젝션 방지
   □ 파라미터화된 쿼리 사용
   □ ORM 사용 권장
   □ 입력값 검증

2. 인증/세션
   □ bcrypt로 비밀번호 해싱
   □ 안전한 세션 관리
   □ JWT 적절한 만료 시간

3. 민감한 데이터
   □ 환경 변수 사용
   □ 시크릿 하드코딩 금지
   □ HTTPS 필수

4. 입력 검증
   □ Pydantic으로 검증
   □ 화이트리스트 방식
   □ 파일 업로드 검증

5. 출력 이스케이프
   □ HTML 이스케이프
   □ 템플릿 자동 이스케이프

6. 접근 제어
   □ 인증/인가 분리
   □ Rate limiting
   □ CORS 설정

7. 보안 헤더
   □ CSP, HSTS, X-Frame-Options
   □ HttpOnly, Secure 쿠키

8. 의존성
   □ 정기적 업데이트
   □ 취약점 스캔

PHP 비교:
- PDO prepared statements와 동일한 원리
- Laravel의 Eloquent ORM과 유사
- PHP의 password_hash와 bcrypt 동일
"""
