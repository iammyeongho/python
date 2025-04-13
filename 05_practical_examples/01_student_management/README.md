# 학생 관리 시스템

## 프로젝트 개요
이 프로젝트는 Python과 Flask를 사용한 간단한 학생 관리 시스템입니다. 기본적인 CRUD(Create, Read, Update, Delete) 기능을 구현했습니다.

## 기능
- 학생 정보 조회
- 학생 정보 추가
- 학생 정보 수정
- 학생 정보 삭제

## 데이터베이스 설정 (DBeaver)

### 1. 데이터베이스 연결 설정
1. DBeaver를 실행하고 새 연결을 생성합니다.
2. PostgreSQL 드라이버를 선택합니다.
3. 연결 정보를 입력합니다:
   - Host: localhost
   - Port: 5432
   - Database: student_management
   - Username: postgres
   - Password: (설정한 비밀번호)

### 2. 데이터베이스 생성
```sql
CREATE DATABASE student_management;
```

### 3. 테이블 생성
프로젝트를 실행하면 자동으로 테이블이 생성됩니다. 또는 다음 SQL을 실행할 수 있습니다:

```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    student_id VARCHAR(20) UNIQUE NOT NULL,
    grade INTEGER NOT NULL,
    major VARCHAR(100) NOT NULL,
    birth_date DATE NOT NULL
);
```

## 실행 방법

### 1. 가상환경 설정
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 또는
.\venv\Scripts\activate  # Windows
```

### 2. 필요한 패키지 설치
```bash
pip install -r requirements.txt
```

### 3. 데이터베이스 설정
1. PostgreSQL이 설치되어 있는지 확인
2. 데이터베이스와 테이블이 생성되어 있는지 확인
3. `database.py`에서 데이터베이스 연결 정보를 수정

### 4. 애플리케이션 실행
```bash
python main.py
```

## 프로젝트 구조
```
student_management/
├── main.py          # 메인 애플리케이션
├── database.py      # 데이터베이스 연결 및 설정
├── models.py        # 데이터 모델
├── templates/       # HTML 템플릿
│   ├── base.html
│   ├── student_list.html
│   └── student_form.html
└── README.md        # 프로젝트 설명
```

## API 엔드포인트
- GET /students - 학생 목록 조회
- GET /students/add - 학생 추가 폼
- POST /students/add - 학생 추가
- GET /students/<id> - 학생 상세 정보
- GET /students/<id>/edit - 학생 수정 폼
- POST /students/<id>/edit - 학생 수정
- POST /students/<id>/delete - 학생 삭제

## 주의사항
- 데이터베이스 연결 정보는 보안을 위해 환경 변수로 관리하는 것이 좋습니다.
- 프로덕션 환경에서는 적절한 보안 설정이 필요합니다.

## 추가 학습 자료

1. [SQLite 공식 문서](https://www.sqlite.org/docs.html)
2. [Python sqlite3 모듈 문서](https://docs.python.org/ko/3/library/sqlite3.html)
3. [SQL 기초 튜토리얼](https://www.w3schools.com/sql/) 