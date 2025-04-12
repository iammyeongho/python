# 학생 관리 시스템 - 모델
# 작성일: 2024-04-09
# 목적: 학생 정보를 표현하는 모델 클래스 정의

from dataclasses import dataclass
from typing import Optional

@dataclass
class Student:
    """
    학생 정보를 저장하는 데이터 클래스
    
    속성:
        id (Optional[int]): 학생 ID (데이터베이스에서 자동 생성)
        name (str): 학생 이름
        age (int): 학생 나이
        grade (str): 학생 학년
        major (str): 학생 전공
    """
    name: str
    age: int
    grade: str
    major: str
    id: Optional[int] = None
    
    def __str__(self) -> str:
        """
        학생 정보를 문자열로 반환
        
        반환:
            str: 포맷된 학생 정보 문자열
        """
        return (f"ID: {self.id}, "
                f"이름: {self.name}, "
                f"나이: {self.age}, "
                f"학년: {self.grade}, "
                f"전공: {self.major}")
    
    def to_dict(self) -> dict:
        """
        학생 정보를 딕셔너리 형태로 변환
        
        반환:
            dict: 학생 정보가 담긴 딕셔너리
        """
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
            "major": self.major
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Student':
        """
        딕셔너리로부터 학생 객체 생성
        
        매개변수:
            data (dict): 학생 정보가 담긴 딕셔너리
            
        반환:
            Student: 생성된 학생 객체
        """
        return cls(
            id=data.get("id"),
            name=data.get("name", ""),
            age=data.get("age", 0),
            grade=data.get("grade", ""),
            major=data.get("major", "")
        ) 