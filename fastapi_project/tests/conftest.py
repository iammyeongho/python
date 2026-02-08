"""
pytest 설정 및 Fixtures
========================
테스트에서 공통으로 사용하는 설정과 객체

Fixture란?
- 테스트 전후에 실행되는 셋업/정리 코드
- 테스트 간 공유되는 객체
- PHP의 setUp()/tearDown()과 유사
"""

import pytest
import asyncio
from typing import AsyncGenerator
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.main import app
from app.database import Base, get_db
from app.config import settings


# ============================================================================
# 테스트용 DB 설정
# ============================================================================

# 테스트용 SQLite (인메모리)
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

test_engine = create_async_engine(
    TEST_DATABASE_URL,
    echo=False,
)

TestSessionLocal = async_sessionmaker(
    bind=test_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


# ============================================================================
# Fixtures
# ============================================================================

@pytest.fixture(scope="session")
def event_loop():
    """
    이벤트 루프 fixture

    pytest-asyncio에서 사용
    """
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    """
    테스트용 DB 세션

    각 테스트마다 새 DB 생성/삭제
    """
    # 테이블 생성
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # 세션 생성
    async with TestSessionLocal() as session:
        yield session

    # 테이블 삭제 (테스트 격리)
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="function")
async def client(db_session: AsyncSession) -> AsyncGenerator[AsyncClient, None]:
    """
    테스트용 HTTP 클라이언트

    실제 서버 없이 FastAPI 앱에 요청
    """

    # DB 의존성 오버라이드
    async def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    # 비동기 HTTP 클라이언트
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as ac:
        yield ac

    # 정리
    app.dependency_overrides.clear()


@pytest.fixture
def user_data():
    """
    테스트용 사용자 데이터
    """
    return {
        "email": "test@example.com",
        "name": "Test User",
        "password": "testpassword123"
    }


@pytest.fixture
async def created_user(client: AsyncClient, user_data: dict):
    """
    생성된 사용자 fixture

    테스트에서 이미 생성된 사용자가 필요할 때 사용
    """
    response = await client.post("/api/v1/users", json=user_data)
    return response.json()


@pytest.fixture
async def auth_headers(client: AsyncClient, user_data: dict):
    """
    인증 헤더 fixture

    로그인된 상태가 필요한 테스트에서 사용
    """
    # 사용자 생성
    await client.post("/api/v1/users", json=user_data)

    # 로그인
    response = await client.post(
        "/api/v1/auth/login",
        data={
            "username": user_data["email"],
            "password": user_data["password"]
        }
    )
    token = response.json()["access_token"]

    return {"Authorization": f"Bearer {token}"}
