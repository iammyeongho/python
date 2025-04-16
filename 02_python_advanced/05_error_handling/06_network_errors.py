"""
네트워크 관련 예외
이 파일은 Python에서 네트워크 작업 시 발생할 수 있는 예외와 그 처리 방법을 다룹니다.
"""

import requests
import socket
import urllib3
from typing import Optional
import logging
from urllib3.exceptions import HTTPError, MaxRetryError
from requests.exceptions import RequestException, Timeout, ConnectionError

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class NetworkService:
    """네트워크 서비스 클래스"""
    
    def __init__(self, base_url: str = "https://api.example.com"):
        self.base_url = base_url
        self.session = requests.Session()
    
    def get_data(self, endpoint: str, timeout: int = 5) -> dict:
        """GET 요청 보내기"""
        url = f"{self.base_url}/{endpoint}"
        logger.info(f"Attempting GET request to: {url}")
        
        try:
            response = self.session.get(url, timeout=timeout)
            response.raise_for_status()
            logger.info(f"Successfully received response from: {url}")
            return response.json()
        except Timeout:
            logger.error(f"Request timed out: {url}")
            raise
        except ConnectionError:
            logger.error(f"Connection error: {url}")
            raise
        except HTTPError as e:
            logger.error(f"HTTP error: {e.response.status_code} - {url}")
            raise
        except RequestException as e:
            logger.error(f"Request error: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise
    
    def post_data(self, endpoint: str, data: dict, timeout: int = 5) -> dict:
        """POST 요청 보내기"""
        url = f"{self.base_url}/{endpoint}"
        logger.info(f"Attempting POST request to: {url}")
        
        try:
            response = self.session.post(url, json=data, timeout=timeout)
            response.raise_for_status()
            logger.info(f"Successfully sent data to: {url}")
            return response.json()
        except Timeout:
            logger.error(f"Request timed out: {url}")
            raise
        except ConnectionError:
            logger.error(f"Connection error: {url}")
            raise
        except HTTPError as e:
            logger.error(f"HTTP error: {e.response.status_code} - {url}")
            raise
        except RequestException as e:
            logger.error(f"Request error: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise
    
    def check_connection(self, host: str = "example.com", port: int = 80) -> bool:
        """연결 상태 확인"""
        logger.info(f"Checking connection to {host}:{port}")
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((host, port))
            sock.close()
            
            if result == 0:
                logger.info(f"Successfully connected to {host}:{port}")
                return True
            else:
                logger.error(f"Failed to connect to {host}:{port}")
                return False
        except socket.error as e:
            logger.error(f"Socket error: {e}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return False

def main():
    """메인 함수"""
    service = NetworkService()
    
    # GET 요청 예제
    try:
        data = service.get_data("users/1")
        print(f"Received data: {data}")
    except Exception as e:
        print(f"Error in GET request: {e}")
    
    # POST 요청 예제
    try:
        response = service.post_data("users", {
            "name": "John Doe",
            "email": "john@example.com"
        })
        print(f"POST response: {response}")
    except Exception as e:
        print(f"Error in POST request: {e}")
    
    # 연결 상태 확인 예제
    is_connected = service.check_connection()
    print(f"Connection status: {'Connected' if is_connected else 'Not connected'}")

if __name__ == "__main__":
    main() 