"""
컨텍스트 매니저와 with 문
이 파일은 Python의 컨텍스트 매니저와 with 문의 사용법을 다룹니다.
"""

import contextlib
from typing import Optional
import time

class DatabaseConnection:
    """데이터베이스 연결을 관리하는 컨텍스트 매니저"""
    
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = None
    
    def __enter__(self):
        """리소스 획득"""
        print(f"Connecting to database: {self.db_name}")
        self.connection = f"Connection to {self.db_name}"
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """리소스 해제"""
        print(f"Closing connection to database: {self.db_name}")
        self.connection = None
        if exc_type is not None:
            print(f"An error occurred: {exc_val}")
        return False  # 예외를 다시 발생시킴

@contextlib.contextmanager
def timer():
    """실행 시간을 측정하는 컨텍스트 매니저"""
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"Execution time: {end - start:.2f} seconds")

class FileHandler:
    """파일 처리를 위한 컨텍스트 매니저"""
    
    def __init__(self, filename: str, mode: str = "r"):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """파일 열기"""
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """파일 닫기"""
        if self.file:
            print(f"Closing file: {self.filename}")
            self.file.close()
        if exc_type is not None:
            print(f"An error occurred: {exc_val}")
        return False  # 예외를 다시 발생시킴

def database_example():
    """데이터베이스 연결 예제"""
    print("\n=== 데이터베이스 연결 예제 ===")
    
    with DatabaseConnection("example_db") as db:
        print(f"Using connection: {db.connection}")
        # 데이터베이스 작업 수행
        print("Executing database operations...")

def timing_example():
    """실행 시간 측정 예제"""
    print("\n=== 실행 시간 측정 예제 ===")
    
    with timer():
        # 시간을 측정할 작업
        time.sleep(1)
        print("Some time-consuming operation...")

def file_example():
    """파일 처리 예제"""
    print("\n=== 파일 처리 예제 ===")
    
    try:
        with FileHandler("example.txt", "w") as file:
            file.write("Hello, World!")
    except Exception as e:
        print(f"File error: {e}")

def main():
    """메인 함수"""
    database_example()
    timing_example()
    file_example()

if __name__ == "__main__":
    main() 