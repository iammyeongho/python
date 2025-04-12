# 4. Python과 PHP의 에러 처리 비교

이 디렉토리는 Python과 PHP의 에러 처리 방식을 비교하는 예제를 포함합니다.

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