# 에러 처리

이 디렉토리는 파이썬의 에러 처리 개념을 다룹니다.

## 파일 구조

1. `01_basic_errors.py`: 기본적인 예외 처리
2. `02_custom_errors.py`: 사용자 정의 예외
3. `03_context_managers.py`: 컨텍스트 매니저와 with 문
4. `04_logging.py`: 로깅과 디버깅
5. `05_file_errors.py`: 파일 처리 관련 예외
6. `06_network_errors.py`: 네트워크 관련 예외
7. `07_database_errors.py`: 데이터베이스 관련 예외
8. `08_best_practices.py`: 에러 처리 모범 사례

각 파일은 해당 주제에 대한 예제 코드와 설명을 포함하고 있습니다.

## 주요 내용

- 예외 처리 방식 비교
- 커스텀 예외 클래스
- 에러 로깅 패턴
- 에러 전파 방식
- 에러 복구 전략

## 예제 파일

- `error_handling.py`: Python의 에러 처리 예제

## 주요 차이점

1. **예외 처리 문법**
   - Python: `try/except/else/finally`
   - PHP: `try/catch/finally`

2. **예외 계층 구조**
   - Python: 모든 예외는 `Exception` 클래스 상속
   - PHP: 모든 예외는 `Throwable` 인터페이스 구현

3. **에러 로깅**
   - Python: `logging` 모듈
   - PHP: `error_log()` 함수 또는 PSR-3 로거

4. **에러 전파**
   - Python: 명시적 예외 전파
   - PHP: 예외 자동 전파

## 실행 방법

```bash
python error_handling.py
```

## 필요한 패키지

- logging (Python 기본 라이브러리)
- traceback (Python 기본 라이브러리) 