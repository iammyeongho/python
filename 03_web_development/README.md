# Python 웹 개발

이 디렉토리는 Python을 사용한 웹 개발을 학습하는 데 필요한 자료를 포함하고 있습니다.

## 학습 내용

1. **01_frameworks/** - 웹 프레임워크
   - Flask
     - 라우팅
     - 템플릿 엔진
     - 요청/응답 처리
     - 미들웨어
   - Django
     - MTV 패턴
     - 관리자 인터페이스
     - 폼 처리
     - 인증 시스템

2. **02_apis/** - API 개발
   - FastAPI
     - OpenAPI 문서화
     - 의존성 주입
     - 백그라운드 태스크
     - 웹소켓
   - RESTful API 설계
     - 리소스 모델링
     - HTTP 메서드
     - 상태 코드
     - 버전 관리

3. **03_database/** - 데이터베이스
   - SQLAlchemy
     - ORM 기본
     - 관계 정의
     - 쿼리 빌더
     - 세션 관리
   - Django ORM
     - 모델 정의
     - 마이그레이션
     - 쿼리셋
     - 트랜잭션

## PHP 개발자를 위한 참고사항

1. **웹 프레임워크**
   - PHP: Laravel, Symfony
   - Python: Flask, Django
   - 주요 차이점:
     - 라우팅 방식
     - 템플릿 엔진
     - 미들웨어 처리
     - 의존성 주입

2. **API 개발**
   - PHP: RESTful API, GraphQL
   - Python: FastAPI, Flask-RESTful
   - 주요 차이점:
     - 문서화 방식
     - 유효성 검사
     - 직렬화/역직렬화

3. **데이터베이스**
   - PHP: Eloquent, Doctrine
   - Python: SQLAlchemy, Django ORM
   - 주요 차이점:
     - 쿼리 빌더 문법
     - 관계 정의 방식
     - 마이그레이션 처리

## 학습 순서

1. 웹 프레임워크 (01_frameworks)를 통해 기본적인 웹 개발 개념을 이해
2. API 개발 (02_apis)을 통해 서버-클라이언트 통신을 학습
3. 데이터베이스 (03_database)를 통해 데이터 영속성을 학습

## 예제 실행 방법

각 프레임워크별로 실행 방법이 다릅니다:

### Flask
```bash
cd 01_frameworks/flask_example
python app.py
```

### Django
```bash
cd 01_frameworks/django_example
python manage.py runserver
```

### FastAPI
```bash
cd 02_apis/fastapi_example
uvicorn main:app --reload
```

## 주의사항

1. 각 프레임워크는 별도의 가상환경에서 실행하는 것을 권장합니다.
2. 데이터베이스 예제를 실행하기 전에 데이터베이스 서버가 실행 중이어야 합니다.
3. 일부 예제는 추가 패키지 설치가 필요할 수 있습니다. 