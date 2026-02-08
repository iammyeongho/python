"""
Auth Service
============
인증 관련 비즈니스 로직

흐름:
1. 로그인 → 이메일/비밀번호 검증 → JWT 발급
2. 토큰 갱신 → Refresh Token 검증 → 새 Access Token 발급
3. 로그아웃 → (클라이언트에서 토큰 삭제)
"""

from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from app.models.user import User
from app.schemas.token import Token
from app.repositories.user_repository import UserRepository
from app.utils.security import (
    verify_password,
    create_access_token,
    create_refresh_token,
    decode_token,
)


class AuthService:
    """
    인증 서비스
    """

    def __init__(self, db: AsyncSession):
        self.db = db
        self.user_repository = UserRepository(db)

    async def authenticate(
        self,
        email: str,
        password: str
    ) -> Optional[User]:
        """
        사용자 인증 (이메일/비밀번호)

        Args:
            email: 이메일
            password: 평문 비밀번호

        Returns:
            인증된 User 객체 또는 None

        사용 예:
            user = await auth_service.authenticate("test@example.com", "password")
            if user:
                # 인증 성공
        """
        # 1. 이메일로 사용자 조회
        user = await self.user_repository.get_by_email(email)
        if not user:
            return None

        # 2. 비밀번호 검증
        if not verify_password(password, user.hashed_password):
            return None

        # 3. 활성 사용자인지 확인
        if not user.is_active:
            return None

        return user

    async def login(self, email: str, password: str) -> Token:
        """
        로그인 처리

        Args:
            email: 이메일
            password: 비밀번호

        Returns:
            Token 객체 (access_token, refresh_token)

        Raises:
            HTTPException: 인증 실패 시 401
        """
        # 1. 인증
        user = await self.authenticate(email, password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="이메일 또는 비밀번호가 올바르지 않습니다.",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # 2. 토큰 생성
        access_token = create_access_token(subject=user.id)
        refresh_token = create_refresh_token(subject=user.id)

        return Token(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type="bearer"
        )

    async def refresh_access_token(self, refresh_token: str) -> Token:
        """
        Access Token 갱신

        Args:
            refresh_token: Refresh Token

        Returns:
            새 Token 객체

        Raises:
            HTTPException: 토큰 유효하지 않을 시 401
        """
        # 1. Refresh Token 검증
        payload = decode_token(refresh_token)
        if not payload:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="유효하지 않은 토큰입니다."
            )

        # 2. 토큰 타입 확인
        if payload.get("type") != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Refresh Token이 아닙니다."
            )

        # 3. 사용자 존재 확인
        user_id = int(payload.get("sub"))
        user = await self.user_repository.get_by_id(user_id)
        if not user or not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="사용자를 찾을 수 없습니다."
            )

        # 4. 새 토큰 생성
        access_token = create_access_token(subject=user.id)

        return Token(
            access_token=access_token,
            refresh_token=refresh_token,  # 기존 refresh token 유지
            token_type="bearer"
        )

    async def get_current_user(self, token: str) -> User:
        """
        현재 로그인한 사용자 조회

        Args:
            token: Access Token

        Returns:
            User 객체

        Raises:
            HTTPException: 인증 실패 시 401
        """
        # 1. 토큰 검증
        payload = decode_token(token)
        if not payload:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="유효하지 않은 토큰입니다.",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # 2. 토큰 타입 확인
        if payload.get("type") != "access":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Access Token이 아닙니다."
            )

        # 3. 사용자 조회
        user_id = int(payload.get("sub"))
        user = await self.user_repository.get_by_id(user_id)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="사용자를 찾을 수 없습니다."
            )

        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="비활성화된 계정입니다."
            )

        return user
