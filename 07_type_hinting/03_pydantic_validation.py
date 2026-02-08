"""
Pydantic - 데이터 검증 및 설정 관리
=====================================
Pydantic을 사용한 런타임 타입 검증 및 데이터 모델링
"""

# pip install pydantic

from datetime import datetime, date
from typing import Optional, List
from enum import Enum

# Pydantic v2 기준
try:
    from pydantic import (
        BaseModel, Field, EmailStr, HttpUrl,
        field_validator, model_validator,
        ConfigDict, computed_field
    )
    PYDANTIC_V2 = True
except ImportError:
    # Pydantic v1 fallback
    from pydantic import BaseModel, Field, validator, root_validator
    PYDANTIC_V2 = False

# =============================================================================
# 1. 기본 모델 정의
# =============================================================================

print("=== 기본 Pydantic 모델 ===")


class User(BaseModel):
    """사용자 모델"""
    id: int
    name: str
    email: str
    age: Optional[int] = None
    is_active: bool = True


# 모델 인스턴스 생성
user = User(id=1, name="Alice", email="alice@example.com")
print(f"User: {user}")
print(f"User dict: {user.model_dump() if PYDANTIC_V2 else user.dict()}")

# 자동 타입 변환
user2 = User(id="2", name="Bob", email="bob@example.com", age="25")
print(f"Auto converted: id={user2.id} (type: {type(user2.id).__name__})")


# =============================================================================
# 2. Field를 사용한 상세 설정
# =============================================================================

print("\n=== Field 설정 ===")


class Product(BaseModel):
    """상품 모델"""
    id: int = Field(..., description="상품 ID")  # ... = 필수
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0, description="가격 (0 초과)")
    quantity: int = Field(default=0, ge=0, description="재고 수량")
    tags: List[str] = Field(default_factory=list)


product = Product(id=1, name="Python Book", price=29.99)
print(f"Product: {product}")

# 유효성 검사 실패 예시
try:
    invalid_product = Product(id=1, name="", price=-10)
except Exception as e:
    print(f"Validation Error: {type(e).__name__}")


# =============================================================================
# 3. 커스텀 Validator
# =============================================================================

print("\n=== 커스텀 Validator ===")

if PYDANTIC_V2:
    class UserWithValidation(BaseModel):
        """검증이 있는 사용자 모델 (Pydantic v2)"""
        username: str
        password: str
        email: str

        @field_validator('username')
        @classmethod
        def username_alphanumeric(cls, v: str) -> str:
            if not v.isalnum():
                raise ValueError('must be alphanumeric')
            return v

        @field_validator('password')
        @classmethod
        def password_strength(cls, v: str) -> str:
            if len(v) < 8:
                raise ValueError('must be at least 8 characters')
            return v

        @model_validator(mode='after')
        def check_username_password(self) -> 'UserWithValidation':
            if self.username in self.password:
                raise ValueError('password should not contain username')
            return self
else:
    class UserWithValidation(BaseModel):
        """검증이 있는 사용자 모델 (Pydantic v1)"""
        username: str
        password: str
        email: str

        @validator('username')
        def username_alphanumeric(cls, v):
            if not v.isalnum():
                raise ValueError('must be alphanumeric')
            return v

        @validator('password')
        def password_strength(cls, v):
            if len(v) < 8:
                raise ValueError('must be at least 8 characters')
            return v


try:
    valid_user = UserWithValidation(
        username="alice123",
        password="securepassword123",
        email="alice@example.com"
    )
    print(f"Valid user: {valid_user.username}")
except Exception as e:
    print(f"Error: {e}")


# =============================================================================
# 4. 중첩 모델
# =============================================================================

print("\n=== 중첩 모델 ===")


class Address(BaseModel):
    """주소 모델"""
    street: str
    city: str
    country: str
    zip_code: Optional[str] = None


class Company(BaseModel):
    """회사 모델"""
    name: str
    address: Address


class Employee(BaseModel):
    """직원 모델"""
    id: int
    name: str
    company: Company
    addresses: List[Address] = []


# 중첩 데이터로 생성
employee_data = {
    "id": 1,
    "name": "John Doe",
    "company": {
        "name": "Tech Corp",
        "address": {
            "street": "123 Tech St",
            "city": "Seoul",
            "country": "Korea"
        }
    },
    "addresses": [
        {"street": "Home St", "city": "Seoul", "country": "Korea"}
    ]
}

employee = Employee(**employee_data)
print(f"Employee: {employee.name}")
print(f"Company: {employee.company.name}")
print(f"Company City: {employee.company.address.city}")


# =============================================================================
# 5. Enum 사용
# =============================================================================

print("\n=== Enum 사용 ===")


class Status(str, Enum):
    """상태 열거형"""
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class Order(BaseModel):
    """주문 모델"""
    id: int
    status: Status = Status.PENDING
    created_at: datetime = Field(default_factory=datetime.now)


order = Order(id=1)
print(f"Order status: {order.status.value}")

order2 = Order(id=2, status="approved")  # 문자열로도 가능
print(f"Order2 status: {order2.status}")


# =============================================================================
# 6. JSON 직렬화
# =============================================================================

print("\n=== JSON 직렬화 ===")


class Article(BaseModel):
    """기사 모델"""
    title: str
    content: str
    published_at: datetime
    tags: List[str] = []


article = Article(
    title="Python Tips",
    content="Learn Python...",
    published_at=datetime.now(),
    tags=["python", "programming"]
)

# JSON으로 변환
if PYDANTIC_V2:
    json_str = article.model_dump_json(indent=2)
else:
    json_str = article.json(indent=2)
print(f"JSON:\n{json_str}")

# JSON에서 모델로
if PYDANTIC_V2:
    article2 = Article.model_validate_json(json_str)
else:
    article2 = Article.parse_raw(json_str)
print(f"Parsed: {article2.title}")


# =============================================================================
# 7. 설정 관리 (Settings)
# =============================================================================

print("\n=== 설정 관리 ===")

try:
    from pydantic_settings import BaseSettings
except ImportError:
    from pydantic import BaseSettings


class AppSettings(BaseSettings):
    """애플리케이션 설정"""
    app_name: str = "MyApp"
    debug: bool = False
    database_url: str = "sqlite:///./test.db"
    secret_key: str = "your-secret-key"
    api_key: Optional[str] = None

    if PYDANTIC_V2:
        model_config = ConfigDict(
            env_file=".env",
            env_prefix="APP_"
        )
    else:
        class Config:
            env_file = ".env"
            env_prefix = "APP_"


# 환경 변수나 .env 파일에서 설정 로드
settings = AppSettings()
print(f"App Name: {settings.app_name}")
print(f"Debug Mode: {settings.debug}")


# =============================================================================
# 8. 고급 기능
# =============================================================================

print("\n=== 고급 기능 ===")


# Computed Field (Pydantic v2)
if PYDANTIC_V2:
    class Rectangle(BaseModel):
        width: float
        height: float

        @computed_field
        @property
        def area(self) -> float:
            return self.width * self.height

    rect = Rectangle(width=10, height=5)
    print(f"Rectangle area: {rect.area}")


# Immutable 모델
class ImmutableUser(BaseModel):
    id: int
    name: str

    if PYDANTIC_V2:
        model_config = ConfigDict(frozen=True)
    else:
        class Config:
            frozen = True


immutable = ImmutableUser(id=1, name="Alice")
# immutable.name = "Bob"  # 에러 발생


# =============================================================================
# 9. 실전 예제: API 요청/응답 모델
# =============================================================================

print("\n=== API 모델 예제 ===")


class CreateUserRequest(BaseModel):
    """사용자 생성 요청"""
    username: str = Field(..., min_length=3, max_length=50)
    email: str
    password: str = Field(..., min_length=8)

    if PYDANTIC_V2:
        @field_validator('email')
        @classmethod
        def validate_email(cls, v: str) -> str:
            if '@' not in v:
                raise ValueError('Invalid email format')
            return v.lower()


class UserResponse(BaseModel):
    """사용자 응답"""
    id: int
    username: str
    email: str
    created_at: datetime

    if PYDANTIC_V2:
        model_config = ConfigDict(from_attributes=True)
    else:
        class Config:
            orm_mode = True  # ORM 객체에서 생성 가능


class PaginatedResponse(BaseModel):
    """페이지네이션 응답"""
    items: List[UserResponse]
    total: int
    page: int
    page_size: int
    has_next: bool


# 요청 처리 예시
request = CreateUserRequest(
    username="newuser",
    email="NEW@Example.com",
    password="securepass123"
)
print(f"Request email (normalized): {request.email}")


# =============================================================================
# 정리: Pydantic 활용 가이드
# =============================================================================

"""
Pydantic 핵심 기능:

1. 데이터 검증
   - 자동 타입 변환
   - 필드별 제약 조건 (min, max, regex 등)
   - 커스텀 validator

2. 직렬화
   - JSON/dict 변환
   - ORM 객체 변환 (orm_mode)

3. 설정 관리
   - 환경 변수 자동 로드
   - .env 파일 지원

4. 문서화
   - JSON Schema 자동 생성
   - OpenAPI/Swagger 통합

PHP 대비 장점:
- 런타임 타입 검증 자동화
- Laravel Validation보다 직관적
- FastAPI와 완벽 통합

버전 차이 (v1 vs v2):
- v2: field_validator, model_validator
- v1: validator, root_validator
- v2: model_dump(), model_dump_json()
- v1: dict(), json()
- v2: model_config = ConfigDict(...)
- v1: class Config: ...
"""
