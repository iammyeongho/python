# 8. Python과 PHP의 테스트 방법 비교

# 테스트 프레임워크 비교 (Python vs PHP)

이 디렉토리는 Python과 PHP의 테스트 프레임워크를 비교하는 예제를 포함합니다.

## 주요 내용

- 단위 테스트 프레임워크 비교
- 테스트 작성 패턴
- 모킹과 스텁
- 테스트 커버리지
- 통합 테스트

## 예제 파일

- `test_example.py`: Python의 테스트 예제

## 주요 차이점

1. **테스트 프레임워크**
   - Python: `unittest`, `pytest`
   - PHP: `PHPUnit`

2. **테스트 구조**
   - Python: 클래스 기반 또는 함수 기반
   - PHP: 클래스 기반

3. **어서션 메서드**
   - Python: `assertEqual`, `assertTrue` 등
   - PHP: `assertEquals`, `assertTrue` 등

4. **모킹 라이브러리**
   - Python: `unittest.mock`, `pytest-mock`
   - PHP: `PHPUnit` 내장 모킹

## 실행 방법

```bash
# unittest 사용
python -m unittest test_example.py

# pytest 사용
pytest test_example.py
```

## 필요한 패키지

- unittest (Python 기본 라이브러리)
- pytest
- pytest-mock
- coverage 