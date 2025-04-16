"""
에러 처리 모범 사례
이 파일은 Python에서 에러 처리를 위한 모범 사례를 다룹니다.
"""

import logging
import traceback
from typing import Optional, Dict, Any
import sys
import os
from datetime import datetime

# 로깅 설정
def setup_logging(log_file: Optional[str] = None) -> logging.Logger:
    """로깅 설정 함수"""
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

class ErrorHandler:
    """에러 처리 유틸리티 클래스"""
    
    @staticmethod
    def handle_error(error: Exception, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """에러 처리 함수"""
        error_info = {
            "error_type": type(error).__name__,
            "error_message": str(error),
            "timestamp": datetime.now().isoformat(),
            "context": context or {}
        }
        
        # 스택 트레이스 추가
        error_info["stack_trace"] = traceback.format_exc()
        
        return error_info
    
    @staticmethod
    def log_error(logger: logging.Logger, error: Exception, context: Dict[str, Any] = None) -> None:
        """에러 로깅 함수"""
        error_info = ErrorHandler.handle_error(error, context)
        
        # 에러 로깅
        logger.error(f"Error occurred: {error_info['error_type']} - {error_info['error_message']}")
        logger.debug(f"Error details: {error_info}")
        
        # 스택 트레이스 로깅
        logger.debug(f"Stack trace:\n{error_info['stack_trace']}")

class UserService:
    """사용자 관련 서비스 클래스"""
    
    def __init__(self, logger: logging.Logger):
        self.logger = logger
        self.users = {
            1: {"name": "John Doe", "email": "john@example.com"},
            2: {"name": "Jane Smith", "email": "jane@example.com"}
        }
    
    def get_user(self, user_id: int) -> Dict[str, Any]:
        """사용자 정보 조회"""
        context = {"user_id": user_id, "operation": "get_user"}
        
        try:
            if user_id not in self.users:
                raise ValueError(f"User with ID {user_id} not found")
            
            user = self.users[user_id]
            self.logger.info(f"Successfully retrieved user: {user}")
            return user
            
        except Exception as e:
            ErrorHandler.log_error(self.logger, e, context)
            raise
    
    def create_user(self, name: str, email: str) -> Dict[str, Any]:
        """새로운 사용자 생성"""
        context = {"name": name, "email": email, "operation": "create_user"}
        
        try:
            # 데이터 검증
            if not name or not email:
                raise ValueError("Name and email are required")
            
            if "@" not in email:
                raise ValueError("Invalid email format")
            
            # 사용자 생성
            user_id = max(self.users.keys()) + 1
            user = {"id": user_id, "name": name, "email": email}
            self.users[user_id] = user
            
            self.logger.info(f"Successfully created user: {user}")
            return user
            
        except Exception as e:
            ErrorHandler.log_error(self.logger, e, context)
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
    
    try:
        # 사용자 조회 예제
        user = service.get_user(1)
        logger.info(f"Found user: {user}")
        
        # 사용자 생성 예제
        new_user = service.create_user("Alice", "alice@example.com")
        logger.info(f"Created user: {new_user}")
        
        # 잘못된 이메일 형식 예제
        service.create_user("Bob", "invalid-email")
        
    except Exception as e:
        logger.error(f"Application error: {e}")
        sys.exit(1)
    
    logger.info("Application finished successfully")

if __name__ == "__main__":
    main() 