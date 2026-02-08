"""
타입 힌팅 기초
=====================================
Python 3.5+에서 도입된 타입 힌팅의 기본 사용법
PHP 개발자를 위한 비교 포함
"""

from typing import List, Dict, Set, Tuple, Optional, Union, Any

# =============================================================================
# 1. 기본 타입 (PHP와 비교)
# =============================================================================

"""
PHP vs Python 타입 선언:

PHP:
    function greet(string $name): string {
        return "Hello, " . $name;
    }

Python:
    def greet(name: str) -> str:
        return f"Hello, {name}"
"""

# 기본 타입들
def basic_types_example():
    # 정수
    age: int = 25

    # 실수
    price: float = 19.99

    # 문자열
    name: str = "Python"

    # 불리언
    is_active: bool = True

    # 바이트
    data: bytes = b"hello"

    print(f"age: {age}, price: {price}, name: {name}")


# 함수 타입 힌팅
def add(a: int, b: int) -> int:
    """두 정수의 합"""
    return a + b


def greet(name: str) -> str:
    """인사 메시지 반환"""
    return f"Hello, {name}"


def is_even(number: int) -> bool:
    """짝수 여부 확인"""
    return number % 2 == 0


print("=== 기본 타입 ===")
print(f"add(3, 5) = {add(3, 5)}")
print(f"greet('World') = {greet('World')}")
print(f"is_even(4) = {is_even(4)}")


# =============================================================================
# 2. 컬렉션 타입
# =============================================================================

print("\n=== 컬렉션 타입 ===")

# Python 3.9+ 에서는 list, dict 등을 직접 사용 가능
# Python 3.8 이하에서는 typing 모듈 사용

# 리스트
def get_names() -> List[str]:
    return ["Alice", "Bob", "Charlie"]


# 딕셔너리
def get_scores() -> Dict[str, int]:
    return {"Alice": 95, "Bob": 87, "Charlie": 92}


# 집합
def get_unique_ids() -> Set[int]:
    return {1, 2, 3, 4, 5}


# 튜플
def get_coordinates() -> Tuple[float, float]:
    return (37.5665, 126.9780)  # 서울 좌표


# 튜플 (가변 길이)
def get_values() -> Tuple[int, ...]:
    return (1, 2, 3, 4, 5)


print(f"names: {get_names()}")
print(f"scores: {get_scores()}")
print(f"coordinates: {get_coordinates()}")


# Python 3.9+ 스타일 (권장)
def modern_types() -> list[str]:
    """Python 3.9+ 스타일"""
    return ["a", "b", "c"]


def modern_dict() -> dict[str, int]:
    """Python 3.9+ 스타일"""
    return {"key": 1}


# =============================================================================
# 3. Optional과 Union
# =============================================================================

print("\n=== Optional과 Union ===")

"""
PHP vs Python nullable:

PHP 8+:
    function find(?int $id): ?User {
        return $id ? findUser($id) : null;
    }

Python:
    def find(id: Optional[int]) -> Optional[User]:
        return find_user(id) if id else None
"""


# Optional: None이 가능한 타입
def find_user(user_id: int) -> Optional[str]:
    """사용자 찾기 (없으면 None)"""
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)


# Union: 여러 타입 중 하나
def process_input(value: Union[str, int]) -> str:
    """문자열 또는 정수 처리"""
    return str(value)


# Python 3.10+ 에서는 | 연산자 사용 가능
# def process_input(value: str | int) -> str:
#     return str(value)


print(f"find_user(1) = {find_user(1)}")
print(f"find_user(999) = {find_user(999)}")
print(f"process_input(42) = {process_input(42)}")


# =============================================================================
# 4. Any 타입
# =============================================================================

print("\n=== Any 타입 ===")

# Any: 모든 타입 허용 (타입 체크 비활성화)
def log_anything(value: Any) -> None:
    """아무 값이나 로깅"""
    print(f"Log: {value}")


log_anything(42)
log_anything("hello")
log_anything([1, 2, 3])

# 주의: Any 남용은 타입 힌팅의 이점을 줄임


# =============================================================================
# 5. None 타입
# =============================================================================

print("\n=== None 타입 ===")

# 반환값이 없는 함수
def print_message(message: str) -> None:
    """메시지 출력 (반환값 없음)"""
    print(message)


# None을 명시적으로 반환
def maybe_return() -> Optional[int]:
    """조건에 따라 None 반환"""
    import random
    if random.random() > 0.5:
        return 42
    return None


print_message("Hello!")


# =============================================================================
# 6. 타입 별칭 (Type Alias)
# =============================================================================

print("\n=== 타입 별칭 ===")

# 복잡한 타입에 이름 부여
UserId = int
Username = str
UserDict = Dict[UserId, Username]


def get_user_map() -> UserDict:
    return {1: "Alice", 2: "Bob"}


# 복잡한 타입 별칭
Coordinates = Tuple[float, float]
Path = List[Coordinates]


def calculate_distance(path: Path) -> float:
    """경로의 총 거리 계산"""
    total = 0.0
    for i in range(1, len(path)):
        x1, y1 = path[i - 1]
        x2, y2 = path[i]
        total += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return total


path: Path = [(0.0, 0.0), (3.0, 4.0), (6.0, 0.0)]
print(f"경로 거리: {calculate_distance(path):.2f}")


# Python 3.10+ TypeAlias
# from typing import TypeAlias
# UserId: TypeAlias = int


# =============================================================================
# 7. 변수 어노테이션
# =============================================================================

print("\n=== 변수 어노테이션 ===")

# 변수에 타입 힌트
name: str = "Python"
numbers: List[int] = [1, 2, 3]
config: Dict[str, Any] = {"debug": True, "port": 8080}

# 초기값 없이 타입만 선언 (나중에 할당)
user_id: int  # 나중에 할당 예정


class User:
    # 클래스 변수 어노테이션
    name: str
    age: int
    email: Optional[str] = None

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


user = User("Alice", 25)
print(f"User: {user.name}, {user.age}")


# =============================================================================
# 8. 리터럴 타입
# =============================================================================

print("\n=== 리터럴 타입 ===")

from typing import Literal

# 특정 값만 허용
def set_status(status: Literal["pending", "approved", "rejected"]) -> None:
    """상태 설정 (특정 값만 허용)"""
    print(f"Status set to: {status}")


set_status("approved")  # OK
# set_status("invalid")  # 타입 체커가 오류 감지


# 방향
Direction = Literal["north", "south", "east", "west"]


def move(direction: Direction) -> None:
    print(f"Moving {direction}")


move("north")


# =============================================================================
# 9. Final (상수)
# =============================================================================

print("\n=== Final (상수) ===")

from typing import Final

# 상수 선언 (재할당 금지)
MAX_CONNECTIONS: Final[int] = 100
API_VERSION: Final[str] = "v1"

print(f"MAX_CONNECTIONS: {MAX_CONNECTIONS}")
print(f"API_VERSION: {API_VERSION}")

# MAX_CONNECTIONS = 200  # 타입 체커가 오류 감지


# =============================================================================
# 10. PHP 개발자를 위한 비교 정리
# =============================================================================

"""
PHP vs Python 타입 힌팅 비교:

| 개념          | PHP                      | Python                    |
|--------------|--------------------------|---------------------------|
| 기본 타입     | int, float, string, bool | int, float, str, bool     |
| 배열         | array                    | List[T], Dict[K, V]       |
| nullable    | ?Type                    | Optional[Type]            |
| union       | Type1|Type2 (PHP 8+)     | Union[T1, T2] 또는 T1|T2  |
| mixed       | mixed                    | Any                       |
| void        | void                     | None                      |
| 상수        | const                    | Final[Type]               |
| 열거형       | enum (PHP 8.1+)          | Literal["a", "b"]         |

주요 차이점:
1. Python은 런타임에 타입을 강제하지 않음 (힌트일 뿐)
2. mypy 같은 도구로 정적 타입 체크 가능
3. Python 3.9+에서는 list[int] 형식 사용 가능
4. Python 3.10+에서는 X | Y 유니온 문법 사용 가능
"""
