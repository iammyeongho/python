"""
API 통합 테스트 예제
이 파일은 API와의 통합 테스트를 수행하는 방법을 보여줍니다.
"""

import unittest
import requests
from unittest.mock import patch, MagicMock
from typing import Dict, Any

class APIClient:
    """API 클라이언트 클래스"""
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()

    def get_user(self, user_id: int) -> Dict[str, Any]:
        """사용자 정보를 조회합니다."""
        response = self.session.get(f"{self.base_url}/users/{user_id}")
        response.raise_for_status()
        return response.json()

    def create_user(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """새로운 사용자를 생성합니다."""
        response = self.session.post(
            f"{self.base_url}/users",
            json=user_data
        )
        response.raise_for_status()
        return response.json()

    def update_user(self, user_id: int, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """사용자 정보를 업데이트합니다."""
        response = self.session.put(
            f"{self.base_url}/users/{user_id}",
            json=user_data
        )
        response.raise_for_status()
        return response.json()

    def delete_user(self, user_id: int) -> None:
        """사용자를 삭제합니다."""
        response = self.session.delete(f"{self.base_url}/users/{user_id}")
        response.raise_for_status()

class TestAPIIntegration(unittest.TestCase):
    """API 통합 테스트"""

    def setUp(self):
        """각 테스트 메서드 실행 전에 호출됩니다."""
        self.base_url = "https://api.example.com"
        self.client = APIClient(self.base_url)
        self.mock_response = MagicMock()

    @patch('requests.Session.get')
    def test_get_user(self, mock_get):
        """사용자 조회 테스트"""
        # 모킹된 응답 설정
        expected_user = {
            "id": 1,
            "username": "testuser",
            "email": "test@example.com"
        }
        self.mock_response.json.return_value = expected_user
        self.mock_response.raise_for_status.return_value = None
        mock_get.return_value = self.mock_response

        # API 호출
        user = self.client.get_user(1)

        # 결과 검증
        self.assertEqual(user, expected_user)
        mock_get.assert_called_once_with(f"{self.base_url}/users/1")

    @patch('requests.Session.post')
    def test_create_user(self, mock_post):
        """사용자 생성 테스트"""
        # 모킹된 응답 설정
        user_data = {
            "username": "newuser",
            "email": "new@example.com"
        }
        expected_response = {
            "id": 2,
            **user_data
        }
        self.mock_response.json.return_value = expected_response
        self.mock_response.raise_for_status.return_value = None
        mock_post.return_value = self.mock_response

        # API 호출
        response = self.client.create_user(user_data)

        # 결과 검증
        self.assertEqual(response, expected_response)
        mock_post.assert_called_once_with(
            f"{self.base_url}/users",
            json=user_data
        )

    @patch('requests.Session.put')
    def test_update_user(self, mock_put):
        """사용자 정보 업데이트 테스트"""
        # 모킹된 응답 설정
        user_id = 1
        update_data = {
            "email": "updated@example.com"
        }
        expected_response = {
            "id": user_id,
            "username": "testuser",
            **update_data
        }
        self.mock_response.json.return_value = expected_response
        self.mock_response.raise_for_status.return_value = None
        mock_put.return_value = self.mock_response

        # API 호출
        response = self.client.update_user(user_id, update_data)

        # 결과 검증
        self.assertEqual(response, expected_response)
        mock_put.assert_called_once_with(
            f"{self.base_url}/users/{user_id}",
            json=update_data
        )

    @patch('requests.Session.delete')
    def test_delete_user(self, mock_delete):
        """사용자 삭제 테스트"""
        # 모킹된 응답 설정
        user_id = 1
        self.mock_response.raise_for_status.return_value = None
        mock_delete.return_value = self.mock_response

        # API 호출
        self.client.delete_user(user_id)

        # 결과 검증
        mock_delete.assert_called_once_with(f"{self.base_url}/users/{user_id}")

    @patch('requests.Session.get')
    def test_error_handling(self, mock_get):
        """오류 처리 테스트"""
        # 모킹된 오류 응답 설정
        self.mock_response.raise_for_status.side_effect = requests.HTTPError("404 Not Found")
        mock_get.return_value = self.mock_response

        # API 호출 및 예외 검증
        with self.assertRaises(requests.HTTPError):
            self.client.get_user(999)

    @patch('requests.Session.post')
    def test_validation_error(self, mock_post):
        """유효성 검사 오류 테스트"""
        # 모킹된 오류 응답 설정
        self.mock_response.raise_for_status.side_effect = requests.HTTPError("400 Bad Request")
        mock_post.return_value = self.mock_response

        # 잘못된 데이터로 API 호출
        invalid_data = {
            "username": "",  # 빈 사용자명
            "email": "invalid-email"  # 잘못된 이메일 형식
        }

        # API 호출 및 예외 검증
        with self.assertRaises(requests.HTTPError):
            self.client.create_user(invalid_data)

if __name__ == '__main__':
    unittest.main() 