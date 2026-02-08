"""
User 스키마
===========
사용자 관련 요청/응답 데이터 검증

스키마 네이밍 컨벤션:
- UserCreate: 생성 요청
- UserUpdate: 수정 요청
- UserResponse: 응답 (클라이언트에게 반환)
- UserInDB: DB에 저장된 상태 (내부용)

PHP의 Form Request와 비교:
- Laravel: FormRequest 클래스에서 rules() 정의
- FastAPI: Pydantic 모델로 타입과 규칙 정의
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, ConfigDict


# ============================================================================
# Base 스키마 (공통 필드)
# ============================================================================

class UserBase(BaseModel):
    """
    사용자 공통 필드

    다른 스키마들이 상속받아 사용
    """
    email: EmailStr = Field(
        ...,  # 필수 필드
        description="이메일 주소",
        examples=["user@example.com"]
    )
    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="사용자 이름",
        examples=["홍길동"]
    )


# ============================================================================
# 요청 스키마 (Request)
# ============================================================================

class UserCreate(UserBase):
    """
    사용자 생성 요청

    POST /api/v1/users 요청 바디
    """
    password: str = Field(
        ...,
        min_length=8,
        max_length=100,
        description="비밀번호 (8자 이상)",
        examples=["securePassword123"]
    )


class UserUpdate(BaseModel):
    """
    사용자 수정 요청

    PATCH /api/v1/users/{id} 요청 바디
    모든 필드가 Optional (부분 수정 가능)
    """
    email: Optional[EmailStr] = None
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    password: Optional[str] = Field(None, min_length=8, max_length=100)
    is_active: Optional[bool] = None


# ============================================================================
# 응답 스키마 (Response)
# ============================================================================

class UserResponse(UserBase):
    """
    사용자 응답

    API 응답으로 반환되는 데이터
    비밀번호 같은 민감 정보 제외
    """
    id: int
    is_active: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime

    # SQLAlchemy 모델에서 직접 변환 허용
    model_config = ConfigDict(from_attributes=True)


# ============================================================================
# 내부용 스키마
# ============================================================================

class UserInDB(UserResponse):
    """
    DB에 저장된 사용자 (내부용)

    해시된 비밀번호 포함
    API 응답으로 직접 사용하지 않음
    """
    hashed_password: str
