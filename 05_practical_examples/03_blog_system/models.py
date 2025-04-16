from datetime import datetime
from typing import List, Optional

class User:
    def __init__(self, id: int, username: str, email: str, password: str, 
                 created_at: datetime = None, updated_at: datetime = None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'User':
        return cls(
            id=data['id'],
            username=data['username'],
            email=data['email'],
            password=data['password'],
            created_at=datetime.fromisoformat(data['created_at']),
            updated_at=datetime.fromisoformat(data['updated_at'])
        )

class Post:
    def __init__(self, id: int, title: str, content: str, user_id: int,
                 created_at: datetime = None, updated_at: datetime = None):
        self.id = id
        self.title = title
        self.content = content
        self.user_id = user_id
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Post':
        return cls(
            id=data['id'],
            title=data['title'],
            content=data['content'],
            user_id=data['user_id'],
            created_at=datetime.fromisoformat(data['created_at']),
            updated_at=datetime.fromisoformat(data['updated_at'])
        )

class Comment:
    def __init__(self, id: int, content: str, post_id: int, user_id: int,
                 created_at: datetime = None, updated_at: datetime = None):
        self.id = id
        self.content = content
        self.post_id = post_id
        self.user_id = user_id
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'content': self.content,
            'post_id': self.post_id,
            'user_id': self.user_id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Comment':
        return cls(
            id=data['id'],
            content=data['content'],
            post_id=data['post_id'],
            user_id=data['user_id'],
            created_at=datetime.fromisoformat(data['created_at']),
            updated_at=datetime.fromisoformat(data['updated_at'])
        ) 