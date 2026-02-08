"""
mypy - 정적 타입 검사 도구
=====================================
mypy를 사용한 정적 타입 분석 방법
"""

# pip install mypy

# =============================================================================
# 1. mypy 기본 사용법
# =============================================================================

"""
mypy 설치 및 실행:
    pip install mypy
    mypy your_file.py
    mypy your_project/

자주 사용하는 옵션:
    mypy --strict file.py           # 엄격 모드
    mypy --ignore-missing-imports   # 타입 힌트 없는 라이브러리 무시
    mypy --show-error-codes         # 에러 코드 표시
    mypy --config-file mypy.ini     # 설정 파일 사용
"""


# =============================================================================
# 2. 타입 오류 예제
# =============================================================================

def greeting(name: str) -> str:
    return f"Hello, {name}"


# 올바른 사용
result = greeting("World")  # OK

# 잘못된 사용 (mypy가 감지)
# result = greeting(123)  # error: Argument 1 to "greeting" has incompatible type "int"


def add(a: int, b: int) -> int:
    return a + b


# 올바른 사용
total = add(1, 2)  # OK

# 잘못된 사용
# total = add("1", "2")  # error: incompatible types


# =============================================================================
# 3. Optional 처리
# =============================================================================

from typing import Optional


def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)


user = find_user(1)

# mypy 경고: user가 None일 수 있음
# print(user.upper())  # error: Item "None" has no attribute "upper"

# 올바른 처리
if user is not None:
    print(user.upper())  # OK

# 또는 타입 가드 사용
if user:
    print(user.upper())  # OK


# =============================================================================
# 4. Union 타입 처리
# =============================================================================

from typing import Union


def process(value: Union[int, str]) -> str:
    # mypy는 타입 축소(narrowing)를 이해함
    if isinstance(value, int):
        return str(value * 2)  # OK: value가 int임을 앎
    else:
        return value.upper()   # OK: value가 str임을 앎


# =============================================================================
# 5. 리스트와 딕셔너리
# =============================================================================

from typing import List, Dict


def sum_list(numbers: List[int]) -> int:
    return sum(numbers)


# 올바른 사용
result = sum_list([1, 2, 3])  # OK

# 잘못된 사용
# result = sum_list([1, "2", 3])  # error: incompatible type in list


def get_config() -> Dict[str, int]:
    return {"port": 8080, "timeout": 30}


config = get_config()
port: int = config["port"]  # OK


# =============================================================================
# 6. 클래스 타입 체크
# =============================================================================

class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hi, I'm {self.name}"


def print_user_info(user: User) -> None:
    print(f"Name: {user.name}, Age: {user.age}")


user = User("Alice", 25)
print_user_info(user)  # OK

# 잘못된 타입
# print_user_info("Alice")  # error: incompatible type "str"


# =============================================================================
# 7. 타입 무시하기
# =============================================================================

# 특정 라인 무시
result = some_untyped_function()  # type: ignore

# 특정 에러만 무시
result = some_function()  # type: ignore[no-untyped-call]

# 전체 파일 무시 (파일 맨 위에)
# mypy: ignore-errors


# =============================================================================
# 8. reveal_type (디버깅용)
# =============================================================================

def example() -> None:
    x = [1, 2, 3]
    # reveal_type(x)  # mypy 실행 시 타입 출력: list[int]

    y: List[str] = []
    # reveal_type(y)  # list[str]


# =============================================================================
# 9. mypy 설정 파일 (mypy.ini)
# =============================================================================

"""
# mypy.ini 또는 setup.cfg의 [mypy] 섹션

[mypy]
python_version = 3.10
warn_return_any = True
warn_unused_ignores = True
disallow_untyped_defs = True
ignore_missing_imports = True

# 특정 모듈 설정
[mypy-tests.*]
disallow_untyped_defs = False

[mypy-third_party.*]
ignore_errors = True
"""


# =============================================================================
# 10. pyproject.toml 설정
# =============================================================================

"""
# pyproject.toml

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_ignores = true
disallow_untyped_defs = true
ignore_missing_imports = true

[[tool.mypy.overrides]]
module = "tests.*"
disallow_untyped_defs = false
"""


# =============================================================================
# 11. 자주 발생하는 에러와 해결법
# =============================================================================

"""
1. "Cannot find implementation or library stub for module"
   해결: ignore_missing_imports = True
         또는 types-xxx 패키지 설치 (예: types-requests)

2. "Function is missing a type annotation"
   해결: 함수에 타입 힌트 추가
         또는 disallow_untyped_defs = False

3. "Incompatible types in assignment"
   해결: 타입 맞추기 또는 Union 사용

4. "Item 'None' of 'Optional[X]' has no attribute 'Y'"
   해결: None 체크 추가 (if x is not None:)

5. "Argument has incompatible type"
   해결: 올바른 타입으로 변환 또는 Union 사용
"""


# =============================================================================
# 12. 스텁 파일 (.pyi)
# =============================================================================

"""
타입 힌트가 없는 라이브러리를 위한 스텁 파일:

# example.pyi
def some_function(x: int) -> str: ...

class SomeClass:
    def method(self, value: str) -> None: ...

스텁 패키지:
- types-requests
- types-PyYAML
- types-redis
- 등등... pip install types-xxx
"""


# =============================================================================
# 13. strict 모드
# =============================================================================

"""
mypy --strict는 다음을 포함:
- disallow_untyped_defs: 타입 힌트 없는 함수 금지
- disallow_untyped_calls: 타입 힌트 없는 함수 호출 금지
- disallow_any_generics: 제네릭에 Any 금지
- warn_return_any: Any 반환 경고
- strict_optional: None 체크 강제
- strict_equality: 호환 안되는 타입 비교 금지
"""


# =============================================================================
# 14. CI/CD 통합
# =============================================================================

"""
GitHub Actions 예제:

name: Type Check

on: [push, pull_request]

jobs:
  mypy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - run: pip install mypy
      - run: mypy src/

pre-commit hook:

# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.0.0
    hooks:
      - id: mypy
        additional_dependencies: [types-requests]
"""


# =============================================================================
# 15. IDE 통합
# =============================================================================

"""
VS Code:
1. Python 확장 설치
2. settings.json:
   {
     "python.analysis.typeCheckingMode": "basic",
     "python.linting.mypyEnabled": true,
     "python.linting.mypyArgs": ["--strict"]
   }

PyCharm:
1. Settings > Editor > Inspections
2. Python > Type checker compatible 활성화
3. 또는 외부 도구로 mypy 설정
"""


# =============================================================================
# 정리: mypy 사용 가이드
# =============================================================================

"""
mypy 도입 단계:

1단계: 기본 설정
   - ignore_missing_imports = True로 시작
   - 점진적으로 타입 추가

2단계: 새 코드에 타입 추가
   - 새 파일/함수에 타입 힌트 작성
   - PR 체크에 mypy 추가

3단계: 엄격화
   - disallow_untyped_defs 활성화
   - 기존 코드 점진적 수정

4단계: strict 모드
   - 프로젝트 전체 strict 적용

장점:
- 런타임 전에 버그 발견
- IDE 자동완성 향상
- 문서화 효과
- 리팩토링 안전성

PHP 대비:
- PHPStan/Psalm과 유사
- 더 엄격한 타입 체크 가능
- 정적 분석 생태계가 더 성숙
"""
