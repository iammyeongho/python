"""
API 라우터
==========
HTTP 엔드포인트 정의

라우터의 역할:
1. URL 엔드포인트 정의
2. HTTP 메서드 매핑 (GET, POST, PUT, DELETE)
3. 요청 데이터 검증 (Pydantic Schema)
4. 의존성 주입 (인증, DB 세션 등)
5. 응답 형식 정의

비즈니스 로직은 Service에 위임!
"""

from app.routers import auth, users

__all__ = ["auth", "users"]
