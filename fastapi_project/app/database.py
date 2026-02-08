"""
데이터베이스 설정
=================
SQLAlchemy 비동기 엔진 및 세션 관리

흐름:
1. create_async_engine() → DB 연결 엔진 생성
2. async_sessionmaker() → 세션 팩토리 생성
3. get_db() → 요청마다 세션 주입 (의존성)
"""

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase
from typing import AsyncGenerator

from app.config import settings


# ============================================================================
# 1. 비동기 엔진 생성
# ============================================================================

engine = create_async_engine(
    settings.database_url,
    echo=settings.debug,  # SQL 쿼리 로깅 (개발용)
    pool_pre_ping=True,   # 연결 상태 확인
    pool_size=5,          # 연결 풀 크기
    max_overflow=10,      # 최대 추가 연결
)


# ============================================================================
# 2. 세션 팩토리 생성
# ============================================================================

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,  # 커밋 후에도 객체 접근 가능
    autocommit=False,
    autoflush=False,
)


# ============================================================================
# 3. Base 클래스 (모든 모델의 부모)
# ============================================================================

class Base(DeclarativeBase):
    """
    모든 SQLAlchemy 모델의 기본 클래스

    사용법:
        class User(Base):
            __tablename__ = "users"
            ...
    """
    pass


# ============================================================================
# 4. DB 세션 의존성 (가장 중요!)
# ============================================================================

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    DB 세션을 제공하는 의존성 함수

    FastAPI의 Depends()와 함께 사용:

        @router.get("/users")
        async def get_users(db: AsyncSession = Depends(get_db)):
            # db 세션 사용
            ...

    흐름:
    1. 요청 시작 → 세션 생성
    2. 라우터 함수 실행 (세션 사용)
    3. 요청 종료 → 세션 자동 닫힘 (finally)
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()  # 성공 시 커밋
        except Exception:
            await session.rollback()  # 실패 시 롤백
            raise
        finally:
            await session.close()


# ============================================================================
# 5. DB 초기화 함수
# ============================================================================

async def init_db() -> None:
    """
    데이터베이스 테이블 생성

    주의: 프로덕션에서는 Alembic 마이그레이션 사용 권장
    """
    async with engine.begin() as conn:
        # 모든 테이블 생성
        await conn.run_sync(Base.metadata.create_all)


async def close_db() -> None:
    """
    데이터베이스 연결 종료
    """
    await engine.dispose()
