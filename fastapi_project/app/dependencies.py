"""
의존성 주입 (Dependency Injection)
==================================
FastAPI의 Depends() 시스템을 활용한 의존성 관리

의존성 주입이란?
- 클래스/함수가 필요한 것을 직접 생성하지 않고 외부에서 주입받음
- 테스트, 유지보수 용이

PHP/Laravel의 Service Container와 유사한 개념
"""

from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.user import User
from app.services.auth_service import AuthService
from app.services.user_service import UserService


# ============================================================================
# OAuth2 스키마 (토큰 추출)
# ============================================================================

# Authorization 헤더에서 Bearer 토큰 추출
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login"  # 토큰 발급 엔드포인트
)


# ============================================================================
# 현재 사용자 가져오기
# ============================================================================

async def get_current_user(
    db: AsyncSession = Depends(get_db),
    token: str = Depends(oauth2_scheme)
) -> User:
    """
    현재 로그인한 사용자 반환

    의존성 체인:
    1. get_db() → DB 세션
    2. oauth2_scheme → 토큰 추출
    3. AuthService → 토큰 검증 및 사용자 조회

    사용 예:
        @router.get("/me")
        async def get_me(
            current_user: User = Depends(get_current_user)
        ):
            return current_user
    """
    auth_service = AuthService(db)
    return await auth_service.get_current_user(token)


async def get_current_active_user(
    current_user: User = Depends(get_current_user)
) -> User:
    """
    활성 사용자만 반환

    get_current_user를 재사용 (의존성 체인)
    """
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="비활성화된 계정입니다."
        )
    return current_user


async def get_current_superuser(
    current_user: User = Depends(get_current_user)
) -> User:
    """
    관리자 사용자만 반환

    사용 예:
        @router.delete("/users/{id}")
        async def delete_user(
            id: int,
            admin: User = Depends(get_current_superuser)
        ):
            # 관리자만 접근 가능
    """
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="관리자 권한이 필요합니다."
        )
    return current_user


# ============================================================================
# 서비스 의존성
# ============================================================================

async def get_user_service(
    db: AsyncSession = Depends(get_db)
) -> UserService:
    """
    UserService 인스턴스 반환

    사용 예:
        @router.get("/users")
        async def get_users(
            user_service: UserService = Depends(get_user_service)
        ):
            return await user_service.get_users()
    """
    return UserService(db)


async def get_auth_service(
    db: AsyncSession = Depends(get_db)
) -> AuthService:
    """
    AuthService 인스턴스 반환
    """
    return AuthService(db)


# ============================================================================
# 타입 힌트용 Annotated (Python 3.9+)
# ============================================================================

# 더 깔끔한 문법을 위한 타입 별칭
DBSession = Annotated[AsyncSession, Depends(get_db)]
CurrentUser = Annotated[User, Depends(get_current_user)]
CurrentActiveUser = Annotated[User, Depends(get_current_active_user)]
CurrentSuperuser = Annotated[User, Depends(get_current_superuser)]


"""
사용 예시:

# 기존 방식
@router.get("/me")
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user

# Annotated 사용 (권장)
@router.get("/me")
async def get_me(current_user: CurrentUser):
    return current_user
"""
