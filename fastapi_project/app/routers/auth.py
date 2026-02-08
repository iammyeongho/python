"""
인증 라우터
===========
로그인, 로그아웃, 토큰 갱신 등

엔드포인트:
- POST /api/v1/auth/login    - 로그인
- POST /api/v1/auth/refresh  - 토큰 갱신
- GET  /api/v1/auth/me       - 현재 사용자 정보
"""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.token import Token, LoginRequest
from app.schemas.user import UserResponse
from app.services.auth_service import AuthService
from app.dependencies import get_auth_service, CurrentUser


# ============================================================================
# 라우터 설정
# ============================================================================

router = APIRouter(
    prefix="/auth",     # URL 접두사: /api/v1/auth
    tags=["인증"],       # Swagger 문서에서 그룹화
)


# ============================================================================
# 엔드포인트
# ============================================================================

@router.post(
    "/login",
    response_model=Token,
    summary="로그인",
    description="이메일과 비밀번호로 로그인하여 JWT 토큰을 발급받습니다."
)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(get_auth_service)
) -> Token:
    """
    로그인 엔드포인트

    OAuth2PasswordRequestForm 사용:
    - Swagger UI에서 "Authorize" 버튼으로 테스트 가능
    - username, password 필드 사용 (email을 username으로 받음)

    Returns:
        Token: access_token, refresh_token
    """
    # form_data.username에 이메일이 들어옴
    return await auth_service.login(
        email=form_data.username,
        password=form_data.password
    )


@router.post(
    "/login/json",
    response_model=Token,
    summary="로그인 (JSON)",
    description="JSON 형식으로 로그인합니다."
)
async def login_json(
    login_data: LoginRequest,
    auth_service: AuthService = Depends(get_auth_service)
) -> Token:
    """
    JSON 바디로 로그인

    모바일 앱 등에서 사용
    """
    return await auth_service.login(
        email=login_data.email,
        password=login_data.password
    )


@router.post(
    "/refresh",
    response_model=Token,
    summary="토큰 갱신",
    description="Refresh Token으로 새 Access Token을 발급받습니다."
)
async def refresh_token(
    refresh_token: str,
    auth_service: AuthService = Depends(get_auth_service)
) -> Token:
    """
    Access Token 갱신

    Access Token 만료 시 호출
    Refresh Token은 유효해야 함
    """
    return await auth_service.refresh_access_token(refresh_token)


@router.get(
    "/me",
    response_model=UserResponse,
    summary="현재 사용자 정보",
    description="로그인한 사용자의 정보를 반환합니다."
)
async def get_current_user_info(
    current_user: CurrentUser  # 의존성 주입으로 자동 인증
) -> UserResponse:
    """
    현재 로그인한 사용자 정보

    Authorization: Bearer <token> 헤더 필요

    의존성 체인:
    1. oauth2_scheme → 토큰 추출
    2. get_current_user → 사용자 조회
    3. 여기서 current_user로 받음
    """
    return current_user
