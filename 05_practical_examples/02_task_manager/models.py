from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class User:
    id: str
    username: str
    email: str
    password: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    def __post_init__(self):
        if not self.id:
            self.id = f"user_{datetime.now().timestamp()}"

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            username=data.get("username"),
            email=data.get("email"),
            password=data.get("password"),
            created_at=datetime.fromisoformat(data.get("created_at")),
            updated_at=datetime.fromisoformat(data.get("updated_at"))
        )

@dataclass
class Task:
    id: str
    title: str
    description: str
    status: str
    priority: str
    due_date: datetime
    user_id: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    def __post_init__(self):
        if not self.id:
            self.id = f"task_{datetime.now().timestamp()}"
        if self.status not in ["todo", "in_progress", "done"]:
            raise ValueError("Invalid status")
        if self.priority not in ["low", "medium", "high"]:
            raise ValueError("Invalid priority")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "priority": self.priority,
            "due_date": self.due_date.isoformat(),
            "user_id": self.user_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            title=data.get("title"),
            description=data.get("description"),
            status=data.get("status"),
            priority=data.get("priority"),
            due_date=datetime.fromisoformat(data.get("due_date")),
            user_id=data.get("user_id"),
            created_at=datetime.fromisoformat(data.get("created_at")),
            updated_at=datetime.fromisoformat(data.get("updated_at"))
        )

@dataclass
class Comment:
    id: str
    content: str
    task_id: str
    user_id: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    def __post_init__(self):
        if not self.id:
            self.id = f"comment_{datetime.now().timestamp()}"

    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content,
            "task_id": self.task_id,
            "user_id": self.user_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data.get("id"),
            content=data.get("content"),
            task_id=data.get("task_id"),
            user_id=data.get("user_id"),
            created_at=datetime.fromisoformat(data.get("created_at")),
            updated_at=datetime.fromisoformat(data.get("updated_at"))
        ) 