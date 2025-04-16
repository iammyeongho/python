"""
데이터베이스 관련 예외
이 파일은 Python에서 데이터베이스 작업 시 발생할 수 있는 예외와 그 처리 방법을 다룹니다.
"""

import sqlite3
import pymysql
from typing import Optional, Dict, List
import logging
from datetime import datetime

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DatabaseError(Exception):
    """데이터베이스 작업 실패 시 발생하는 예외"""
    def __init__(self, message: str, sql: str = None):
        self.message = message
        self.sql = sql
        super().__init__(self.message)

class DatabaseService:
    """데이터베이스 서비스 클래스"""
    
    def __init__(self, db_type: str = "sqlite", **kwargs):
        self.db_type = db_type
        self.connection = None
        self.connect(**kwargs)
    
    def connect(self, **kwargs) -> None:
        """데이터베이스 연결"""
        try:
            if self.db_type == "sqlite":
                self.connection = sqlite3.connect(kwargs.get("database", ":memory:"))
            elif self.db_type == "mysql":
                self.connection = pymysql.connect(**kwargs)
            else:
                raise ValueError(f"Unsupported database type: {self.db_type}")
            
            logger.info(f"Successfully connected to {self.db_type} database")
        except Exception as e:
            logger.error(f"Failed to connect to database: {e}")
            raise DatabaseError("Failed to connect to database") from e
    
    def execute_query(self, query: str, params: tuple = None) -> List[Dict]:
        """쿼리 실행"""
        logger.info(f"Executing query: {query}")
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params or ())
            
            if query.strip().upper().startswith("SELECT"):
                columns = [desc[0] for desc in cursor.description]
                results = []
                for row in cursor.fetchall():
                    results.append(dict(zip(columns, row)))
                return results
            else:
                self.connection.commit()
                return []
        except Exception as e:
            logger.error(f"Query execution failed: {e}")
            self.connection.rollback()
            raise DatabaseError("Query execution failed", query) from e
        finally:
            cursor.close()
    
    def create_tables(self) -> None:
        """테이블 생성"""
        try:
            # 사용자 테이블 생성
            self.execute_query("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)
            
            # 게시물 테이블 생성
            self.execute_query("""
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                content TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
            """)
            
            logger.info("Tables created successfully")
        except Exception as e:
            logger.error(f"Failed to create tables: {e}")
            raise
    
    def insert_user(self, username: str, email: str) -> int:
        """사용자 추가"""
        try:
            self.execute_query(
                "INSERT INTO users (username, email) VALUES (?, ?)",
                (username, email)
            )
            return self.connection.cursor().lastrowid
        except Exception as e:
            logger.error(f"Failed to insert user: {e}")
            raise
    
    def insert_post(self, user_id: int, title: str, content: str) -> int:
        """게시물 추가"""
        try:
            self.execute_query(
                "INSERT INTO posts (user_id, title, content) VALUES (?, ?, ?)",
                (user_id, title, content)
            )
            return self.connection.cursor().lastrowid
        except Exception as e:
            logger.error(f"Failed to insert post: {e}")
            raise
    
    def get_user(self, user_id: int) -> Optional[Dict]:
        """사용자 조회"""
        try:
            results = self.execute_query(
                "SELECT * FROM users WHERE id = ?",
                (user_id,)
            )
            return results[0] if results else None
        except Exception as e:
            logger.error(f"Failed to get user: {e}")
            raise
    
    def get_user_posts(self, user_id: int) -> List[Dict]:
        """사용자의 게시물 조회"""
        try:
            return self.execute_query(
                "SELECT * FROM posts WHERE user_id = ?",
                (user_id,)
            )
        except Exception as e:
            logger.error(f"Failed to get user posts: {e}")
            raise
    
    def close(self) -> None:
        """데이터베이스 연결 종료"""
        if self.connection:
            self.connection.close()
            logger.info("Database connection closed")

def main():
    """메인 함수"""
    # SQLite 예제
    try:
        db = DatabaseService("sqlite", database=":memory:")
        db.create_tables()
        
        # 사용자 추가
        user_id = db.insert_user("john_doe", "john@example.com")
        print(f"Created user with ID: {user_id}")
        
        # 게시물 추가
        post_id = db.insert_post(user_id, "First Post", "Hello, World!")
        print(f"Created post with ID: {post_id}")
        
        # 사용자 조회
        user = db.get_user(user_id)
        print(f"User: {user}")
        
        # 게시물 조회
        posts = db.get_user_posts(user_id)
        print(f"Posts: {posts}")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'db' in locals():
            db.close()
    
    # MySQL 예제 (설정 필요)
    try:
        db = DatabaseService("mysql",
                           host="localhost",
                           user="root",
                           password="password",
                           database="example_db")
        # MySQL 관련 작업...
    except Exception as e:
        print(f"MySQL Error: {e}")
    finally:
        if 'db' in locals():
            db.close()

if __name__ == "__main__":
    main() 