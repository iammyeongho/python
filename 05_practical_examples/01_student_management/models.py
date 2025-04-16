# 학생 관리 시스템 - 모델
# 작성일: 2024-04-16
# 목적: 학생, 성적, 출석, 학급 정보를 표현하는 모델 클래스 정의

from dataclasses import dataclass
from typing import Optional, List
from datetime import date

@dataclass
class Class:
    """
    학급 정보를 저장하는 데이터 클래스
    
    속성:
        id (Optional[int]): 학급 ID
        name (str): 학급 이름
        grade (int): 학년
        teacher (str): 담임 선생님
        room_number (str): 교실 번호
    """
    id: Optional[int] = None
    name: str = ""
    grade: int = 0
    teacher: str = ""
    room_number: str = ""
    
    def __post_init__(self):
        if self.id is None:
            self.id = id(self)  # 임시 ID 생성

    def __str__(self) -> str:
        return f"{self.grade}학년 {self.name}반 (담임: {self.teacher})"
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "grade": self.grade,
            "teacher": self.teacher,
            "room_number": self.room_number
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Class':
        return cls(
            id=data.get("id"),
            name=data.get("name", ""),
            grade=data.get("grade", 0),
            teacher=data.get("teacher", ""),
            room_number=data.get("room_number", "")
        )

@dataclass
class Student:
    """
    학생 정보를 저장하는 데이터 클래스
    
    속성:
        id (Optional[int]): 학생 ID
        name (str): 학생 이름
        student_id (str): 학번
        birth_date (date): 생년월일
        class_id (int): 소속 학급 ID
        phone (str): 연락처
        address (str): 주소
    """
    id: Optional[int] = None
    name: str = ""
    student_id: str = ""
    birth_date: date = date.today()
    class_id: int = 0
    phone: str = ""
    address: str = ""
    
    def __post_init__(self):
        if self.id is None:
            self.id = id(self)  # 임시 ID 생성

    def __str__(self) -> str:
        return f"{self.name} ({self.student_id})"
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "student_id": self.student_id,
            "birth_date": self.birth_date.isoformat(),
            "class_id": self.class_id,
            "phone": self.phone,
            "address": self.address
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Student':
        return cls(
            id=data.get("id"),
            name=data.get("name", ""),
            student_id=data.get("student_id", ""),
            birth_date=date.fromisoformat(data.get("birth_date", "2000-01-01")),
            class_id=data.get("class_id", 0),
            phone=data.get("phone", ""),
            address=data.get("address", "")
        )

@dataclass
class Grade:
    """
    성적 정보를 저장하는 데이터 클래스
    
    속성:
        id (Optional[int]): 성적 ID
        student_id (int): 학생 ID
        subject (str): 과목
        score (float): 점수
        semester (int): 학기
        exam_date (date): 시험일
    """
    id: Optional[int] = None
    student_id: int = 0
    subject: str = ""
    score: float = 0.0
    semester: int = 1
    exam_date: date = date.today()
    
    def __post_init__(self):
        if self.id is None:
            self.id = id(self)  # 임시 ID 생성

    def __str__(self) -> str:
        return f"{self.subject}: {self.score}점 ({self.semester}학기)"
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "student_id": self.student_id,
            "subject": self.subject,
            "score": self.score,
            "semester": self.semester,
            "exam_date": self.exam_date.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Grade':
        return cls(
            id=data.get("id"),
            student_id=data.get("student_id", 0),
            subject=data.get("subject", ""),
            score=data.get("score", 0.0),
            semester=data.get("semester", 1),
            exam_date=date.fromisoformat(data.get("exam_date", "2000-01-01"))
        )

@dataclass
class Attendance:
    """
    출석 정보를 저장하는 데이터 클래스
    
    속성:
        id (Optional[int]): 출석 ID
        student_id (int): 학생 ID
        date (date): 날짜
        status (str): 출석 상태 (출석, 지각, 결석, 조퇴)
        reason (Optional[str]): 결석/지각 사유
    """
    id: Optional[int] = None
    student_id: int = 0
    date: date = date.today()
    status: str = "출석"  # 출석, 지각, 조퇴, 결석
    reason: Optional[str] = None
    
    def __post_init__(self):
        if self.id is None:
            self.id = id(self)  # 임시 ID 생성

    def __str__(self) -> str:
        return f"{self.date}: {self.status}" + (f" ({self.reason})" if self.reason else "")
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "student_id": self.student_id,
            "date": self.date.isoformat(),
            "status": self.status,
            "reason": self.reason
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Attendance':
        return cls(
            id=data.get("id"),
            student_id=data.get("student_id", 0),
            date=date.fromisoformat(data.get("date", "2000-01-01")),
            status=data.get("status", "출석"),
            reason=data.get("reason")
        ) 