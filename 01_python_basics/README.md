# Python 기본 개념

이 디렉토리는 Python의 기본 개념을 학습하는 데 필요한 자료를 포함하고 있습니다.

## 학습 내용

1. **01_environment/** - 환경 설정
   - 가상환경 설정과 관리
   - 패키지 관리 (pip)
   - 의존성 관리

2. **02_syntax/** - 기본 문법
   - 변수와 상수
   - 연산자
   - 주석
   - 들여쓰기 규칙
   - 기본 함수

3. **03_data_types/** - 데이터 타입
   - 숫자 타입 (int, float)
   - 문자열 (str)
   - 리스트 (list)
   - 튜플 (tuple)
   - 딕셔너리 (dict)
   - 집합 (set)

4. **04_control_flow/** - 제어 구조
   - 조건문 (if-elif-else)
   - 반복문 (for, while)
   - break와 continue
   - 예외 처리 (try-except)

## PHP 개발자를 위한 참고사항

1. **변수 선언**
   - PHP: `$variable = value;`
   - Python: `variable = value`

2. **문자열 처리**
   - PHP: `"문자열"` 또는 `'문자열'`
   - Python: `"문자열"` 또는 `'문자열'` (동일하게 사용)

3. **배열 vs 리스트/딕셔너리**
   - PHP: `$array = [1, 2, 3];`
   - Python: `list = [1, 2, 3]` 또는 `dict = {'key': 'value'}`

4. **제어 구조**
   - PHP: `if ($condition) { ... }`
   - Python: `if condition:` (들여쓰기 사용)

## 학습 순서

1. 환경 설정 (01_environment)을 먼저 학습하여 개발 환경을 준비
2. 기본 문법 (02_syntax)을 통해 Python의 기본적인 규칙을 이해
3. 데이터 타입 (03_data_types)을 학습하여 Python의 데이터 구조를 이해
4. 제어 구조 (04_control_flow)를 통해 프로그램의 흐름을 제어하는 방법을 학습

## 예제 실행 방법

각 디렉토리의 예제 파일은 독립적으로 실행 가능합니다:

```bash
python 01_environment/virtualenv_guide.py
python 02_syntax/basic_syntax.py
python 03_data_types/data_types.py
python 04_control_flow/control_flow.py
``` 