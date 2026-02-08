"""
SQLAlchemy 모델
================
DB 테이블을 Python 클래스로 정의

모든 모델을 여기서 import하여 Alembic이 감지할 수 있게 함
"""

from app.models.user import User

__all__ = ["User"]
