"""
User 모델
==========
사용자 테이블 정의

이 파일은 DB 테이블 구조만 정의
비즈니스 로직은 Service에, DB 쿼리는 Repository에
"""

from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class User(Base):
    """
    사용자 테이블

    SQLAlchemy 2.0 스타일 (Mapped 사용)

    PHP의 Eloquent Model과 비교:
    - Laravel: $fillable, $hidden, $casts
    - SQLAlchemy: Column 정의로 타입 명시
    """

    __tablename__ = "users"

    # ========================================
    # 컬럼 정의
    # ========================================

    # Primary Key
    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        comment="사용자 ID"
    )

    # 이메일 (유니크)
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,  # 인덱스 생성 (조회 성능)
        nullable=False,
        comment="이메일 주소"
    )

    # 비밀번호 해시
    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        comment="해시된 비밀번호"
    )

    # 이름
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        comment="사용자 이름"
    )

    # 활성화 여부
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        comment="계정 활성화 여부"
    )

    # 관리자 여부
    is_superuser: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        comment="관리자 여부"
    )

    # 생성일시 (자동)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),  # DB에서 기본값 설정
        comment="생성일시"
    )

    # 수정일시 (자동)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),  # 업데이트 시 자동 갱신
        comment="수정일시"
    )

    # ========================================
    # 메서드
    # ========================================

    def __repr__(self) -> str:
        """디버깅용 문자열 표현"""
        return f"<User(id={self.id}, email={self.email})>"

    # 관계 설정 예시 (나중에 추가)
    # posts: Mapped[List["Post"]] = relationship(back_populates="author")
