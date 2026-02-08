# Python 학습 가이드 (PHP 개발자를 위한)

이 저장소는 PHP 개발자가 Python을 학습하기 위한 체계적인 가이드를 제공합니다.

## 디렉토리 구조

1. **01_python_basics/** - Python 기본 개념
   - 01_environment/ - 환경 설정
     - `01_environment_setup.py` - Python 설치, IDE 설정
     - `02_virtualenv_guide.py` - 가상환경 생성 및 관리
     - `03_package_management.py` - pip, Poetry, requirements.txt
   - 02_syntax/ - 기본 문법
     - `01_basic_syntax.py` - 변수, 타입, 연산자
     - `02_data_structures.py` - 리스트, 딕셔너리, 집합, 튜플
     - `03_control_structures.py` - if, for, while, match
     - `04_functions.py` - 함수, *args, **kwargs, 람다
     - `05_file_handling.py` - 파일 읽기/쓰기, CSV, JSON
     - `06_error_handling.py` - try-except, 커스텀 예외
     - `07_debugging.py` - pdb, 로깅, 프로파일링
     - `08_modules_packages.py` - 모듈 임포트, 패키지 구조
     - `09_useful_libraries.py` - os, datetime, json, re 등
     - `10_regular_expressions.py` - 정규표현식

2. **02_python_advanced/** - Python 고급 개념
   - 01_oop/ - 객체지향 프로그래밍
     - `01_basic_oop.py` - 클래스, 인스턴스, 메서드
     - `02_encapsulation.py` - 캡슐화, property
     - `03_inheritance.py` - 상속, super(), MRO
     - `04_polymorphism.py` - 다형성, 덕 타이핑
     - `05_magic_methods.py` - __init__, __str__, 연산자 오버로딩
     - `06_decorators.py` - 데코레이터 패턴
     - `07_design_patterns.py` - 싱글톤, 팩토리, 옵저버
     - `08_solid_principles.py` - SOLID 원칙
   - 02_functional/ - 함수형 프로그래밍
     - `01_basic_fp.py` - 일급 함수, 순수 함수
     - `02_higher_order.py` - map, filter, reduce
     - `03_decorators.py` - 함수형 데코레이터
     - `04_generators.py` - yield, 지연 평가
     - `05_iterators.py` - 이터레이터 프로토콜
     - `06_lambda.py` - 람다 함수
     - `07_recursion.py` - 재귀, 꼬리 재귀
     - `08_functools.py` - partial, lru_cache, wraps
   - 03_concurrency/ - 동시성
     - `01_threading.py` - 스레드, Lock
     - `02_multiprocessing.py` - 프로세스, Pool
     - `03_asyncio.py` - 이벤트 루프
     - `04_concurrent_futures.py` - ThreadPoolExecutor
   - 04_async/ - 비동기 프로그래밍
     - `01_basic_async.py` ~ `08_advanced_async.py` - async/await 심화
   - 05_error_handling/ - 에러 처리 심화
     - `01_basic_errors.py` ~ `08_best_practices.py` - 예외 처리 패턴

3. **03_web_development/** - 웹 개발
   - 01_frameworks/ - 웹 프레임워크
     - `01_web_frameworks.py` - 프레임워크 비교
     - `02_django_example.py` - Django 기본
     - `03_flask_example.py` - Flask 기본
   - 02_apis/ - API 개발
     - `01_basic_api.py` - FastAPI 기본
     - `02_database.py` - SQLAlchemy 연동
     - `03_auth.py` - JWT 인증
     - `04_dependencies.py` - 의존성 주입
   - 03_database/ - 데이터베이스
     - `01_sqlalchemy_example.py` - SQLAlchemy ORM
     - `02_django_orm_example.py` - Django ORM
     - `03_postgresql_basics.py` - PostgreSQL

4. **04_testing/** - 테스트
   - 01_unit_tests/ - 단위 테스트
     - `01_unittest_example.py` - unittest 모듈
     - `02_pytest_example.py` - pytest 프레임워크
     - `03_mock_example.py` - Mock, Patch
   - 02_integration_tests/ - 통합 테스트
     - `01_database_test.py` - DB 테스트
     - `02_api_test.py` - API 테스트
     - `03_web_test.py` - 웹 앱 테스트
   - 03_functional_tests/ - 기능 테스트
     - `01_selenium_test.py` - Selenium
     - `02_playwright_test.py` - Playwright
   - 04_performance_tests/ - 성능 테스트
     - `01_basic_performance.py` - 성능 측정
     - `02_load_testing.py` - 부하 테스트

5. **05_practical_examples/** - 실전 예제
   - 01_student_management/ - 학생 관리 시스템 (Flask, SQLite)
   - 02_task_manager/ - 작업 관리 시스템
   - 03_blog_system/ - 블로그 시스템
   - 04_e_commerce/ - e-커머스 시스템

6. **06_php_comparison/** - PHP와 비교
   - `00_php_developer_guide.md` - PHP→Python 전환 가이드
   - 01_package_management/ - Composer vs pip 비교
   - 02_type_system/ - PHP 타입 vs Python 타입
   - 03_data_structures/ - 배열 vs 리스트/딕셔너리

7. **07_type_hinting/** - 타입 힌팅 심화
   - `01_basic_types.py` - 기본 타입, Optional, Union
   - `02_advanced_types.py` - Generic, Protocol, TypeVar
   - `03_pydantic_validation.py` - Pydantic 데이터 검증
   - `04_mypy_usage.py` - mypy 정적 타입 체크

8. **08_docker_deployment/** - Docker & 배포
   - `01_dockerfile_basics.py` - Dockerfile 작성법
   - `02_docker_compose.py` - 멀티 컨테이너 관리
   - `03_cicd_pipeline.py` - GitHub Actions, GitLab CI

9. **09_data_science/** - 데이터 과학 기초
   - `01_numpy_basics.py` - NumPy 배열 연산, 선형대수
   - `02_pandas_basics.py` - Pandas DataFrame, 데이터 분석
   - `03_matplotlib_visualization.py` - 데이터 시각화

10. **10_cloud_infrastructure/** - 클라우드 & 인프라
    - `01_aws_boto3.py` - AWS S3, DynamoDB, SQS, Lambda
    - `02_celery_redis.py` - 분산 작업 큐, 캐싱

11. **11_api_advanced/** - API 심화
    - `01_graphql.py` - Strawberry GraphQL

12. **12_security/** - 보안
    - `01_security_best_practices.py` - SQL Injection, XSS, CSRF 방지

13. **codingtest/** - 코딩 테스트 & 알고리즘
    - `01_data_structures.py` - 스택, 큐, 힙, 해시맵, 트리, 그래프
    - `02_sorting_algorithms.py` - 버블, 선택, 삽입, 병합, 퀵, 힙 정렬
    - `03_search_algorithms.py` - 이진탐색, DFS, BFS
    - `04_dynamic_programming.py` - DP 기초, 배낭문제, LCS, LIS
    - `05_backtracking.py` - 순열, 조합, N-Queens
    - `06_graph_algorithms.py` - 다익스트라, 플로이드, MST, 위상정렬

14. **fastapi_project/** - FastAPI 실무 프로젝트
    - app/main.py - 앱 진입점
    - app/config.py - 환경 설정
    - app/database.py - DB 연결
    - app/dependencies.py - 의존성 주입
    - app/models/ - SQLAlchemy 모델 (user.py)
    - app/schemas/ - Pydantic 스키마 (user.py, token.py)
    - app/routers/ - API 라우터 (auth.py, users.py)
    - app/services/ - 비즈니스 로직 (auth_service.py, user_service.py)
    - app/repositories/ - DB 접근 계층 (user_repository.py)
    - app/utils/ - 유틸리티 (security.py)
    - tests/ - 테스트 코드
    - Dockerfile, docker-compose.yml - 컨테이너 설정

## 학습 순서

### 기본 과정 (필수)

1. **Python 기본 (01_python_basics)** - 1~2주
   - 환경 설정부터 시작하여 Python의 기본 문법과 개념을 학습
   - 데이터 타입과 제어 구조를 이해

2. **Python 고급 (02_python_advanced)** - 2~3주
   - 객체지향 프로그래밍 개념 학습
   - 함수형 프로그래밍 패턴 이해
   - 에러 처리와 비동기 프로그래밍 학습

3. **코딩 테스트 (codingtest)** - 2주
   - 자료구조와 알고리즘 학습
   - 취업 준비에 필수

4. **웹 개발 (03_web_development + fastapi_project)** - 3~4주
   - 웹 프레임워크 사용법 학습
   - FastAPI 실무 프로젝트로 실전 경험

5. **테스트 & 배포 (04_testing + 08_docker_deployment)** - 1~2주
   - 단위 테스트 작성법 학습
   - Docker와 CI/CD 파이프라인 이해

### 심화 과정 (선택)

6. **타입 힌팅 (07_type_hinting)**
   - Pydantic, mypy를 활용한 타입 안전성

7. **데이터 과학 (09_data_science)**
   - NumPy, Pandas, Matplotlib 기초

8. **클라우드 (10_cloud_infrastructure)**
   - AWS 서비스 연동, Celery 작업 큐

9. **보안 (12_security)**
   - OWASP Top 10 방어 기법

10. **PHP 비교 (06_php_comparison)**
    - 필요에 따라 PHP와의 차이점을 비교하며 학습

## 시작하기

1. 가상환경 설정:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 또는
.\venv\Scripts\activate  # Windows
```

2. 필요한 패키지 설치:
```bash
pip install -r requirements.txt
```

3. 각 섹션의 README.md 파일을 참고하여 순서대로 학습

## FastAPI 프로젝트 실행

```bash
cd fastapi_project
pip install -r requirements.txt
uvicorn app.main:app --reload

# API 문서: http://localhost:8000/docs
```
