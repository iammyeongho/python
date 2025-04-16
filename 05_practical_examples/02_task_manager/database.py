import sqlite3
from typing import List, Optional
from datetime import datetime
from models import User, Task, Comment

class Database:
    def __init__(self, db_path: str = "task_manager.db"):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # 사용자 테이블 생성
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id TEXT PRIMARY KEY,
                    username TEXT NOT NULL UNIQUE,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )
            """)
            
            # 작업 테이블 생성
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    description TEXT,
                    status TEXT NOT NULL,
                    priority TEXT NOT NULL,
                    due_date TEXT NOT NULL,
                    user_id TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            """)
            
            # 댓글 테이블 생성
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS comments (
                    id TEXT PRIMARY KEY,
                    content TEXT NOT NULL,
                    task_id TEXT NOT NULL,
                    user_id TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    FOREIGN KEY (task_id) REFERENCES tasks (id),
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            """)
            
            conn.commit()

    # 사용자 관련 메서드
    def add_user(self, user: User) -> User:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)",
                (
                    user.id,
                    user.username,
                    user.email,
                    user.password,
                    user.created_at.isoformat(),
                    user.updated_at.isoformat()
                )
            )
            conn.commit()
        return user

    def get_user(self, user_id: str) -> Optional[User]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            row = cursor.fetchone()
            if row:
                return User.from_dict({
                    "id": row[0],
                    "username": row[1],
                    "email": row[2],
                    "password": row[3],
                    "created_at": row[4],
                    "updated_at": row[5]
                })
            return None

    def get_user_by_username(self, username: str) -> Optional[User]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            row = cursor.fetchone()
            if row:
                return User.from_dict({
                    "id": row[0],
                    "username": row[1],
                    "email": row[2],
                    "password": row[3],
                    "created_at": row[4],
                    "updated_at": row[5]
                })
            return None

    def update_user(self, user: User) -> User:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE users 
                SET username = ?, email = ?, password = ?, updated_at = ?
                WHERE id = ?
                """,
                (
                    user.username,
                    user.email,
                    user.password,
                    datetime.now().isoformat(),
                    user.id
                )
            )
            conn.commit()
        return user

    def delete_user(self, user_id: str) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
            conn.commit()
            return cursor.rowcount > 0

    # 작업 관련 메서드
    def add_task(self, task: Task) -> Task:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    task.id,
                    task.title,
                    task.description,
                    task.status,
                    task.priority,
                    task.due_date.isoformat(),
                    task.user_id,
                    task.created_at.isoformat(),
                    task.updated_at.isoformat()
                )
            )
            conn.commit()
        return task

    def get_task(self, task_id: str) -> Optional[Task]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
            row = cursor.fetchone()
            if row:
                return Task.from_dict({
                    "id": row[0],
                    "title": row[1],
                    "description": row[2],
                    "status": row[3],
                    "priority": row[4],
                    "due_date": row[5],
                    "user_id": row[6],
                    "created_at": row[7],
                    "updated_at": row[8]
                })
            return None

    def get_user_tasks(self, user_id: str) -> List[Task]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tasks WHERE user_id = ?", (user_id,))
            rows = cursor.fetchall()
            return [
                Task.from_dict({
                    "id": row[0],
                    "title": row[1],
                    "description": row[2],
                    "status": row[3],
                    "priority": row[4],
                    "due_date": row[5],
                    "user_id": row[6],
                    "created_at": row[7],
                    "updated_at": row[8]
                })
                for row in rows
            ]

    def update_task(self, task: Task) -> Task:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE tasks 
                SET title = ?, description = ?, status = ?,
                    priority = ?, due_date = ?, updated_at = ?
                WHERE id = ?
                """,
                (
                    task.title,
                    task.description,
                    task.status,
                    task.priority,
                    task.due_date.isoformat(),
                    datetime.now().isoformat(),
                    task.id
                )
            )
            conn.commit()
        return task

    def delete_task(self, task_id: str) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            conn.commit()
            return cursor.rowcount > 0

    # 댓글 관련 메서드
    def add_comment(self, comment: Comment) -> Comment:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO comments VALUES (?, ?, ?, ?, ?, ?)",
                (
                    comment.id,
                    comment.content,
                    comment.task_id,
                    comment.user_id,
                    comment.created_at.isoformat(),
                    comment.updated_at.isoformat()
                )
            )
            conn.commit()
        return comment

    def get_task_comments(self, task_id: str) -> List[Comment]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM comments WHERE task_id = ?", (task_id,))
            rows = cursor.fetchall()
            return [
                Comment.from_dict({
                    "id": row[0],
                    "content": row[1],
                    "task_id": row[2],
                    "user_id": row[3],
                    "created_at": row[4],
                    "updated_at": row[5]
                })
                for row in rows
            ]

    def update_comment(self, comment: Comment) -> Comment:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                UPDATE comments 
                SET content = ?, updated_at = ?
                WHERE id = ?
                """,
                (
                    comment.content,
                    datetime.now().isoformat(),
                    comment.id
                )
            )
            conn.commit()
        return comment

    def delete_comment(self, comment_id: str) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM comments WHERE id = ?", (comment_id,))
            conn.commit()
            return cursor.rowcount > 0 