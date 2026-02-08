"""
애플리케이션 설정
=================
환경 변수를 Pydantic Settings로 관리

흐름: .env 파일 → Settings 클래스 → 앱 전체에서 사용
"""

from functools import lru_cache
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """
    애플리케이션 설정

    .env 파일 또는 환경 변수에서 자동으로 값을 로드
    타입 검증도 자동으로 수행
    """

    # 앱 기본 설정
    app_name: str = "FastAPI Project"
    debug: bool = False
    api_v1_prefix: str = "/api/v1"

    # 데이터베이스
    database_url: str = "postgresql+asyncpg://postgres:password@localhost:5432/fastapi_db"

    # JWT 인증
    secret_key: str = "your-secret-key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7

    # CORS
    cors_origins: List[str] = ["http://localhost:3000"]

    class Config:
        # .env 파일에서 설정 로드
        env_file = ".env"
        env_file_encoding = "utf-8"
        # 환경 변수 이름은 대소문자 무시
        case_sensitive = False


@lru_cache()  # 싱글톤 패턴: 설정은 한 번만 로드
def get_settings() -> Settings:
    """
    설정 인스턴스 반환 (캐싱됨)

    사용법:
        from app.config import get_settings
        settings = get_settings()
        print(settings.app_name)
    """
    return Settings()


# 전역에서 바로 사용할 수 있도록 인스턴스 생성
settings = get_settings()
