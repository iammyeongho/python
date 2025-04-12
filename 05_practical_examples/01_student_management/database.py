# 학생 관리 시스템 - 데이터베이스
# 작성일: 2024-04-09
# 목적: SQLite 데이터베이스를 사용한 학생 정보 관리

import sqlite3
from typing import List, Optional, Tuple
from contextlib import contextmanager
from models import Student

class Database:
    """
    SQLite 데이터베이스를 사용하여 학생 정보를 관리하는 클래스
    
    속성:
        db_path (str): 데이터베이스 파일 경로
    """
    
    def __init__(self, db_path: str = "students.db"):
        """
        데이터베이스 연결 초기화
        
        매개변수:
            db_path (str): 데이터베이스 파일 경로. 기본값 "students.db"
        """
        self.db_path = db_path
        self._create_tables()
    
    @contextmanager
    def _get_connection(self):
        """
        데이터베이스 연결을 관리하는 컨텍스트 매니저
        
        반환:
            sqlite3.Connection: 데이터베이스 연결 객체
        """
        conn = sqlite3.connect(self.db_path)
        try:
            yield conn
        finally:
            conn.close()
    
    def _create_tables(self) -> None:
        """
        필요한 테이블을 생성
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    grade TEXT NOT NULL,
                    major TEXT NOT NULL
                )
            """)
            conn.commit()
    
    def add_student(self, student: Student) -> int:
        """
        새로운 학생을 추가
        
        매개변수:
            student (Student): 추가할 학생 객체
            
        반환:
            int: 생성된 학생 ID
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO students (name, age, grade, major)
                VALUES (?, ?, ?, ?)
            """, (student.name, student.age, student.grade, student.major))
            conn.commit()
            return cursor.lastrowid
    
    def get_student(self, student_id: int) -> Optional[Student]:
        """
        ID로 학생 정보를 조회
        
        매개변수:
            student_id (int): 조회할 학생 ID
            
        반환:
            Optional[Student]: 조회된 학생 객체 또는 None
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, name, age, grade, major
                FROM students
                WHERE id = ?
            """, (student_id,))
            row = cursor.fetchone()
            
            if row:
                return Student(
                    id=row[0],
                    name=row[1],
                    age=row[2],
                    grade=row[3],
                    major=row[4]
                )
            return None
    
    def get_all_students(self) -> List[Student]:
        """
        모든 학생 정보를 조회
        
        반환:
            List[Student]: 학생 객체 리스트
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, name, age, grade, major
                FROM students
                ORDER BY id
            """)
            return [
                Student(
                    id=row[0],
                    name=row[1],
                    age=row[2],
                    grade=row[3],
                    major=row[4]
                )
                for row in cursor.fetchall()
            ]
    
    def update_student(self, student: Student) -> bool:
        """
        학생 정보를 업데이트
        
        매개변수:
            student (Student): 업데이트할 학생 객체
            
        반환:
            bool: 업데이트 성공 여부
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE students
                SET name = ?, age = ?, grade = ?, major = ?
                WHERE id = ?
            """, (student.name, student.age, student.grade, student.major, student.id))
            conn.commit()
            return cursor.rowcount > 0
    
    def delete_student(self, student_id: int) -> bool:
        """
        학생을 삭제
        
        매개변수:
            student_id (int): 삭제할 학생 ID
            
        반환:
            bool: 삭제 성공 여부
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM students
                WHERE id = ?
            """, (student_id,))
            conn.commit()
            return cursor.rowcount > 0
    
    def search_students(self, keyword: str) -> List[Student]:
        """
        키워드로 학생을 검색
        
        매개변수:
            keyword (str): 검색 키워드
            
        반환:
            List[Student]: 검색된 학생 객체 리스트
        """
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, name, age, grade, major
                FROM students
                WHERE name LIKE ? OR major LIKE ?
                ORDER BY id
            """, (f"%{keyword}%", f"%{keyword}%"))
            return [
                Student(
                    id=row[0],
                    name=row[1],
                    age=row[2],
                    grade=row[3],
                    major=row[4]
                )
                for row in cursor.fetchall()
            ] 