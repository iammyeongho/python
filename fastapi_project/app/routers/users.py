"""
사용자 라우터
=============
사용자 CRUD API

엔드포인트:
- GET    /api/v1/users          - 사용자 목록 조회
- POST   /api/v1/users          - 사용자 생성 (회원가입)
- GET    /api/v1/users/{id}     - 사용자 상세 조회
- PATCH  /api/v1/users/{id}     - 사용자 수정
- DELETE /api/v1/users/{id}     - 사용자 삭제
"""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Query

from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.services.user_service import UserService
from app.dependencies import (
    get_user_service,
    CurrentUser,
    CurrentSuperuser,
)


# ============================================================================
# 라우터 설정
# ============================================================================

router = APIRouter(
    prefix="/users",
    tags=["사용자"],
)


# ============================================================================
# CRUD 엔드포인트
# ============================================================================

# ----------------------------------------------------------------------------
# CREATE
# ----------------------------------------------------------------------------

@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="회원가입",
    description="새 사용자를 생성합니다."
)
async def create_user(
    user_create: UserCreate,
    user_service: UserService = Depends(get_user_service)
) -> UserResponse:
    """
    회원가입 (사용자 생성)

    요청 바디:
    ```json
    {
        "email": "user@example.com",
        "name": "홍길동",
        "password": "securePassword123"
    }
    ```

    흐름:
    1. Pydantic이 요청 데이터 검증
    2. UserService.create_user() 호출
    3. 이메일 중복 체크 → 비밀번호 해싱 → DB 저장
    4. 생성된 사용자 반환 (비밀번호 제외)
    """
    return await user_service.create_user(user_create)


# ----------------------------------------------------------------------------
# READ
# ----------------------------------------------------------------------------

@router.get(
    "",
    response_model=List[UserResponse],
    summary="사용자 목록",
    description="모든 사용자 목록을 조회합니다. (관리자 전용)"
)
async def get_users(
    skip: int = Query(0, ge=0, description="건너뛸 개수"),
    limit: int = Query(100, ge=1, le=100, description="조회 개수"),
    current_user: CurrentSuperuser = None,  # 관리자만 접근 가능
    user_service: UserService = Depends(get_user_service)
) -> List[UserResponse]:
    """
    사용자 목록 조회 (페이지네이션)

    Query Parameters:
    - skip: 건너뛸 개수 (기본: 0)
    - limit: 조회 개수 (기본: 100, 최대: 100)

    관리자만 접근 가능
    """
    return await user_service.get_users(skip=skip, limit=limit)


@router.get(
    "/{user_id}",
    response_model=UserResponse,
    summary="사용자 상세 조회",
    description="특정 사용자의 정보를 조회합니다."
)
async def get_user(
    user_id: int,
    current_user: CurrentUser = None,  # 로그인 필요
    user_service: UserService = Depends(get_user_service)
) -> UserResponse:
    """
    사용자 상세 조회

    Path Parameters:
    - user_id: 조회할 사용자 ID
    """
    return await user_service.get_user(user_id)


# ----------------------------------------------------------------------------
# UPDATE
# ----------------------------------------------------------------------------

@router.patch(
    "/{user_id}",
    response_model=UserResponse,
    summary="사용자 수정",
    description="사용자 정보를 수정합니다."
)
async def update_user(
    user_id: int,
    user_update: UserUpdate,
    current_user: CurrentUser = None,
    user_service: UserService = Depends(get_user_service)
) -> UserResponse:
    """
    사용자 수정

    본인 또는 관리자만 수정 가능

    요청 바디 (부분 수정 가능):
    ```json
    {
        "name": "새 이름",
        "email": "new@example.com"
    }
    ```
    """
    # 본인 또는 관리자만 수정 가능
    if current_user.id != user_id and not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="권한이 없습니다."
        )

    return await user_service.update_user(user_id, user_update)


# ----------------------------------------------------------------------------
# DELETE
# ----------------------------------------------------------------------------

@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="사용자 삭제",
    description="사용자를 삭제합니다. (관리자 전용)"
)
async def delete_user(
    user_id: int,
    current_user: CurrentSuperuser = None,  # 관리자만
    user_service: UserService = Depends(get_user_service)
) -> None:
    """
    사용자 삭제 (하드 삭제)

    관리자만 접근 가능
    204 No Content 반환
    """
    await user_service.delete_user(user_id)


@router.post(
    "/{user_id}/deactivate",
    response_model=UserResponse,
    summary="사용자 비활성화",
    description="사용자 계정을 비활성화합니다."
)
async def deactivate_user(
    user_id: int,
    current_user: CurrentUser = None,
    user_service: UserService = Depends(get_user_service)
) -> UserResponse:
    """
    사용자 비활성화 (소프트 삭제)

    본인 또는 관리자만 가능
    """
    if current_user.id != user_id and not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="권한이 없습니다."
        )

    return await user_service.deactivate_user(user_id)
