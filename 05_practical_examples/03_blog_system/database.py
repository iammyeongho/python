import sqlite3
from typing import List, Optional
from datetime import datetime
from models import User, Post, Comment

class Database:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # 사용자 테이블 생성
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # 게시글 테이블 생성
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS posts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL,
                    user_id INTEGER NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            ''')
            
            # 댓글 테이블 생성
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS comments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content TEXT NOT NULL,
                    post_id INTEGER NOT NULL,
                    user_id INTEGER NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (post_id) REFERENCES posts (id),
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            ''')
            
            conn.commit()

    def add_user(self, user: User) -> int:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (username, email, password, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?)
            ''', (user.username, user.email, user.password, 
                  user.created_at, user.updated_at))
            conn.commit()
            return cursor.lastrowid

    def get_user(self, user_id: int) -> Optional[User]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
            row = cursor.fetchone()
            if row:
                return User.from_dict({
                    'id': row[0],
                    'username': row[1],
                    'email': row[2],
                    'password': row[3],
                    'created_at': row[4],
                    'updated_at': row[5]
                })
            return None

    def get_user_by_username(self, username: str) -> Optional[User]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
            row = cursor.fetchone()
            if row:
                return User.from_dict({
                    'id': row[0],
                    'username': row[1],
                    'email': row[2],
                    'password': row[3],
                    'created_at': row[4],
                    'updated_at': row[5]
                })
            return None

    def update_user(self, user: User) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE users 
                SET username = ?, email = ?, password = ?, updated_at = ?
                WHERE id = ?
            ''', (user.username, user.email, user.password, 
                  datetime.now(), user.id))
            conn.commit()
            return cursor.rowcount > 0

    def delete_user(self, user_id: int) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
            conn.commit()
            return cursor.rowcount > 0

    def add_post(self, post: Post) -> int:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO posts (title, content, user_id, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?)
            ''', (post.title, post.content, post.user_id, 
                  post.created_at, post.updated_at))
            conn.commit()
            return cursor.lastrowid

    def get_post(self, post_id: int) -> Optional[Post]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM posts WHERE id = ?', (post_id,))
            row = cursor.fetchone()
            if row:
                return Post.from_dict({
                    'id': row[0],
                    'title': row[1],
                    'content': row[2],
                    'user_id': row[3],
                    'created_at': row[4],
                    'updated_at': row[5]
                })
            return None

    def get_user_posts(self, user_id: int) -> List[Post]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM posts WHERE user_id = ?', (user_id,))
            rows = cursor.fetchall()
            return [Post.from_dict({
                'id': row[0],
                'title': row[1],
                'content': row[2],
                'user_id': row[3],
                'created_at': row[4],
                'updated_at': row[5]
            }) for row in rows]

    def update_post(self, post: Post) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE posts 
                SET title = ?, content = ?, updated_at = ?
                WHERE id = ?
            ''', (post.title, post.content, datetime.now(), post.id))
            conn.commit()
            return cursor.rowcount > 0

    def delete_post(self, post_id: int) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM posts WHERE id = ?', (post_id,))
            conn.commit()
            return cursor.rowcount > 0

    def add_comment(self, comment: Comment) -> int:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO comments (content, post_id, user_id, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?)
            ''', (comment.content, comment.post_id, comment.user_id, 
                  comment.created_at, comment.updated_at))
            conn.commit()
            return cursor.lastrowid

    def get_post_comments(self, post_id: int) -> List[Comment]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM comments WHERE post_id = ?', (post_id,))
            rows = cursor.fetchall()
            return [Comment.from_dict({
                'id': row[0],
                'content': row[1],
                'post_id': row[2],
                'user_id': row[3],
                'created_at': row[4],
                'updated_at': row[5]
            }) for row in rows]

    def update_comment(self, comment: Comment) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE comments 
                SET content = ?, updated_at = ?
                WHERE id = ?
            ''', (comment.content, datetime.now(), comment.id))
            conn.commit()
            return cursor.rowcount > 0

    def delete_comment(self, comment_id: int) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM comments WHERE id = ?', (comment_id,))
            conn.commit()
            return cursor.rowcount > 0 