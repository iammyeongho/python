"""
로깅과 디버깅
이 파일은 Python의 로깅과 디버깅 기능을 다룹니다.
"""

import logging
import traceback
from typing import Optional
import sys
import os
from datetime import datetime

# 로깅 설정
def setup_logging(log_file: Optional[str] = None):
    """로깅 설정 함수"""
    # 로거 생성
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    
    # 포맷터 생성
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # 콘솔 핸들러
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # 파일 핸들러
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger

class UserService:
    """사용자 관련 서비스 클래스"""
    
    def __init__(self, logger: logging.Logger):
        self.logger = logger
        self.users = {
            1: {"name": "John Doe", "email": "john@example.com"},
            2: {"name": "Jane Smith", "email": "jane@example.com"}
        }
    
    def get_user(self, user_id: int) -> dict:
        """사용자 정보 조회"""
        self.logger.debug(f"Attempting to get user with ID: {user_id}")
        
        try:
            if user_id not in self.users:
                self.logger.warning(f"User not found: {user_id}")
                raise ValueError(f"User with ID {user_id} not found")
            
            user = self.users[user_id]
            self.logger.info(f"Successfully retrieved user: {user}")
            return user
            
        except Exception as e:
            self.logger.error(f"Error getting user: {e}")
            self.logger.error(traceback.format_exc())
            raise
    
    def create_user(self, name: str, email: str) -> dict:
        """새로운 사용자 생성"""
        self.logger.debug(f"Attempting to create user: {name}, {email}")
        
        try:
            # 데이터 검증
            if not name or not email:
                self.logger.warning("Invalid user data: name or email is empty")
                raise ValueError("Name and email are required")
            
            if "@" not in email:
                self.logger.warning(f"Invalid email format: {email}")
                raise ValueError("Invalid email format")
            
            # 사용자 생성
            user_id = max(self.users.keys()) + 1
            user = {"id": user_id, "name": name, "email": email}
            self.users[user_id] = user
            
            self.logger.info(f"Successfully created user: {user}")
            return user
            
        except Exception as e:
            self.logger.error(f"Error creating user: {e}")
            self.logger.error(traceback.format_exc())
            raise

def main():
    """메인 함수"""
    # 로그 파일 설정
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    log_file = os.path.join(
        log_dir,
        f"app_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    )
    
    # 로깅 설정
    logger = setup_logging(log_file)
    logger.info("Application started")
    
    # 서비스 인스턴스 생성
    service = UserService(logger)
    
    # 사용자 조회 예제
    try:
        user = service.get_user(1)
        logger.info(f"Found user: {user}")
    except Exception as e:
        logger.error(f"Error in get_user: {e}")
    
    # 사용자 생성 예제
    try:
        new_user = service.create_user("Alice", "alice@example.com")
        logger.info(f"Created user: {new_user}")
    except Exception as e:
        logger.error(f"Error in create_user: {e}")
    
    # 잘못된 이메일 형식 예제
    try:
        service.create_user("Bob", "invalid-email")
    except Exception as e:
        logger.error(f"Error in create_user with invalid email: {e}")
    
    logger.info("Application finished")

if __name__ == "__main__":
    main() 