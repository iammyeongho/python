"""
타입 힌팅 심화
=====================================
Generic, Protocol, TypeVar 등 고급 타입 사용법
"""

from typing import (
    TypeVar, Generic, Protocol, Callable,
    Iterable, Iterator, Generator,
    ClassVar, overload, cast,
    TYPE_CHECKING
)
from dataclasses import dataclass

# =============================================================================
# 1. TypeVar (제네릭 타입 변수)
# =============================================================================

print("=== TypeVar ===")

# 기본 TypeVar
T = TypeVar('T')


def first(items: list[T]) -> T:
    """리스트의 첫 번째 요소 반환"""
    return items[0]


print(f"first([1, 2, 3]) = {first([1, 2, 3])}")          # int
print(f"first(['a', 'b']) = {first(['a', 'b'])}")        # str


# 제한된 TypeVar
Number = TypeVar('Number', int, float)


def add_numbers(a: Number, b: Number) -> Number:
    """숫자 더하기"""
    return a + b


print(f"add_numbers(1, 2) = {add_numbers(1, 2)}")
print(f"add_numbers(1.5, 2.5) = {add_numbers(1.5, 2.5)}")


# bound를 사용한 TypeVar
class Comparable:
    def __lt__(self, other: 'Comparable') -> bool:
        raise NotImplementedError


CT = TypeVar('CT', bound=Comparable)


def find_min(items: list[CT]) -> CT:
    """최솟값 찾기"""
    return min(items)


# =============================================================================
# 2. Generic 클래스
# =============================================================================

print("\n=== Generic 클래스 ===")

T = TypeVar('T')


class Stack(Generic[T]):
    """제네릭 스택 구현"""

    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def peek(self) -> T:
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0


# 사용 예제
int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)
print(f"int_stack.pop() = {int_stack.pop()}")

str_stack: Stack[str] = Stack()
str_stack.push("hello")
str_stack.push("world")
print(f"str_stack.pop() = {str_stack.pop()}")


# 여러 타입 파라미터
K = TypeVar('K')
V = TypeVar('V')


class Pair(Generic[K, V]):
    """키-값 쌍"""

    def __init__(self, key: K, value: V) -> None:
        self.key = key
        self.value = value

    def __repr__(self) -> str:
        return f"Pair({self.key}, {self.value})"


pair: Pair[str, int] = Pair("age", 25)
print(f"pair = {pair}")


# =============================================================================
# 3. Protocol (구조적 서브타이핑)
# =============================================================================

print("\n=== Protocol ===")

"""
Protocol은 덕 타이핑을 정적으로 표현
PHP의 interface와 유사하지만, 명시적 구현 선언 불필요
"""


class Drawable(Protocol):
    """그릴 수 있는 객체의 프로토콜"""

    def draw(self) -> str:
        ...


class Circle:
    """원 - Drawable 프로토콜 구현 (명시적 선언 없음)"""

    def __init__(self, radius: float):
        self.radius = radius

    def draw(self) -> str:
        return f"Circle(radius={self.radius})"


class Rectangle:
    """사각형 - Drawable 프로토콜 구현"""

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def draw(self) -> str:
        return f"Rectangle({self.width}x{self.height})"


def render(shape: Drawable) -> None:
    """Drawable 프로토콜을 구현한 객체 렌더링"""
    print(f"Rendering: {shape.draw()}")


render(Circle(5))
render(Rectangle(10, 20))


# 런타임 체크 가능한 Protocol
from typing import runtime_checkable


@runtime_checkable
class Closeable(Protocol):
    def close(self) -> None:
        ...


class FileHandle:
    def close(self) -> None:
        print("File closed")


fh = FileHandle()
print(f"isinstance(fh, Closeable) = {isinstance(fh, Closeable)}")


# =============================================================================
# 4. Callable (호출 가능 타입)
# =============================================================================

print("\n=== Callable ===")

# 기본 Callable
def apply(func: Callable[[int], int], value: int) -> int:
    """함수를 값에 적용"""
    return func(value)


def double(x: int) -> int:
    return x * 2


print(f"apply(double, 5) = {apply(double, 5)}")


# 복잡한 Callable
Handler = Callable[[str, int], bool]


def create_handler() -> Handler:
    def handler(name: str, count: int) -> bool:
        print(f"Handling {name} x {count}")
        return True
    return handler


handler = create_handler()
handler("test", 3)


# 가변 인자 Callable
from typing import ParamSpec

P = ParamSpec('P')
R = TypeVar('R')


def logged(func: Callable[P, R]) -> Callable[P, R]:
    """로깅 데코레이터"""
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@logged
def greet(name: str) -> str:
    return f"Hello, {name}"


print(greet("World"))


# =============================================================================
# 5. Iterator와 Generator
# =============================================================================

print("\n=== Iterator와 Generator ===")


# Iterator 타입
def count_up(limit: int) -> Iterator[int]:
    """숫자 이터레이터"""
    n = 0
    while n < limit:
        yield n
        n += 1


for num in count_up(3):
    print(f"  {num}")


# Generator 타입 (더 상세한 힌트)
def fibonacci(n: int) -> Generator[int, None, None]:
    """피보나치 제너레이터"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(f"fibonacci(7) = {list(fibonacci(7))}")


# Iterable 타입
def sum_all(items: Iterable[int]) -> int:
    """이터러블의 합계"""
    return sum(items)


print(f"sum_all([1, 2, 3]) = {sum_all([1, 2, 3])}")
print(f"sum_all((4, 5, 6)) = {sum_all((4, 5, 6))}")


# =============================================================================
# 6. ClassVar (클래스 변수)
# =============================================================================

print("\n=== ClassVar ===")


class Counter:
    """인스턴스 카운터"""
    count: ClassVar[int] = 0  # 클래스 변수
    name: str                  # 인스턴스 변수

    def __init__(self, name: str) -> None:
        self.name = name
        Counter.count += 1


c1 = Counter("first")
c2 = Counter("second")
print(f"Counter.count = {Counter.count}")


# =============================================================================
# 7. overload (함수 오버로딩)
# =============================================================================

print("\n=== overload ===")


@overload
def process(value: int) -> int: ...


@overload
def process(value: str) -> str: ...


@overload
def process(value: list[int]) -> list[int]: ...


def process(value):
    """다양한 타입 처리"""
    if isinstance(value, int):
        return value * 2
    elif isinstance(value, str):
        return value.upper()
    elif isinstance(value, list):
        return [x * 2 for x in value]


print(f"process(5) = {process(5)}")
print(f"process('hello') = {process('hello')}")
print(f"process([1, 2, 3]) = {process([1, 2, 3])}")


# =============================================================================
# 8. cast (타입 캐스팅)
# =============================================================================

print("\n=== cast ===")


def get_value() -> object:
    return "hello"


# cast는 타입 체커에게 힌트를 줌 (런타임 영향 없음)
value = cast(str, get_value())
print(f"value.upper() = {value.upper()}")


# =============================================================================
# 9. TYPE_CHECKING (순환 import 방지)
# =============================================================================

print("\n=== TYPE_CHECKING ===")

# TYPE_CHECKING은 타입 체커가 실행될 때만 True
# 순환 import 문제를 해결할 때 유용

if TYPE_CHECKING:
    from typing import TYPE_CHECKING  # 예시

"""
# 실제 사용 예:
# file: models.py
if TYPE_CHECKING:
    from services import UserService

class User:
    def __init__(self, service: "UserService"):
        self.service = service

# file: services.py
if TYPE_CHECKING:
    from models import User

class UserService:
    def get_user(self) -> "User":
        ...
"""


# =============================================================================
# 10. dataclass와 타입 힌팅
# =============================================================================

print("\n=== dataclass와 타입 힌팅 ===")


@dataclass
class Point:
    """2D 좌표점"""
    x: float
    y: float

    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5


@dataclass
class Rectangle:
    """사각형"""
    top_left: Point
    bottom_right: Point

    def area(self) -> float:
        width = abs(self.bottom_right.x - self.top_left.x)
        height = abs(self.bottom_right.y - self.top_left.y)
        return width * height


rect = Rectangle(Point(0, 0), Point(10, 5))
print(f"Rectangle area: {rect.area()}")


# frozen dataclass (불변)
@dataclass(frozen=True)
class ImmutablePoint:
    x: float
    y: float


immutable = ImmutablePoint(1.0, 2.0)
# immutable.x = 3.0  # 에러: FrozenInstanceError


# =============================================================================
# 정리: 고급 타입 선택 가이드
# =============================================================================

"""
고급 타입 사용 가이드:

1. TypeVar
   - 제네릭 함수/클래스 작성 시
   - 입력과 출력의 타입 관계 표현

2. Generic
   - 재사용 가능한 컨테이너 클래스
   - 예: Stack[T], Queue[T]

3. Protocol
   - 덕 타이핑을 정적으로 표현
   - 명시적 상속 없이 인터페이스 정의
   - PHP의 interface와 유사

4. Callable
   - 함수를 인자로 받거나 반환할 때
   - 콜백, 핸들러 타입 정의

5. overload
   - 같은 함수명으로 다른 시그니처 지원
   - PHP의 유사한 패턴과 달리 명시적

6. cast
   - 타입 체커에게 힌트 제공
   - 런타임 변환은 없음

7. TYPE_CHECKING
   - 순환 import 문제 해결
   - 타입 체크 시에만 import
"""
