# 학생 관리 시스템

이 프로젝트는 Python과 SQLite를 사용한 간단한 학생 관리 시스템입니다.

## 설치 방법

1. 필요한 패키지 설치:
```bash
pip install sqlite3
```

2. 프로그램 실행:
```bash
python main.py
```

## 프로젝트 구조

```
student_management/
├── README.md           # 프로젝트 설명 문서
├── main.py            # 메인 프로그램 파일
├── database.py        # 데이터베이스 연결 및 쿼리 관리
└── models.py          # 데이터 모델 정의
```

## 주요 기능

1. **학생 관리**
   - 학생 등록
   - 학생 정보 조회
   - 학생 정보 수정
   - 학생 삭제

2. **데이터베이스 작업**
   - SQLite 데이터베이스 사용
   - 테이블 생성 및 관리
   - CRUD 작업 구현

## 데이터베이스 구조

### students 테이블
```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT,
    major TEXT
);
```

## 사용 방법

1. **학생 등록**
   - 이름, 나이, 학년, 전공 정보 입력
   - 데이터베이스에 자동 저장

2. **학생 조회**
   - 전체 학생 목록 조회
   - ID로 특정 학생 조회

3. **학생 정보 수정**
   - ID로 학생 선택
   - 수정할 정보 입력

4. **학생 삭제**
   - ID로 학생 선택
   - 확인 후 삭제

## SQLite 데이터베이스 기초

1. **데이터베이스 연결**
   ```python
   import sqlite3
   conn = sqlite3.connect('database.db')
   ```

2. **테이블 생성**
   ```python
   cursor = conn.cursor()
   cursor.execute('''
       CREATE TABLE IF NOT EXISTS students (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           name TEXT NOT NULL,
           age INTEGER,
           grade TEXT,
           major TEXT
       )
   ''')
   ```

3. **데이터 삽입**
   ```python
   cursor.execute('''
       INSERT INTO students (name, age, grade, major)
       VALUES (?, ?, ?, ?)
   ''', (name, age, grade, major))
   ```

4. **데이터 조회**
   ```python
   cursor.execute('SELECT * FROM students')
   students = cursor.fetchall()
   ```

5. **데이터 수정**
   ```python
   cursor.execute('''
       UPDATE students
       SET name = ?, age = ?, grade = ?, major = ?
       WHERE id = ?
   ''', (name, age, grade, major, student_id))
   ```

6. **데이터 삭제**
   ```python
   cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
   ```

## 주의사항

1. **데이터베이스 연결 관리**
   - 작업 완료 후 반드시 연결 종료
   - `conn.close()` 사용

2. **트랜잭션 관리**
   - 데이터 변경 시 `conn.commit()` 호출
   - 오류 발생 시 `conn.rollback()` 사용

3. **SQL 인젝션 방지**
   - 파라미터화된 쿼리 사용
   - 사용자 입력 데이터 검증

## 추가 학습 자료

1. [SQLite 공식 문서](https://www.sqlite.org/docs.html)
2. [Python sqlite3 모듈 문서](https://docs.python.org/ko/3/library/sqlite3.html)
3. [SQL 기초 튜토리얼](https://www.w3schools.com/sql/) 