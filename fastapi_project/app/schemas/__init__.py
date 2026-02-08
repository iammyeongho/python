"""
Pydantic 스키마
===============
API 요청/응답 데이터 검증

Model(SQLAlchemy)과 Schema(Pydantic)의 차이:
- Model: DB 테이블 구조
- Schema: API 요청/응답 데이터 구조 및 검증
"""

from app.schemas.user import (
    UserCreate,
    UserUpdate,
    UserResponse,
    UserInDB,
)
from app.schemas.token import Token, TokenPayload

__all__ = [
    "UserCreate",
    "UserUpdate",
    "UserResponse",
    "UserInDB",
    "Token",
    "TokenPayload",
]
