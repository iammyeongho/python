# 2. Python과 PHP의 타입 시스템 비교

이 디렉토리는 Python과 PHP의 타입 시스템을 비교하는 예제를 포함합니다.

## 주요 내용

- 타입 힌팅/타입 선언 비교
- 제네릭 타입 비교
- 유니온 타입 비교
- 옵셔널 타입 비교
- 타입 가드 비교

## 예제 파일

- `type_hinting.py`: Python의 타입 힌팅 예제

## 주요 차이점

1. **타입 힌팅 문법**
   - Python: `: type` 구문 사용
   - PHP: `: type` 구문 사용

2. **제네릭**
   - Python: `TypeVar`, `Generic` 사용
   - PHP: 제네릭 클래스/메서드 지원

3. **유니온 타입**
   - Python: `Union[Type1, Type2]`
   - PHP: `Type1|Type2`

4. **옵셔널 타입**
   - Python: `Optional[Type]`
   - PHP: `?Type`

## 실행 방법

```bash
python type_hinting.py
```

## 필요한 패키지

- typing (Python 3.5+ 기본 내장)
- dataclasses (Python 3.7+ 기본 내장) 