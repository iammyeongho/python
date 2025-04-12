"""
Python과 PHP의 테스트 프레임워크 비교 예제
이 파일은 PHP 개발자가 Python의 테스트 방식을 이해하는 데 도움을 주기 위한 예제입니다.
"""

import unittest
from unittest.mock import patch, MagicMock
from typing import List, Dict, Optional
from datetime import datetime

class UserService:
    """사용자 서비스 클래스"""
    
    def __init__(self):
        self.users = {
            1: {"id": 1, "name": "John Doe", "email": "john@example.com"},
            2: {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
        }
    
    def get_user(self, user_id: int) -> Dict:
        """사용자 정보 조회"""
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} not found")
        return self.users[user_id]
    
    def create_user(self, name: str, email: str) -> Dict:
        """새로운 사용자 생성"""
        if not name or not email:
            raise ValueError("Name and email are required")
        
        user_id = max(self.users.keys()) + 1
        new_user = {"id": user_id, "name": name, "email": email}
        self.users[user_id] = new_user
        return new_user
    
    def update_user(self, user_id: int, name: Optional[str] = None, email: Optional[str] = None) -> Dict:
        """사용자 정보 업데이트"""
        user = self.get_user(user_id)
        
        if name is not None:
            user["name"] = name
        if email is not None:
            user["email"] = email
        
        self.users[user_id] = user
        return user

class TestUserService(unittest.TestCase):
    """UserService 클래스의 테스트"""
    
    def setUp(self):
        """각 테스트 전에 실행되는 설정"""
        self.service = UserService()
    
    def tearDown(self):
        """각 테스트 후에 실행되는 정리"""
        pass
    
    def test_get_user_success(self):
        """사용자 조회 성공 테스트"""
        user = self.service.get_user(1)
        self.assertEqual(user["id"], 1)
        self.assertEqual(user["name"], "John Doe")
        self.assertEqual(user["email"], "john@example.com")
    
    def test_get_user_not_found(self):
        """사용자 조회 실패 테스트"""
        with self.assertRaises(ValueError):
            self.service.get_user(999)
    
    def test_create_user_success(self):
        """사용자 생성 성공 테스트"""
        new_user = self.service.create_user("Alice", "alice@example.com")
        self.assertEqual(new_user["name"], "Alice")
        self.assertEqual(new_user["email"], "alice@example.com")
        self.assertIn(new_user["id"], self.service.users)
    
    def test_create_user_validation(self):
        """사용자 생성 유효성 검사 테스트"""
        with self.assertRaises(ValueError):
            self.service.create_user("", "alice@example.com")
        with self.assertRaises(ValueError):
            self.service.create_user("Alice", "")
    
    def test_update_user_success(self):
        """사용자 업데이트 성공 테스트"""
        updated_user = self.service.update_user(1, name="John Updated")
        self.assertEqual(updated_user["name"], "John Updated")
        self.assertEqual(self.service.users[1]["name"], "John Updated")
    
    def test_update_user_not_found(self):
        """사용자 업데이트 실패 테스트"""
        with self.assertRaises(ValueError):
            self.service.update_user(999, name="Not Found")

class MockExampleTest(unittest.TestCase):
    """모킹 예제 테스트"""
    
    @patch('datetime.datetime')
    def test_mock_datetime(self, mock_datetime):
        """datetime 모킹 테스트"""
        mock_datetime.now.return_value = datetime(2023, 1, 1)
        current_time = datetime.now()
        self.assertEqual(current_time, datetime(2023, 1, 1))
    
    def test_mock_service(self):
        """서비스 모킹 테스트"""
        mock_service = MagicMock(spec=UserService)
        mock_service.get_user.return_value = {"id": 1, "name": "Mock User"}
        
        user = mock_service.get_user(1)
        self.assertEqual(user["name"], "Mock User")
        mock_service.get_user.assert_called_once_with(1)

def suite():
    """테스트 스위트 생성"""
    test_suite = unittest.TestSuite()
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestUserService))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MockExampleTest))
    return test_suite

if __name__ == '__main__':
    # 단순 실행
    unittest.main()
    
    # 또는 테스트 스위트 실행
    # runner = unittest.TextTestRunner()
    # runner.run(suite()) 