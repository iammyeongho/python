# Python 고급 개념

이 디렉토리는 Python의 고급 개념을 학습하는 데 필요한 자료를 포함하고 있습니다.

## 학습 내용

1. **01_oop/** - 객체지향 프로그래밍
   - 클래스와 객체
   - 상속과 다형성
   - 캡슐화
   - 매직 메서드
   - 추상 클래스와 인터페이스

2. **02_functional/** - 함수형 프로그래밍
   - 람다 함수
   - map, filter, reduce
   - 리스트 컴프리헨션
   - 제너레이터
   - 데코레이터

3. **03_error_handling/** - 에러 처리
   - 예외 처리 (try-except)
   - 커스텀 예외
   - 예외 계층 구조
   - 예외 전파
   - finally 블록

4. **04_async/** - 비동기 프로그래밍
   - 코루틴
   - async/await
   - 이벤트 루프
   - 비동기 컨텍스트 매니저
   - 동시성 처리

## PHP 개발자를 위한 참고사항

1. **객체지향 프로그래밍**
   - PHP: `class MyClass { private $property; public function method() {} }`
   - Python: `class MyClass: def __init__(self): self._property = None`

2. **함수형 프로그래밍**
   - PHP: `array_map()`, `array_filter()`
   - Python: `map()`, `filter()`, 리스트 컴프리헨션

3. **에러 처리**
   - PHP: `try { ... } catch (Exception $e) { ... }`
   - Python: `try: ... except Exception as e: ...`

4. **비동기 프로그래밍**
   - PHP: `async function`, `await`
   - Python: `async def`, `await`

## 학습 순서

1. 객체지향 프로그래밍 (01_oop)을 통해 Python의 OOP 패러다임을 이해
2. 함수형 프로그래밍 (02_functional)을 통해 Python의 함수형 기능을 학습
3. 에러 처리 (03_error_handling)를 통해 견고한 코드 작성법을 학습
4. 비동기 프로그래밍 (04_async)을 통해 동시성 처리를 학습

## 예제 실행 방법

각 디렉토리의 예제 파일은 독립적으로 실행 가능합니다:

```bash
python 01_oop/oop_examples.py
python 02_functional/functional_examples.py
python 03_error_handling/error_examples.py
python 04_async/async_examples.py
```

## 주의사항

1. 비동기 프로그래밍 예제는 Python 3.7 이상이 필요합니다.
2. 일부 고급 기능은 특정 Python 버전에서만 지원됩니다.
3. 예제를 실행하기 전에 필요한 패키지를 설치해야 할 수 있습니다. 