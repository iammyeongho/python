# 7. Python과 PHP의 데이터베이스 접근 비교

이 디렉토리는 Python과 PHP의 데이터베이스 접근 방식을 비교하는 예제들을 포함하고 있습니다.

## 주요 내용

### SQLAlchemy 예제 (`sqlalchemy_example.py`)

이 예제는 Python의 SQLAlchemy ORM을 사용하여 데이터베이스 작업을 수행하는 방법을 보여줍니다.
PHP의 Doctrine이나 Eloquent와 유사한 기능을 제공합니다.

#### 주요 특징:
- 모델 정의 (PHP의 엔티티와 유사)
- 트랜잭션 관리 (PHP의 트랜잭션과 유사)
- Repository 패턴 구현
- 관계 정의 (1:N 관계)
- CRUD 작업 예제

#### PHP와의 비교:
1. **모델 정의**
   - PHP: Doctrine의 엔티티 클래스나 Eloquent의 모델 클래스
   - Python: SQLAlchemy의 모델 클래스

2. **트랜잭션 관리**
   - PHP: `beginTransaction()`, `commit()`, `rollback()`
   - Python: 컨텍스트 매니저를 사용한 세션 스코프

3. **Repository 패턴**
   - PHP: Doctrine의 Repository 클래스나 Eloquent의 모델 메서드
   - Python: Repository 클래스와 정적 메서드

4. **관계 정의**
   - PHP: `@OneToMany`, `@ManyToOne` 등의 어노테이션
   - Python: `relationship()` 함수와 `back_populates` 파라미터

5. **쿼리 빌더**
   - PHP: Doctrine의 QueryBuilder나 Eloquent의 쿼리 빌더
   - Python: SQLAlchemy의 쿼리 인터페이스

## 실행 방법

1. 필요한 패키지 설치:
```bash
pip install sqlalchemy
```

2. 예제 실행:
```bash
python sqlalchemy_example.py
```

## 참고 사항

- SQLAlchemy는 Python에서 가장 널리 사용되는 ORM 중 하나입니다.
- PHP의 Doctrine이나 Eloquent와 마찬가지로, SQLAlchemy도 데이터베이스 스키마를 자동으로 생성하고 관리할 수 있습니다.
- 트랜잭션 관리는 컨텍스트 매니저를 사용하여 더 안전하고 간결하게 처리할 수 있습니다.
- Repository 패턴을 사용하면 비즈니스 로직과 데이터 접근 계층을 분리할 수 있습니다.

## 주요 차이점

1. **ORM 접근 방식**
   - Python: SQLAlchemy(선언적), Django ORM(액티브 레코드)
   - PHP: Eloquent(액티브 레코드), Doctrine(데이터 매퍼)

2. **쿼리 빌더**
   - Python: SQLAlchemy Core, Django QuerySet
   - PHP: Laravel Query Builder, Doctrine QueryBuilder

3. **마이그레이션**
   - Python: Alembic, Django Migrations
   - PHP: Laravel Migrations, Doctrine Migrations

4. **트랜잭션 처리**
   - Python: 컨텍스트 매니저 사용
   - PHP: 트랜잭션 메서드 체인

## 예제 파일

- `sqlalchemy_example.py`: SQLAlchemy 예제
- `django_orm_example.py`: Django ORM 예제

## 필요한 패키지

- SQLAlchemy
- Django
- alembic
- psycopg2 (PostgreSQL)
- mysqlclient (MySQL) 