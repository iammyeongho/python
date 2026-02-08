"""
사용자 API 테스트
=================
pytest + httpx를 사용한 API 테스트

실행:
    pytest tests/ -v
    pytest tests/test_users.py -v
"""

import pytest
from httpx import AsyncClient


# ============================================================================
# 회원가입 테스트
# ============================================================================

class TestCreateUser:
    """사용자 생성 테스트"""

    @pytest.mark.asyncio
    async def test_create_user_success(self, client: AsyncClient, user_data: dict):
        """
        회원가입 성공
        """
        response = await client.post("/api/v1/users", json=user_data)

        assert response.status_code == 201
        data = response.json()
        assert data["email"] == user_data["email"]
        assert data["name"] == user_data["name"]
        assert "id" in data
        assert "hashed_password" not in data  # 비밀번호 노출 안됨

    @pytest.mark.asyncio
    async def test_create_user_duplicate_email(
        self, client: AsyncClient, user_data: dict
    ):
        """
        이메일 중복 시 에러
        """
        # 첫 번째 생성
        await client.post("/api/v1/users", json=user_data)

        # 두 번째 생성 (중복)
        response = await client.post("/api/v1/users", json=user_data)

        assert response.status_code == 400
        assert "이미 등록된 이메일" in response.json()["detail"]

    @pytest.mark.asyncio
    async def test_create_user_invalid_email(self, client: AsyncClient):
        """
        잘못된 이메일 형식
        """
        response = await client.post("/api/v1/users", json={
            "email": "invalid-email",
            "name": "Test",
            "password": "password123"
        })

        assert response.status_code == 422  # Validation Error

    @pytest.mark.asyncio
    async def test_create_user_short_password(self, client: AsyncClient):
        """
        짧은 비밀번호
        """
        response = await client.post("/api/v1/users", json={
            "email": "test@example.com",
            "name": "Test",
            "password": "short"  # 8자 미만
        })

        assert response.status_code == 422


# ============================================================================
# 로그인 테스트
# ============================================================================

class TestLogin:
    """로그인 테스트"""

    @pytest.mark.asyncio
    async def test_login_success(
        self, client: AsyncClient, created_user: dict, user_data: dict
    ):
        """
        로그인 성공
        """
        response = await client.post(
            "/api/v1/auth/login",
            data={
                "username": user_data["email"],
                "password": user_data["password"]
            }
        )

        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert "refresh_token" in data
        assert data["token_type"] == "bearer"

    @pytest.mark.asyncio
    async def test_login_wrong_password(
        self, client: AsyncClient, created_user: dict, user_data: dict
    ):
        """
        잘못된 비밀번호
        """
        response = await client.post(
            "/api/v1/auth/login",
            data={
                "username": user_data["email"],
                "password": "wrongpassword"
            }
        )

        assert response.status_code == 401

    @pytest.mark.asyncio
    async def test_login_nonexistent_user(self, client: AsyncClient):
        """
        존재하지 않는 사용자
        """
        response = await client.post(
            "/api/v1/auth/login",
            data={
                "username": "nonexistent@example.com",
                "password": "password123"
            }
        )

        assert response.status_code == 401


# ============================================================================
# 사용자 조회 테스트
# ============================================================================

class TestGetUser:
    """사용자 조회 테스트"""

    @pytest.mark.asyncio
    async def test_get_current_user(
        self, client: AsyncClient, auth_headers: dict
    ):
        """
        현재 사용자 정보 조회
        """
        response = await client.get(
            "/api/v1/auth/me",
            headers=auth_headers
        )

        assert response.status_code == 200
        data = response.json()
        assert "email" in data
        assert "name" in data

    @pytest.mark.asyncio
    async def test_get_user_by_id(
        self, client: AsyncClient, created_user: dict, auth_headers: dict
    ):
        """
        ID로 사용자 조회
        """
        user_id = created_user["id"]
        response = await client.get(
            f"/api/v1/users/{user_id}",
            headers=auth_headers
        )

        assert response.status_code == 200
        assert response.json()["id"] == user_id

    @pytest.mark.asyncio
    async def test_get_user_not_found(
        self, client: AsyncClient, auth_headers: dict
    ):
        """
        존재하지 않는 사용자
        """
        response = await client.get(
            "/api/v1/users/99999",
            headers=auth_headers
        )

        assert response.status_code == 404

    @pytest.mark.asyncio
    async def test_get_user_unauthorized(self, client: AsyncClient):
        """
        인증 없이 접근
        """
        response = await client.get("/api/v1/users/1")

        assert response.status_code == 401


# ============================================================================
# 사용자 수정 테스트
# ============================================================================

class TestUpdateUser:
    """사용자 수정 테스트"""

    @pytest.mark.asyncio
    async def test_update_user_name(
        self, client: AsyncClient, created_user: dict, auth_headers: dict
    ):
        """
        이름 수정
        """
        user_id = created_user["id"]
        response = await client.patch(
            f"/api/v1/users/{user_id}",
            json={"name": "Updated Name"},
            headers=auth_headers
        )

        assert response.status_code == 200
        assert response.json()["name"] == "Updated Name"

    @pytest.mark.asyncio
    async def test_update_user_email(
        self, client: AsyncClient, created_user: dict, auth_headers: dict
    ):
        """
        이메일 수정
        """
        user_id = created_user["id"]
        response = await client.patch(
            f"/api/v1/users/{user_id}",
            json={"email": "updated@example.com"},
            headers=auth_headers
        )

        assert response.status_code == 200
        assert response.json()["email"] == "updated@example.com"


# ============================================================================
# 헬스 체크 테스트
# ============================================================================

class TestHealthCheck:
    """헬스 체크 테스트"""

    @pytest.mark.asyncio
    async def test_health_check(self, client: AsyncClient):
        """
        헬스 체크 엔드포인트
        """
        response = await client.get("/health")

        assert response.status_code == 200
        assert response.json()["status"] == "healthy"

    @pytest.mark.asyncio
    async def test_root(self, client: AsyncClient):
        """
        루트 엔드포인트
        """
        response = await client.get("/")

        assert response.status_code == 200
        assert "message" in response.json()
