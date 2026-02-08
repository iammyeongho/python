"""
User Repository
===============
사용자 DB CRUD 작업

Repository는 DB 접근만 담당
비즈니스 로직은 Service에서 처리

PHP의 Repository와 동일한 개념
Laravel의 Eloquent 쿼리를 분리한 것과 유사
"""

from typing import Optional, List
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class UserRepository:
    """
    사용자 Repository

    CRUD 메서드 제공
    모든 메서드는 async (비동기)
    """

    def __init__(self, db: AsyncSession):
        """
        Args:
            db: 데이터베이스 세션 (의존성 주입)
        """
        self.db = db

    # ========================================
    # CREATE
    # ========================================

    async def create(self, user_data: dict) -> User:
        """
        사용자 생성

        Args:
            user_data: 사용자 데이터 딕셔너리
                {
                    "email": "...",
                    "name": "...",
                    "hashed_password": "..."
                }

        Returns:
            생성된 User 객체

        사용 예:
            user = await repo.create({
                "email": "test@example.com",
                "name": "Test User",
                "hashed_password": "hashed..."
            })
        """
        user = User(**user_data)
        self.db.add(user)
        await self.db.flush()  # DB에 쓰기 (ID 생성)
        await self.db.refresh(user)  # 최신 상태로 갱신
        return user

    # ========================================
    # READ
    # ========================================

    async def get_by_id(self, user_id: int) -> Optional[User]:
        """
        ID로 사용자 조회

        Args:
            user_id: 사용자 ID

        Returns:
            User 객체 또는 None
        """
        result = await self.db.execute(
            select(User).where(User.id == user_id)
        )
        return result.scalar_one_or_none()

    async def get_by_email(self, email: str) -> Optional[User]:
        """
        이메일로 사용자 조회

        로그인 시 사용
        """
        result = await self.db.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()

    async def get_all(
        self,
        skip: int = 0,
        limit: int = 100
    ) -> List[User]:
        """
        모든 사용자 조회 (페이지네이션)

        Args:
            skip: 건너뛸 개수 (offset)
            limit: 조회 개수

        Returns:
            User 리스트
        """
        result = await self.db.execute(
            select(User)
            .offset(skip)
            .limit(limit)
            .order_by(User.id)
        )
        return list(result.scalars().all())

    async def get_active_users(self) -> List[User]:
        """
        활성 사용자만 조회
        """
        result = await self.db.execute(
            select(User).where(User.is_active == True)
        )
        return list(result.scalars().all())

    async def exists_by_email(self, email: str) -> bool:
        """
        이메일 존재 여부 확인

        회원가입 시 중복 체크에 사용
        """
        result = await self.db.execute(
            select(User.id).where(User.email == email)
        )
        return result.scalar_one_or_none() is not None

    # ========================================
    # UPDATE
    # ========================================

    async def update(
        self,
        user_id: int,
        update_data: dict
    ) -> Optional[User]:
        """
        사용자 정보 수정

        Args:
            user_id: 수정할 사용자 ID
            update_data: 수정할 데이터 딕셔너리

        Returns:
            수정된 User 객체 또는 None
        """
        # 먼저 사용자 존재 확인
        user = await self.get_by_id(user_id)
        if not user:
            return None

        # 업데이트 실행
        await self.db.execute(
            update(User)
            .where(User.id == user_id)
            .values(**update_data)
        )
        await self.db.flush()

        # 갱신된 데이터 반환
        await self.db.refresh(user)
        return user

    # ========================================
    # DELETE
    # ========================================

    async def delete(self, user_id: int) -> bool:
        """
        사용자 삭제

        Args:
            user_id: 삭제할 사용자 ID

        Returns:
            삭제 성공 여부
        """
        result = await self.db.execute(
            delete(User).where(User.id == user_id)
        )
        return result.rowcount > 0

    async def soft_delete(self, user_id: int) -> Optional[User]:
        """
        소프트 삭제 (비활성화)

        실제 삭제 대신 is_active = False로 변경
        """
        return await self.update(user_id, {"is_active": False})

    # ========================================
    # 검색/필터
    # ========================================

    async def search_by_name(self, name: str) -> List[User]:
        """
        이름으로 검색 (부분 일치)
        """
        result = await self.db.execute(
            select(User).where(User.name.ilike(f"%{name}%"))
        )
        return list(result.scalars().all())

    async def count(self) -> int:
        """
        전체 사용자 수
        """
        from sqlalchemy import func
        result = await self.db.execute(
            select(func.count(User.id))
        )
        return result.scalar_one()
