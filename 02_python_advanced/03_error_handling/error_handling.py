"""
Python과 PHP의 에러 처리 비교 예제
이 파일은 PHP 개발자가 Python의 에러 처리 방식을 이해하는 데 도움을 주기 위한 예제입니다.
"""

import logging
import traceback
from typing import Optional, Union
from dataclasses import dataclass
from datetime import datetime

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 커스텀 예외 클래스들
class ValidationError(Exception):
    """데이터 검증 실패 시 발생하는 예외"""
    pass

class DatabaseError(Exception):
    """데이터베이스 작업 실패 시 발생하는 예외"""
    pass

class UserNotFoundError(Exception):
    """사용자를 찾을 수 없을 때 발생하는 예외"""
    pass

@dataclass
class User:
    """사용자 데이터 클래스"""
    id: int
    name: str
    email: str
    created_at: datetime

class UserService:
    """사용자 관련 서비스 클래스"""
    
    def __init__(self):
        self.users = {
            1: User(1, "John Doe", "john@example.com", datetime.now()),
            2: User(2, "Jane Smith", "jane@example.com", datetime.now())
        }
    
    def get_user(self, user_id: int) -> User:
        """
        사용자 정보 조회
        PHP의 try-catch와 유사한 Python의 try-except 사용 예제
        """
        try:
            if user_id not in self.users:
                raise UserNotFoundError(f"User with ID {user_id} not found")
            return self.users[user_id]
        except UserNotFoundError as e:
            logger.error(f"User not found: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise DatabaseError("Failed to get user") from e
    
    def create_user(self, name: str, email: str) -> User:
        """
        새로운 사용자 생성
        예외 처리와 로깅의 조합 예제
        """
        try:
            # 데이터 검증
            if not name or not email:
                raise ValidationError("Name and email are required")
            
            # 이메일 형식 검증
            if "@" not in email:
                raise ValidationError("Invalid email format")
            
            # 사용자 생성
            user_id = max(self.users.keys()) + 1
            new_user = User(user_id, name, email, datetime.now())
            self.users[user_id] = new_user
            
            logger.info(f"Created new user: {new_user}")
            return new_user
            
        except ValidationError as e:
            logger.warning(f"Validation failed: {e}")
            raise
        except Exception as e:
            logger.error(f"Failed to create user: {e}")
            raise DatabaseError("Failed to create user") from e
    
    def update_user(self, user_id: int, name: Optional[str] = None, email: Optional[str] = None) -> User:
        """
        사용자 정보 업데이트
        try-except-else-finally 블록 사용 예제
        """
        try:
            user = self.get_user(user_id)
            
            if name is not None:
                user.name = name
            if email is not None:
                user.email = email
            
        except UserNotFoundError:
            logger.error(f"User {user_id} not found for update")
            raise
        except Exception as e:
            logger.error(f"Failed to update user: {e}")
            raise DatabaseError("Failed to update user") from e
        else:
            logger.info(f"Successfully updated user {user_id}")
            return user
        finally:
            logger.debug("Update operation completed")

def process_user_data(user_id: int) -> dict:
    """
    사용자 데이터 처리
    예외 전파와 에러 복구 예제
    """
    service = UserService()
    
    try:
        user = service.get_user(user_id)
        return {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "created_at": user.created_at.isoformat()
        }
    except UserNotFoundError:
        logger.error(f"User {user_id} not found")
        return {"error": "User not found", "status": 404}
    except DatabaseError:
        logger.error("Database error occurred")
        return {"error": "Database error", "status": 500}
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        logger.error(traceback.format_exc())
        return {"error": "Internal server error", "status": 500}

def main():
    """메인 실행 함수"""
    service = UserService()
    
    # 사용자 조회 예제
    try:
        user = service.get_user(1)
        print(f"Found user: {user}")
    except UserNotFoundError as e:
        print(f"Error: {e}")
    
    # 사용자 생성 예제
    try:
        new_user = service.create_user("Alice", "alice@example.com")
        print(f"Created user: {new_user}")
    except ValidationError as e:
        print(f"Validation error: {e}")
    except DatabaseError as e:
        print(f"Database error: {e}")
    
    # 사용자 업데이트 예제
    try:
        updated_user = service.update_user(1, name="John Updated")
        print(f"Updated user: {updated_user}")
    except Exception as e:
        print(f"Error updating user: {e}")
    
    # 데이터 처리 예제
    result = process_user_data(1)
    print(f"Processed data: {result}")

if __name__ == "__main__":
    main() 