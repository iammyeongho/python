# Python 학습 가이드 (PHP 개발자를 위한)

이 저장소는 PHP 개발자가 Python을 학습하기 위한 체계적인 가이드를 제공합니다.

## 디렉토리 구조

1. **01_python_basics/** - Python 기본 개념
   - 01_environment/ - 환경 설정 (가상환경, 패키지 관리)
   - 02_syntax/ - 기본 문법
   - 03_data_types/ - 데이터 타입
   - 04_control_flow/ - 제어 구조

2. **02_python_advanced/** - Python 고급 개념
   - 01_oop/ - 객체지향 프로그래밍
   - 02_functional/ - 함수형 프로그래밍
   - 03_error_handling/ - 에러 처리
   - 04_async/ - 비동기 프로그래밍

3. **03_web_development/** - 웹 개발
   - 01_frameworks/ - 웹 프레임워크 (Flask, Django)
   - 02_apis/ - API 개발 (FastAPI)
   - 03_database/ - 데이터베이스 (SQLAlchemy, Django ORM)

4. **04_testing/** - 테스트
   - 01_unit_tests/ - 단위 테스트
   - 02_integration_tests/ - 통합 테스트

5. **05_practical_examples/** - 실전 예제
   - 01_student_management/ - 학생 관리 시스템
   - 02_ecommerce/ - e-commerce 예제

6. **06_php_comparison/** - PHP와 비교
   - 01_syntax_comparison/ - 문법 비교
   - 02_oop_comparison/ - OOP 비교
   - 03_web_comparison/ - 웹 개발 비교
   - 04_database_comparison/ - 데이터베이스 비교

## 학습 순서

1. Python 기본 (01_python_basics)
   - 환경 설정부터 시작하여 Python의 기본 문법과 개념을 학습
   - 데이터 타입과 제어 구조를 이해

2. Python 고급 (02_python_advanced)
   - 객체지향 프로그래밍 개념 학습
   - 함수형 프로그래밍 패턴 이해
   - 에러 처리와 비동기 프로그래밍 학습

3. 웹 개발 (03_web_development)
   - 웹 프레임워크 사용법 학습
   - API 개발 방법 이해
   - 데이터베이스 연동 방법 학습

4. 테스트 (04_testing)
   - 단위 테스트 작성법 학습
   - 통합 테스트 방법 이해

5. 실전 예제 (05_practical_examples)
   - 실제 프로젝트 예제를 통해 학습 내용 적용

6. PHP 비교 (06_php_comparison)
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