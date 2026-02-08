"""
Repository 패턴
===============
DB 접근 로직을 캡슐화

왜 Repository를 사용하는가?
1. DB 로직과 비즈니스 로직 분리
2. 테스트 용이성 (Mock 가능)
3. DB 변경에 유연하게 대응
"""

from app.repositories.user_repository import UserRepository

__all__ = ["UserRepository"]
