"""
보안 유틸리티
=============
비밀번호 해싱 및 JWT 토큰 처리

흐름:
1. 회원가입 → get_password_hash()로 비밀번호 해싱
2. 로그인 → verify_password()로 비밀번호 검증
3. 인증 성공 → create_access_token()으로 JWT 발급
4. API 요청 → decode_token()으로 토큰 검증
"""

from datetime import datetime, timedelta
from typing import Any, Optional

from jose import jwt, JWTError
from passlib.context import CryptContext

from app.config import settings


# ============================================================================
# 비밀번호 해싱 설정
# ============================================================================

# bcrypt 사용 (가장 안전한 해싱 알고리즘)
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"  # 이전 알고리즘 자동 업그레이드
)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    비밀번호 검증

    Args:
        plain_password: 사용자가 입력한 평문 비밀번호
        hashed_password: DB에 저장된 해시 비밀번호

    Returns:
        일치 여부

    사용 예:
        if verify_password(input_password, user.hashed_password):
            # 로그인 성공
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    비밀번호 해싱

    Args:
        password: 평문 비밀번호

    Returns:
        해시된 비밀번호

    사용 예:
        hashed = get_password_hash("mypassword123")
        # $2b$12$... 형태의 bcrypt 해시
    """
    return pwd_context.hash(password)


# ============================================================================
# JWT 토큰 처리
# ============================================================================

def create_access_token(
    subject: str | int,
    expires_delta: Optional[timedelta] = None
) -> str:
    """
    Access Token 생성

    Args:
        subject: 토큰에 담을 주체 (보통 user_id)
        expires_delta: 만료 시간 (기본: 설정값)

    Returns:
        JWT 토큰 문자열

    토큰 구조:
        {
            "sub": "1",           # subject (user_id)
            "exp": 1234567890,    # 만료 시간
            "type": "access"
        }
    """
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.access_token_expire_minutes
        )

    to_encode = {
        "sub": str(subject),
        "exp": expire,
        "type": "access"
    }

    encoded_jwt = jwt.encode(
        to_encode,
        settings.secret_key,
        algorithm=settings.algorithm
    )

    return encoded_jwt


def create_refresh_token(
    subject: str | int,
    expires_delta: Optional[timedelta] = None
) -> str:
    """
    Refresh Token 생성

    Access Token보다 긴 유효기간
    Access Token 갱신에 사용
    """
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            days=settings.refresh_token_expire_days
        )

    to_encode = {
        "sub": str(subject),
        "exp": expire,
        "type": "refresh"
    }

    encoded_jwt = jwt.encode(
        to_encode,
        settings.secret_key,
        algorithm=settings.algorithm
    )

    return encoded_jwt


def decode_token(token: str) -> Optional[dict[str, Any]]:
    """
    토큰 디코딩 및 검증

    Args:
        token: JWT 토큰 문자열

    Returns:
        페이로드 딕셔너리 (실패 시 None)

    검증 항목:
    1. 서명 유효성
    2. 만료 시간
    3. 알고리즘

    사용 예:
        payload = decode_token(token)
        if payload:
            user_id = payload["sub"]
    """
    try:
        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[settings.algorithm]
        )
        return payload
    except JWTError:
        return None
