"""
Token 스키마
============
JWT 토큰 관련 데이터 구조
"""

from typing import Optional
from pydantic import BaseModel


class Token(BaseModel):
    """
    토큰 응답

    로그인 성공 시 반환
    """
    access_token: str
    refresh_token: Optional[str] = None
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    """
    토큰 페이로드

    JWT 토큰 내부에 담기는 데이터
    """
    sub: str  # subject (보통 user_id)
    exp: int  # expiration time
    type: str = "access"  # access or refresh


class LoginRequest(BaseModel):
    """
    로그인 요청
    """
    email: str
    password: str
