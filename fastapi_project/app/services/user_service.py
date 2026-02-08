"""
User Service
============
사용자 관련 비즈니스 로직

Service의 역할:
1. 비즈니스 규칙 적용
2. 데이터 검증/변환
3. 여러 Repository 조합
4. 트랜잭션 관리

PHP의 Service 클래스와 동일한 개념
Laravel의 Action 클래스와 유사
"""

from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.repositories.user_repository import UserRepository
from app.utils.security import get_password_hash


class UserService:
    """
    사용자 비즈니스 로직 처리

    Repository를 주입받아 사용
    """

    def __init__(self, db: AsyncSession):
        """
        Args:
            db: 데이터베이스 세션
        """
        self.db = db
        self.repository = UserRepository(db)

    # ========================================
    # 사용자 생성
    # ========================================

    async def create_user(self, user_create: UserCreate) -> User:
        """
        새 사용자 생성

        비즈니스 규칙:
        1. 이메일 중복 체크
        2. 비밀번호 해싱
        3. 사용자 생성

        Args:
            user_create: 사용자 생성 요청 데이터

        Returns:
            생성된 User 객체

        Raises:
            HTTPException: 이메일 중복 시
        """
        # 1. 이메일 중복 체크
        if await self.repository.exists_by_email(user_create.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="이미 등록된 이메일입니다."
            )

        # 2. 비밀번호 해싱
        hashed_password = get_password_hash(user_create.password)

        # 3. 사용자 데이터 준비
        user_data = {
            "email": user_create.email,
            "name": user_create.name,
            "hashed_password": hashed_password,
        }

        # 4. 사용자 생성
        user = await self.repository.create(user_data)
        return user

    # ========================================
    # 사용자 조회
    # ========================================

    async def get_user(self, user_id: int) -> User:
        """
        사용자 조회 (단일)

        Raises:
            HTTPException: 사용자 없을 시 404
        """
        user = await self.repository.get_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="사용자를 찾을 수 없습니다."
            )
        return user

    async def get_user_by_email(self, email: str) -> Optional[User]:
        """
        이메일로 사용자 조회

        인증 시 사용 (예외 던지지 않음)
        """
        return await self.repository.get_by_email(email)

    async def get_users(
        self,
        skip: int = 0,
        limit: int = 100
    ) -> List[User]:
        """
        사용자 목록 조회 (페이지네이션)
        """
        return await self.repository.get_all(skip=skip, limit=limit)

    # ========================================
    # 사용자 수정
    # ========================================

    async def update_user(
        self,
        user_id: int,
        user_update: UserUpdate
    ) -> User:
        """
        사용자 정보 수정

        비즈니스 규칙:
        1. 사용자 존재 확인
        2. 이메일 변경 시 중복 체크
        3. 비밀번호 변경 시 해싱
        4. 수정 실행
        """
        # 1. 사용자 존재 확인
        user = await self.repository.get_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="사용자를 찾을 수 없습니다."
            )

        # 2. 수정할 데이터 준비 (None 제외)
        update_data = user_update.model_dump(exclude_unset=True)

        # 3. 이메일 중복 체크
        if "email" in update_data:
            existing = await self.repository.get_by_email(update_data["email"])
            if existing and existing.id != user_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="이미 사용 중인 이메일입니다."
                )

        # 4. 비밀번호 해싱
        if "password" in update_data:
            update_data["hashed_password"] = get_password_hash(
                update_data.pop("password")
            )

        # 5. 수정 실행
        if update_data:
            user = await self.repository.update(user_id, update_data)

        return user

    # ========================================
    # 사용자 삭제
    # ========================================

    async def delete_user(self, user_id: int) -> None:
        """
        사용자 삭제

        Raises:
            HTTPException: 사용자 없을 시 404
        """
        success = await self.repository.delete(user_id)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="사용자를 찾을 수 없습니다."
            )

    async def deactivate_user(self, user_id: int) -> User:
        """
        사용자 비활성화 (소프트 삭제)
        """
        user = await self.repository.soft_delete(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="사용자를 찾을 수 없습니다."
            )
        return user
