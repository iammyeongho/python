# 3. Python과 PHP의 데이터 구조 비교

이 디렉토리는 Python과 PHP의 데이터 구조를 비교하는 예제를 포함합니다.

## 주요 내용

- 배열/리스트 비교
- 연관 배열/딕셔너리 비교
- 세트 비교
- 튜플 비교
- 고급 데이터 구조 비교

## 예제 파일

- `data_structures_comparison.py`: Python의 데이터 구조 예제

## 주요 차이점

1. **배열/리스트**
   - Python: `list` 사용, 가변 크기
   - PHP: `array` 사용, 가변 크기

2. **연관 배열/딕셔너리**
   - Python: `dict` 사용
   - PHP: 연관 배열 사용

3. **세트**
   - Python: `set` 사용, 중복 불가
   - PHP: `array_unique`로 구현

4. **튜플**
   - Python: `tuple` 사용, 불변
   - PHP: `array` 사용, 가변

5. **고급 데이터 구조**
   - Python: `defaultdict`, `Counter`, `deque` 등
   - PHP: 기본 배열로 구현

## 실행 방법

```bash
python data_structures_comparison.py
```

## 필요한 패키지

- collections (Python 기본 내장)
- typing (Python 3.5+ 기본 내장) 