# FastAPI 예제 프로젝트

이 프로젝트는 FastAPI의 주요 기능들을 보여주는 예제 코드 모음입니다.

## 설치 방법

1. 필요한 패키지 설치:
```bash
pip install fastapi uvicorn sqlalchemy pydantic python-jose[cryptography] passlib[bcrypt] python-multipart
```

2. 각 예제 실행:
```bash
# 기본 API 예제
python 01_basic_api.py

# 데이터베이스 연동 예제
python 02_database.py

# 인증 예제
python 03_auth.py

# 의존성 주입 예제
python 04_dependencies.py
```

## 예제 설명

### 1. 기본 API (01_basic_api.py)
- FastAPI의 기본적인 기능들을 보여주는 예제
- RESTful API의 기본 개념 (GET, POST, PUT, DELETE)
- 경로 매개변수, 쿼리 매개변수, 요청 본문 사용법
- 응답 모델과 검증
- 예외 처리

### 2. 데이터베이스 연동 (02_database.py)
- SQLAlchemy를 사용한 데이터베이스 연동
- ORM 모델 정의
- CRUD 작업 구현
- 관계 설정 (1:N 관계)
- 데이터베이스 세션 관리

### 3. 인증 (03_auth.py)
- JWT 기반 인증 구현
- 비밀번호 해싱
- OAuth2 with Password flow
- 토큰 기반 인증
- 사용자 관리 (등록, 활성화/비활성화)

### 4. 의존성 주입 (04_dependencies.py)
- FastAPI의 의존성 주입 시스템
- 다양한 의존성 패턴
- 의존성 공유
- 테스트를 위한 의존성 오버라이드
- 비동기 의존성

## API 문서

각 서버 실행 후 다음 URL에서 API 문서를 확인할 수 있습니다:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## RESTful API와 FastAPI의 차이점

1. **타입 힌팅**
   - FastAPI는 Python의 타입 힌팅을 활용하여 자동으로 요청/응답 검증
   - RESTful API는 수동으로 검증 로직을 구현해야 함

2. **자동 문서화**
   - FastAPI는 OpenAPI (Swagger) 문서를 자동으로 생성
   - RESTful API는 별도의 문서화 작업 필요

3. **비동기 지원**
   - FastAPI는 비동기 처리를 기본적으로 지원
   - RESTful API는 동기식 처리가 기본

4. **의존성 주입**
   - FastAPI는 강력한 의존성 주입 시스템 제공
   - RESTful API는 의존성 주입을 직접 구현해야 함

5. **검증**
   - FastAPI는 Pydantic을 통한 자동 검증
   - RESTful API는 수동 검증 필요

## 추가 학습 자료

1. [FastAPI 공식 문서](https://fastapi.tiangolo.com/ko/)
2. [SQLAlchemy 문서](https://docs.sqlalchemy.org/)
3. [Pydantic 문서](https://docs.pydantic.dev/)
4. [Python-Jose 문서](https://python-jose.readthedocs.io/)
5. [Passlib 문서](https://passlib.readthedocs.io/) 