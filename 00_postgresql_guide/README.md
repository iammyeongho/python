# MySQL 개발자를 위한 PostgreSQL 가이드

## 1. PostgreSQL 설치 및 설정

### macOS에서 설치
```bash
# Homebrew를 사용하여 PostgreSQL 14 버전 설치
brew install postgresql@14

# PostgreSQL 서비스 시작 (부팅 시 자동 시작)
brew services start postgresql@14

# PostgreSQL 서비스 상태 확인
brew services list
```

### Windows에서 설치
1. [PostgreSQL 다운로드 페이지](https://www.postgresql.org/download/windows/)에서 설치 프로그램 다운로드
2. 설치 과정에서 비밀번호 설정 (이 비밀번호는 postgres 사용자의 비밀번호가 됨)
3. 설치 완료 후 pgAdmin 4 실행 (PostgreSQL의 GUI 관리 도구)

## 2. MySQL과 PostgreSQL 주요 차이점

### 데이터 타입
| MySQL | PostgreSQL | 설명 | 주의사항 |
|-------|-----------|------|----------|
| INT | INTEGER | 정수형 | PostgreSQL에서는 INT와 INTEGER가 동일 |
| VARCHAR | VARCHAR | 가변 길이 문자열 | PostgreSQL에서는 VARCHAR(n)에서 n을 지정하지 않으면 TEXT와 동일 |
| TEXT | TEXT | 긴 텍스트 | PostgreSQL에서는 TEXT 타입이 VARCHAR보다 효율적 |
| DATETIME | TIMESTAMP | 날짜와 시간 | PostgreSQL에서는 TIMESTAMP WITH TIME ZONE도 지원 |
| BOOLEAN | BOOLEAN | 참/거짓 | PostgreSQL에서는 TRUE, FALSE, NULL 값 사용 |
| AUTO_INCREMENT | SERIAL | 자동 증가 | PostgreSQL에서는 SERIAL, BIGSERIAL, SMALLSERIAL 지원 |

### 기본 명령어 비교
| 작업 | MySQL | PostgreSQL | 설명 |
|------|-------|-----------|------|
| 데이터베이스 생성 | `CREATE DATABASE dbname;` | `CREATE DATABASE dbname;` | PostgreSQL에서는 템플릿 데이터베이스 지정 가능 |
| 데이터베이스 선택 | `USE dbname;` | `\c dbname` | PostgreSQL에서는 메타 명령어 사용 |
| 테이블 생성 | `CREATE TABLE ...` | `CREATE TABLE ...` | PostgreSQL에서는 더 많은 제약 조건 지원 |
| 사용자 생성 | `CREATE USER 'user'@'localhost';` | `CREATE USER username;` | PostgreSQL에서는 호스트 제한이 없음 |
| 권한 부여 | `GRANT ALL ON dbname.* TO 'user'@'localhost';` | `GRANT ALL ON DATABASE dbname TO username;` | PostgreSQL에서는 더 세분화된 권한 지원 |

## 3. PostgreSQL 기본 명령어

### 데이터베이스 관리
```sql
-- 데이터베이스 생성 (템플릿 지정 가능)
CREATE DATABASE dbname TEMPLATE template0;

-- 데이터베이스 목록 보기 (크기, 소유자 등 상세 정보 포함)
\l

-- 데이터베이스 선택 (현재 데이터베이스 변경)
\c dbname

-- 데이터베이스 삭제 (연결된 세션이 없어야 함)
DROP DATABASE dbname;
```

### 사용자 관리
```sql
-- 사용자 생성 (비밀번호와 함께)
CREATE USER username WITH PASSWORD 'password';

-- 사용자 비밀번호 변경
ALTER USER username WITH PASSWORD 'newpassword';

-- 사용자 목록 보기 (권한 정보 포함)
\du

-- 사용자 삭제 (소유한 객체가 없어야 함)
DROP USER username;
```

### 테이블 관리
```sql
-- 테이블 생성 (제약 조건 포함)
CREATE TABLE table_name (
    id SERIAL PRIMARY KEY,  -- 자동 증가 기본 키
    name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_name UNIQUE (name)  -- 유니크 제약 조건
);

-- 테이블 목록 보기 (스키마 정보 포함)
\dt

-- 테이블 구조 보기 (인덱스, 제약 조건 포함)
\d table_name

-- 테이블 삭제 (CASCADE 옵션으로 종속 객체도 삭제 가능)
DROP TABLE table_name CASCADE;
```

## 4. DBeaver에서 PostgreSQL 사용하기

### 연결 설정
1. 새 연결 생성 (Database > New Connection)
2. PostgreSQL 드라이버 선택
3. 연결 정보 입력:
   - Host: localhost (PostgreSQL 서버 주소)
   - Port: 5432 (기본 포트)
   - Database: (연결할 데이터베이스 이름)
   - Username: (PostgreSQL 사용자 이름)
   - Password: (사용자 비밀번호)
   - Save password: (비밀번호 저장 여부)

### 주요 기능
- SQL 편집기: SQL 쿼리 작성 및 실행
  - 구문 강조
  - 자동 완성
  - 실행 계획 보기
- 데이터 편집기: 테이블 데이터 직접 편집
  - 필터링
  - 정렬
  - 데이터 내보내기/가져오기
- 스키마 브라우저: 데이터베이스 구조 탐색
  - 테이블
  - 뷰
  - 함수
  - 트리거
- 쿼리 결과: 결과 데이터 표시 및 내보내기
  - 그리드 뷰
  - 텍스트 뷰
  - 차트 생성

## 5. Python에서 PostgreSQL 사용하기

### 필요한 패키지
```bash
# psycopg2: PostgreSQL 드라이버
pip install psycopg2-binary

# SQLAlchemy: ORM (선택적)
pip install SQLAlchemy

# 환경 변수 관리 (선택적)
pip install python-dotenv
```

### 연결 예제
```python
import psycopg2
from psycopg2 import Error

try:
    # 연결 정보 설정
    connection = psycopg2.connect(
        host="localhost",
        database="dbname",
        user="username",
        password="password"
    )
    
    # 커서 생성 (쿼리 실행을 위한 객체)
    cursor = connection.cursor()
    
    # 쿼리 실행
    cursor.execute("SELECT * FROM table_name")
    
    # 결과 가져오기
    records = cursor.fetchall()
    
    # 결과 처리
    for row in records:
        print(row)
        
except Error as e:
    print(f"PostgreSQL 오류: {e}")
    
finally:
    # 리소스 정리
    if connection:
        cursor.close()
        connection.close()
```

## 6. 일반적인 문제 해결

### 연결 오류
- PostgreSQL 서비스가 실행 중인지 확인
  ```bash
  # macOS
  brew services list
  
  # Windows
  services.msc
  ```
- 사용자 이름과 비밀번호 확인
  ```sql
  -- 사용자 목록 확인
  \du
  ```
- 데이터베이스 이름 확인
  ```sql
  -- 데이터베이스 목록 확인
  \l
  ```

### 권한 오류
- 사용자에게 적절한 권한 부여
  ```sql
  -- 데이터베이스 권한 부여
  GRANT ALL ON DATABASE dbname TO username;
  
  -- 스키마 권한 부여
  GRANT ALL ON SCHEMA public TO username;
  
  -- 테이블 권한 부여
  GRANT ALL ON ALL TABLES IN SCHEMA public TO username;
  ```
- 데이터베이스 소유자 확인
  ```sql
  -- 데이터베이스 소유자 확인
  \l
  ```

### 성능 문제
- 인덱스 생성
  ```sql
  -- 단일 컬럼 인덱스
  CREATE INDEX idx_name ON table_name (column_name);
  
  -- 복합 인덱스
  CREATE INDEX idx_name ON table_name (column1, column2);
  ```
- 쿼리 최적화
  ```sql
  -- 실행 계획 분석
  EXPLAIN ANALYZE SELECT * FROM table_name;
  ```
- EXPLAIN 명령어 사용
  ```sql
  -- 실행 계획만 보기
  EXPLAIN SELECT * FROM table_name;
  
  -- 실제 실행 시간 포함
  EXPLAIN ANALYZE SELECT * FROM table_name;
  ```

## 7. 추가 리소스
- [PostgreSQL 공식 문서](https://www.postgresql.org/docs/)
  - 튜토리얼
  - SQL 명령어 참조
  - 관리자 가이드
- [PostgreSQL 튜토리얼](https://www.postgresqltutorial.com/)
  - 초보자를 위한 가이드
  - 고급 기능 설명
  - 예제 코드
- [DBeaver 문서](https://dbeaver.com/docs/)
  - 설치 및 설정
  - 기능 설명
  - 문제 해결 