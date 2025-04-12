# Python 테스트

이 디렉토리는 Python의 테스트 방법을 학습하는 데 필요한 자료를 포함하고 있습니다.

## 학습 내용

1. **01_unit_tests/** - 단위 테스트
   - unittest 모듈
     - 테스트 케이스 작성
     - 테스트 픽스처
     - 어서션 메서드
     - 테스트 스위트
   - pytest
     - 픽스처
     - 파라미터화된 테스트
     - 마커
     - 플러그인

2. **02_integration_tests/** - 통합 테스트
   - 데이터베이스 테스트
     - 트랜잭션 관리
     - 테스트 데이터
     - 모킹
   - API 테스트
     - 요청/응답 검증
     - 인증/인가
     - 상태 코드
   - 웹 테스트
     - Selenium
     - Playwright
     - E2E 테스트

## PHP 개발자를 위한 참고사항

1. **단위 테스트**
   - PHP: PHPUnit
   - Python: unittest, pytest
   - 주요 차이점:
     - 테스트 구조
     - 어서션 문법
     - 테스트 픽스처

2. **통합 테스트**
   - PHP: PHPUnit + 추가 라이브러리
   - Python: pytest + 추가 라이브러리
   - 주요 차이점:
     - 테스트 실행 방식
     - 보고서 형식
     - 커버리지 측정

## 학습 순서

1. 단위 테스트 (01_unit_tests)를 통해 기본적인 테스트 방법을 학습
2. 통합 테스트 (02_integration_tests)를 통해 전체 시스템 테스트를 학습

## 예제 실행 방법

### unittest
```bash
cd 01_unit_tests/unittest_example
python -m unittest discover
```

### pytest
```bash
cd 01_unit_tests/pytest_example
pytest
```

### 통합 테스트
```bash
cd 02_integration_tests
python -m pytest
```

## 주의사항

1. 테스트를 실행하기 전에 필요한 패키지를 설치해야 합니다.
2. 데이터베이스 테스트는 별도의 테스트 데이터베이스를 사용하는 것을 권장합니다.
3. API 테스트는 실제 서버가 실행 중이어야 합니다.
4. 웹 테스트는 적절한 웹 드라이버가 설치되어 있어야 합니다.

## 테스트 커버리지 측정

pytest-cov를 사용하여 테스트 커버리지를 측정할 수 있습니다:

```bash
pytest --cov=your_package tests/
```

## 테스트 자동화

CI/CD 파이프라인에서 테스트를 자동화하는 방법:

1. GitHub Actions
2. GitLab CI/CD
3. Jenkins

각 플랫폼별 설정 파일 예제가 포함되어 있습니다. 