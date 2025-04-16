"""
데이터베이스 통합 테스트 예제
이 파일은 데이터베이스와의 통합 테스트를 수행하는 방법을 보여줍니다.
"""

import unittest
import sqlite3
import os
from datetime import datetime
from typing import List, Optional

class DatabaseManager:
    """데이터베이스 관리 클래스"""
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = None
        self.cursor = None

    def connect(self):
        """데이터베이스에 연결합니다."""
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        """데이터베이스 연결을 종료합니다."""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def create_tables(self):
        """필요한 테이블을 생성합니다."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        self.conn.commit()

    def add_user(self, username: str, email: str) -> int:
        """새로운 사용자를 추가합니다."""
        self.cursor.execute(
            'INSERT INTO users (username, email) VALUES (?, ?)',
            (username, email)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def get_user(self, user_id: int) -> Optional[tuple]:
        """사용자 정보를 조회합니다."""
        self.cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        return self.cursor.fetchone()

    def add_post(self, user_id: int, title: str, content: str) -> int:
        """새로운 게시글을 추가합니다."""
        self.cursor.execute(
            'INSERT INTO posts (user_id, title, content) VALUES (?, ?, ?)',
            (user_id, title, content)
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def get_user_posts(self, user_id: int) -> List[tuple]:
        """사용자의 게시글 목록을 조회합니다."""
        self.cursor.execute('SELECT * FROM posts WHERE user_id = ?', (user_id,))
        return self.cursor.fetchall()

class TestDatabaseIntegration(unittest.TestCase):
    """데이터베이스 통합 테스트"""

    @classmethod
    def setUpClass(cls):
        """테스트 클래스 시작 시 호출됩니다."""
        cls.db_path = 'test_database.db'
        cls.db = DatabaseManager(cls.db_path)
        cls.db.connect()
        cls.db.create_tables()

    @classmethod
    def tearDownClass(cls):
        """테스트 클래스 종료 시 호출됩니다."""
        cls.db.disconnect()
        if os.path.exists(cls.db_path):
            os.remove(cls.db_path)

    def setUp(self):
        """각 테스트 메서드 실행 전에 호출됩니다."""
        # 테스트 데이터 초기화
        self.db.cursor.execute('DELETE FROM posts')
        self.db.cursor.execute('DELETE FROM users')
        self.db.conn.commit()

    def test_user_creation_and_retrieval(self):
        """사용자 생성 및 조회 테스트"""
        # 사용자 생성
        user_id = self.db.add_user('testuser', 'test@example.com')
        
        # 사용자 조회
        user = self.db.get_user(user_id)
        
        # 결과 검증
        self.assertIsNotNone(user)
        self.assertEqual(user[1], 'testuser')
        self.assertEqual(user[2], 'test@example.com')
        self.assertIsInstance(user[3], str)  # created_at

    def test_post_creation_and_retrieval(self):
        """게시글 생성 및 조회 테스트"""
        # 사용자 생성
        user_id = self.db.add_user('testuser', 'test@example.com')
        
        # 게시글 생성
        post_id = self.db.add_post(user_id, 'Test Title', 'Test Content')
        
        # 게시글 조회
        posts = self.db.get_user_posts(user_id)
        
        # 결과 검증
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0][2], user_id)
        self.assertEqual(posts[0][3], 'Test Title')
        self.assertEqual(posts[0][4], 'Test Content')

    def test_user_post_relationship(self):
        """사용자-게시글 관계 테스트"""
        # 사용자 생성
        user_id = self.db.add_user('testuser', 'test@example.com')
        
        # 여러 게시글 생성
        self.db.add_post(user_id, 'Post 1', 'Content 1')
        self.db.add_post(user_id, 'Post 2', 'Content 2')
        
        # 게시글 조회
        posts = self.db.get_user_posts(user_id)
        
        # 결과 검증
        self.assertEqual(len(posts), 2)
        for post in posts:
            self.assertEqual(post[2], user_id)

    def test_unique_constraints(self):
        """유니크 제약 조건 테스트"""
        # 중복되지 않는 사용자 생성
        self.db.add_user('user1', 'email1@example.com')
        
        # 중복된 사용자명으로 생성 시도
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.add_user('user1', 'email2@example.com')
        
        # 중복된 이메일로 생성 시도
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.add_user('user2', 'email1@example.com')

    def test_foreign_key_constraint(self):
        """외래 키 제약 조건 테스트"""
        # 존재하지 않는 사용자 ID로 게시글 생성 시도
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.add_post(999, 'Test Title', 'Test Content')

if __name__ == '__main__':
    unittest.main() 