"""
파일 처리 관련 예외
이 파일은 Python에서 파일 처리 시 발생할 수 있는 예외와 그 처리 방법을 다룹니다.
"""

import os
import shutil
from typing import Optional
import logging

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class FileHandler:
    """파일 처리 클래스"""
    
    def __init__(self, base_dir: str = "."):
        self.base_dir = base_dir
    
    def read_file(self, filename: str) -> str:
        """파일 읽기"""
        filepath = os.path.join(self.base_dir, filename)
        logger.info(f"Attempting to read file: {filepath}")
        
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            logger.info(f"Successfully read file: {filepath}")
            return content
        except FileNotFoundError:
            logger.error(f"File not found: {filepath}")
            raise
        except PermissionError:
            logger.error(f"Permission denied: {filepath}")
            raise
        except UnicodeDecodeError:
            logger.error(f"Failed to decode file: {filepath}")
            raise
        except Exception as e:
            logger.error(f"Error reading file: {e}")
            raise
    
    def write_file(self, filename: str, content: str) -> None:
        """파일 쓰기"""
        filepath = os.path.join(self.base_dir, filename)
        logger.info(f"Attempting to write file: {filepath}")
        
        try:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(content)
            logger.info(f"Successfully wrote file: {filepath}")
        except PermissionError:
            logger.error(f"Permission denied: {filepath}")
            raise
        except Exception as e:
            logger.error(f"Error writing file: {e}")
            raise
    
    def copy_file(self, source: str, destination: str) -> None:
        """파일 복사"""
        source_path = os.path.join(self.base_dir, source)
        dest_path = os.path.join(self.base_dir, destination)
        logger.info(f"Attempting to copy file: {source_path} -> {dest_path}")
        
        try:
            shutil.copy2(source_path, dest_path)
            logger.info(f"Successfully copied file: {source_path} -> {dest_path}")
        except FileNotFoundError:
            logger.error(f"Source file not found: {source_path}")
            raise
        except PermissionError:
            logger.error(f"Permission denied: {dest_path}")
            raise
        except Exception as e:
            logger.error(f"Error copying file: {e}")
            raise
    
    def delete_file(self, filename: str) -> None:
        """파일 삭제"""
        filepath = os.path.join(self.base_dir, filename)
        logger.info(f"Attempting to delete file: {filepath}")
        
        try:
            os.remove(filepath)
            logger.info(f"Successfully deleted file: {filepath}")
        except FileNotFoundError:
            logger.error(f"File not found: {filepath}")
            raise
        except PermissionError:
            logger.error(f"Permission denied: {filepath}")
            raise
        except Exception as e:
            logger.error(f"Error deleting file: {e}")
            raise

def main():
    """메인 함수"""
    handler = FileHandler()
    
    # 파일 읽기 예제
    try:
        content = handler.read_file("example.txt")
        print(f"File content: {content}")
    except Exception as e:
        print(f"Error reading file: {e}")
    
    # 파일 쓰기 예제
    try:
        handler.write_file("new_file.txt", "Hello, World!")
        print("File written successfully")
    except Exception as e:
        print(f"Error writing file: {e}")
    
    # 파일 복사 예제
    try:
        handler.copy_file("new_file.txt", "copy.txt")
        print("File copied successfully")
    except Exception as e:
        print(f"Error copying file: {e}")
    
    # 파일 삭제 예제
    try:
        handler.delete_file("copy.txt")
        print("File deleted successfully")
    except Exception as e:
        print(f"Error deleting file: {e}")

if __name__ == "__main__":
    main() 