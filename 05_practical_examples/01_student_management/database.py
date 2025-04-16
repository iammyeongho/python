# 학생 관리 시스템 - 데이터베이스
# 작성일: 2024-04-16
# 목적: 데이터베이스 연결 및 CRUD 작업 처리

import sqlite3
from typing import List, Optional
from datetime import date
from models import Student, Class, Grade, Attendance

class Database:
    """
    SQLite 데이터베이스를 사용하여 학생 정보를 관리하는 클래스
    
    속성:
        db_path (str): 데이터베이스 파일 경로
    """
    
    def __init__(self, db_path: str = "student_management.db"):
        """
        데이터베이스 연결 초기화
        
        매개변수:
            db_path (str): 데이터베이스 파일 경로. 기본값 "student_management.db"
        """
        self.db_path = db_path
        self._init_db()
    
    def _get_connection(self):
        return sqlite3.connect(self.db_path)
    
    def _init_db(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            # 학급 테이블
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS classes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    grade INTEGER NOT NULL,
                    teacher TEXT NOT NULL,
                    room_number TEXT NOT NULL
                )
            ''')
            
            # 학생 테이블
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    student_id TEXT UNIQUE NOT NULL,
                    birth_date DATE NOT NULL,
                    class_id INTEGER NOT NULL,
                    phone TEXT,
                    address TEXT,
                    FOREIGN KEY (class_id) REFERENCES classes (id)
                )
            ''')
            
            # 성적 테이블
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS grades (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER NOT NULL,
                    subject TEXT NOT NULL,
                    score REAL NOT NULL,
                    semester INTEGER NOT NULL,
                    exam_date DATE NOT NULL,
                    FOREIGN KEY (student_id) REFERENCES students (id)
                )
            ''')
            
            # 출석 테이블
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS attendance (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER NOT NULL,
                    date DATE NOT NULL,
                    status TEXT NOT NULL,
                    reason TEXT,
                    FOREIGN KEY (student_id) REFERENCES students (id)
                )
            ''')
            
            conn.commit()
    
    # 학급 관련 메서드
    def add_class(self, class_: Class) -> int:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO classes (name, grade, teacher, room_number)
                VALUES (?, ?, ?, ?)
            ''', (class_.name, class_.grade, class_.teacher, class_.room_number))
            conn.commit()
            return cursor.lastrowid
    
    def get_class(self, class_id: int) -> Optional[Class]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM classes WHERE id = ?', (class_id,))
            row = cursor.fetchone()
            if row:
                return Class(id=row[0], name=row[1], grade=row[2], 
                           teacher=row[3], room_number=row[4])
            return None
    
    def get_all_classes(self) -> List[Class]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM classes')
            return [Class(id=row[0], name=row[1], grade=row[2], 
                         teacher=row[3], room_number=row[4]) 
                   for row in cursor.fetchall()]
    
    def update_class(self, class_: Class):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE classes
                SET name = ?, grade = ?, teacher = ?, room_number = ?
                WHERE id = ?
            ''', (class_.name, class_.grade, class_.teacher, 
                  class_.room_number, class_.id))
            conn.commit()
    
    # 학생 관련 메서드
    def add_student(self, student: Student) -> int:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO students (name, student_id, birth_date, 
                                    class_id, phone, address)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (student.name, student.student_id, student.birth_date,
                  student.class_id, student.phone, student.address))
            conn.commit()
            return cursor.lastrowid
    
    def get_student(self, student_id: int) -> Optional[Student]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
            row = cursor.fetchone()
            if row:
                return Student(id=row[0], name=row[1], student_id=row[2],
                             birth_date=date.fromisoformat(row[3]),
                             class_id=row[4], phone=row[5], address=row[6])
            return None
    
    def get_students_by_class(self, class_id: int) -> List[Student]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM students WHERE class_id = ?', (class_id,))
            return [Student(id=row[0], name=row[1], student_id=row[2],
                          birth_date=date.fromisoformat(row[3]),
                          class_id=row[4], phone=row[5], address=row[6])
                   for row in cursor.fetchall()]
    
    def update_student(self, student: Student):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE students
                SET name = ?, student_id = ?, birth_date = ?, 
                    class_id = ?, phone = ?, address = ?
                WHERE id = ?
            ''', (student.name, student.student_id, student.birth_date,
                  student.class_id, student.phone, student.address,
                  student.id))
            conn.commit()
    
    # 성적 관련 메서드
    def add_grade(self, grade: Grade) -> int:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO grades (student_id, subject, score, 
                                  semester, exam_date)
                VALUES (?, ?, ?, ?, ?)
            ''', (grade.student_id, grade.subject, grade.score,
                  grade.semester, grade.exam_date))
            conn.commit()
            return cursor.lastrowid
    
    def get_grade(self, grade_id: int) -> Optional[Grade]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM grades WHERE id = ?', (grade_id,))
            row = cursor.fetchone()
            if row:
                return Grade(id=row[0], student_id=row[1], subject=row[2],
                           score=row[3], semester=row[4],
                           exam_date=date.fromisoformat(row[5]))
            return None
    
    def get_student_grades(self, student_id: int) -> List[Grade]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM grades WHERE student_id = ?', (student_id,))
            return [Grade(id=row[0], student_id=row[1], subject=row[2],
                        score=row[3], semester=row[4],
                        exam_date=date.fromisoformat(row[5]))
                   for row in cursor.fetchall()]
    
    def get_class_grades(self, class_id: int, semester: Optional[int] = None,
                        subject: Optional[str] = None) -> List[Grade]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            query = '''
                SELECT g.* FROM grades g
                JOIN students s ON g.student_id = s.id
                WHERE s.class_id = ?
            '''
            params = [class_id]
            
            if semester:
                query += ' AND g.semester = ?'
                params.append(semester)
            
            if subject:
                query += ' AND g.subject = ?'
                params.append(subject)
            
            cursor.execute(query, params)
            return [Grade(id=row[0], student_id=row[1], subject=row[2],
                        score=row[3], semester=row[4],
                        exam_date=date.fromisoformat(row[5]))
                   for row in cursor.fetchall()]
    
    def get_class_subjects(self, class_id: int) -> List[str]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT DISTINCT g.subject FROM grades g
                JOIN students s ON g.student_id = s.id
                WHERE s.class_id = ?
            ''', (class_id,))
            return [row[0] for row in cursor.fetchall()]
    
    def update_grade(self, grade: Grade):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE grades
                SET student_id = ?, subject = ?, score = ?,
                    semester = ?, exam_date = ?
                WHERE id = ?
            ''', (grade.student_id, grade.subject, grade.score,
                  grade.semester, grade.exam_date, grade.id))
            conn.commit()
    
    # 출석 관련 메서드
    def add_attendance(self, attendance: Attendance) -> int:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO attendance (student_id, date, status, reason)
                VALUES (?, ?, ?, ?)
            ''', (attendance.student_id, attendance.date,
                  attendance.status, attendance.reason))
            conn.commit()
            return cursor.lastrowid
    
    def get_attendance(self, attendance_id: int) -> Optional[Attendance]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM attendance WHERE id = ?', (attendance_id,))
            row = cursor.fetchone()
            if row:
                return Attendance(id=row[0], student_id=row[1],
                                date=date.fromisoformat(row[2]),
                                status=row[3], reason=row[4])
            return None
    
    def get_student_attendance(self, student_id: int) -> List[Attendance]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM attendance WHERE student_id = ?', (student_id,))
            return [Attendance(id=row[0], student_id=row[1],
                             date=date.fromisoformat(row[2]),
                             status=row[3], reason=row[4])
                   for row in cursor.fetchall()]
    
    def get_class_attendance(self, class_id: int, date_: date) -> List[Attendance]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT a.* FROM attendance a
                JOIN students s ON a.student_id = s.id
                WHERE s.class_id = ? AND a.date = ?
            ''', (class_id, date_))
            return [Attendance(id=row[0], student_id=row[1],
                             date=date.fromisoformat(row[2]),
                             status=row[3], reason=row[4])
                   for row in cursor.fetchall()]
    
    def update_attendance(self, attendance: Attendance):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE attendance
                SET student_id = ?, date = ?, status = ?, reason = ?
                WHERE id = ?
            ''', (attendance.student_id, attendance.date,
                  attendance.status, attendance.reason,
                  attendance.id))
            conn.commit()
    
    def __del__(self):
        """데이터베이스 연결을 종료합니다."""
        if hasattr(self, '_conn'):
            self._conn.close() 