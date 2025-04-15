"""
PHP 개발자를 위한 Python 디버깅 가이드
이 파일은 PHP 개발자가 Python의 디버깅 방식을 이해하는 데 도움을 주기 위한 예제입니다.
"""

import pdb
import logging
from typing import Any, Dict, List

# 로깅 설정
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DebugExample:
    """디버깅 예제를 보여주는 클래스"""

    def __init__(self):
        self.data: Dict[str, Any] = {}
        self.items: List[int] = []

    def add_item(self, key: str, value: Any) -> None:
        """
        데이터를 추가하는 메서드
        
        Args:
            key: 데이터의 키
            value: 저장할 값
        """
        # PHP의 var_dump($value)와 유사한 디버깅
        logger.debug(f"Adding item - Key: {key}, Value: {value}")
        
        # pdb를 사용한 디버깅 (PHP의 xdebug와 유사)
        # pdb.set_trace()  # 이 줄의 주석을 해제하면 디버거가 시작됨
        
        self.data[key] = value
        self.items.append(len(self.data))

    def process_data(self) -> Dict[str, Any]:
        """
        데이터를 처리하는 메서드
        
        Returns:
            처리된 데이터
        """
        try:
            # 예외 발생 가능한 코드
            result = {}
            for key, value in self.data.items():
                # PHP의 print_r($value)와 유사한 디버깅
                logger.debug(f"Processing - Key: {key}, Value: {value}")
                
                # 값이 숫자인 경우에만 처리
                if isinstance(value, (int, float)):
                    result[key] = value * 2
                else:
                    result[key] = str(value).upper()
            
            return result
            
        except Exception as e:
            # PHP의 try-catch와 유사한 예외 처리
            logger.error(f"Error processing data: {str(e)}")
            raise

def debug_example():
    """디버깅 예제 실행 함수"""
    # PHP의 error_reporting(E_ALL)과 유사한 설정
    logger.setLevel(logging.DEBUG)
    
    example = DebugExample()
    
    # 데이터 추가
    example.add_item("name", "John")
    example.add_item("age", 30)
    example.add_item("score", 85.5)
    
    try:
        # 데이터 처리
        result = example.process_data()
        logger.info(f"Processed result: {result}")
        
    except Exception as e:
        logger.error(f"Failed to process data: {str(e)}")

def debug_with_pdb():
    """pdb를 사용한 디버깅 예제"""
    def calculate_average(numbers: List[float]) -> float:
        """
        숫자 리스트의 평균을 계산
        
        Args:
            numbers: 숫자 리스트
            
        Returns:
            평균값
        """
        # pdb 디버거 시작 (PHP의 xdebug_break()와 유사)
        pdb.set_trace()
        
        total = sum(numbers)
        count = len(numbers)
        
        if count == 0:
            return 0.0
            
        return total / count

    # 테스트 데이터
    numbers = [10, 20, 30, 40, 50]
    
    # 평균 계산
    average = calculate_average(numbers)
    print(f"Average: {average}")

def debug_with_logging():
    """로깅을 사용한 디버깅 예제"""
    def process_user_data(user_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        사용자 데이터 처리
        
        Args:
            user_data: 사용자 데이터
            
        Returns:
            처리된 데이터
        """
        logger.info("Starting user data processing")
        logger.debug(f"Input data: {user_data}")
        
        try:
            # 데이터 검증
            if "name" not in user_data:
                raise ValueError("Name is required")
                
            if "age" not in user_data:
                raise ValueError("Age is required")
                
            # 데이터 처리
            processed_data = {
                "name": user_data["name"].upper(),
                "age": user_data["age"] * 2,
                "processed_at": "2024-01-01"
            }
            
            logger.info("User data processed successfully")
            logger.debug(f"Processed data: {processed_data}")
            
            return processed_data
            
        except Exception as e:
            logger.error(f"Error processing user data: {str(e)}")
            raise

    # 테스트 데이터
    user_data = {
        "name": "John",
        "age": 30
    }
    
    # 데이터 처리
    try:
        result = process_user_data(user_data)
        print(f"Processed result: {result}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    # 디버깅 예제 실행
    print("=== Basic Debugging Example ===")
    debug_example()
    
    print("\n=== PDB Debugging Example ===")
    debug_with_pdb()
    
    print("\n=== Logging Debugging Example ===")
    debug_with_logging() 