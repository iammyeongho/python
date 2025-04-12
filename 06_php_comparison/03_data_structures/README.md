# 3. Python과 PHP의 데이터 구조 비교

이 디렉토리는 Python과 PHP의 기본 데이터 구조를 비교하는 예제를 포함합니다.

## 주요 내용

- 리스트/배열 비교
- 딕셔너리/연관 배열 비교
- 세트/배열 비교
- 튜플/배열 비교
- 데이터 클래스/클래스 비교

## 예제 파일

- `data_structures_comparison.py`: Python의 데이터 구조 예제

## 주요 차이점

1. **리스트 vs 배열**
   - Python: `list` 타입, 가변 길이
   - PHP: `array` 타입, 숫자/연관 배열 통합

2. **딕셔너리 vs 연관 배열**
   - Python: `dict` 타입, 키-값 쌍
   - PHP: `array` 타입의 연관 배열

3. **세트 vs 배열**
   - Python: `set` 타입, 고유한 요소만 포함
   - PHP: `array_unique()` 함수로 구현

4. **튜플 vs 배열**
   - Python: `tuple` 타입, 불변
   - PHP: `array` 타입을 const로 선언

## 실행 방법

```bash
python data_structures_comparison.py
```

## 필요한 패키지

- 기본 Python 라이브러리만 사용 