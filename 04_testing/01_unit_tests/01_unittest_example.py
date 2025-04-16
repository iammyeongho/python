"""
unittest 모듈을 사용한 단위 테스트 예제
이 파일은 Python의 unittest 모듈을 사용하여 단위 테스트를 작성하는 방법을 보여줍니다.
"""

import unittest
from datetime import datetime
from typing import List, Optional

class User:
    """사용자 정보를 관리하는 클래스"""
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        self.created_at = datetime.now()
        self.is_active = True

    def deactivate(self) -> None:
        """사용자 계정을 비활성화합니다."""
        self.is_active = False

    def update_email(self, new_email: str) -> None:
        """사용자의 이메일을 업데이트합니다."""
        self.email = new_email

class UserRepository:
    """사용자 데이터를 관리하는 저장소 클래스"""
    def __init__(self):
        self.users: List[User] = []

    def add_user(self, user: User) -> None:
        """새로운 사용자를 추가합니다."""
        self.users.append(user)

    def get_user(self, username: str) -> Optional[User]:
        """사용자명으로 사용자를 조회합니다."""
        for user in self.users:
            if user.username == username:
                return user
        return None

    def deactivate_user(self, username: str) -> bool:
        """사용자를 비활성화합니다."""
        user = self.get_user(username)
        if user:
            user.deactivate()
            return True
        return False

class TestUser(unittest.TestCase):
    """User 클래스에 대한 테스트 케이스"""
    
    def setUp(self):
        """각 테스트 메서드 실행 전에 호출됩니다."""
        self.user = User("testuser", "test@example.com")
    
    def test_user_creation(self):
        """사용자 생성 테스트"""
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertTrue(self.user.is_active)
        self.assertIsInstance(self.user.created_at, datetime)
    
    def test_user_deactivation(self):
        """사용자 비활성화 테스트"""
        self.user.deactivate()
        self.assertFalse(self.user.is_active)
    
    def test_email_update(self):
        """이메일 업데이트 테스트"""
        self.user.update_email("new@example.com")
        self.assertEqual(self.user.email, "new@example.com")

class TestUserRepository(unittest.TestCase):
    """UserRepository 클래스에 대한 테스트 케이스"""
    
    def setUp(self):
        """각 테스트 메서드 실행 전에 호출됩니다."""
        self.repository = UserRepository()
        self.user = User("testuser", "test@example.com")
        self.repository.add_user(self.user)
    
    def test_add_user(self):
        """사용자 추가 테스트"""
        self.assertEqual(len(self.repository.users), 1)
        self.assertEqual(self.repository.users[0], self.user)
    
    def test_get_user(self):
        """사용자 조회 테스트"""
        found_user = self.repository.get_user("testuser")
        self.assertIsNotNone(found_user)
        self.assertEqual(found_user.username, "testuser")
        
        not_found_user = self.repository.get_user("nonexistent")
        self.assertIsNone(not_found_user)
    
    def test_deactivate_user(self):
        """사용자 비활성화 테스트"""
        result = self.repository.deactivate_user("testuser")
        self.assertTrue(result)
        self.assertFalse(self.repository.get_user("testuser").is_active)
        
        result = self.repository.deactivate_user("nonexistent")
        self.assertFalse(result)

def suite():
    """테스트 스위트 생성"""
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestUser))
    test_suite.addTest(unittest.makeSuite(TestUserRepository))
    return test_suite

if __name__ == '__main__':
    # 테스트 실행
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite()) 