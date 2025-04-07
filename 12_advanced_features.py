# 고급 파이썬 기능

# 1. 메타프로그래밍
print("=== 메타프로그래밍 예제 ===")

class MetaClass(type):
    def __new__(cls, name, bases, attrs):
        # 클래스 생성 전에 속성 수정
        attrs['created_at'] = '2024-03-21'
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MetaClass):
    pass

obj = MyClass()
print(f"생성 시간: {obj.created_at}")

# 2. 디스크립터
print("\n=== 디스크립터 예제 ===")

class Validator:
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value
    
    def __get__(self, obj, objtype):
        return obj._value
    
    def __set__(self, obj, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"값은 {self.min_value} 이상이어야 합니다.")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"값은 {self.max_value} 이하여야 합니다.")
        obj._value = value

class Product:
    price = Validator(min_value=0)
    quantity = Validator(min_value=0, max_value=1000)
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

# 3. 컨텍스트 매니저 프로토콜
print("\n=== 컨텍스트 매니저 프로토콜 예제 ===")

class DatabaseConnection:
    def __init__(self, dbname):
        self.dbname = dbname
        self.connection = None
    
    def __enter__(self):
        print(f"{self.dbname} 데이터베이스에 연결합니다.")
        self.connection = "연결됨"  # 실제로는 데이터베이스 연결 코드가 들어갈 것입니다
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{self.dbname} 데이터베이스 연결을 종료합니다.")
        self.connection = None

with DatabaseConnection("test_db") as db:
    print(f"데이터베이스 상태: {db.connection}")

# 4. 제너레이터 표현식과 제너레이터 함수
print("\n=== 제너레이터 예제 ===")

# 제너레이터 표현식
squares = (x**2 for x in range(5))
print("제너레이터 표현식:", list(squares))

# 제너레이터 함수
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("피보나치 수열:", list(fibonacci(10)))

# 5. 데코레이터 체이닝
print("\n=== 데코레이터 체이닝 예제 ===")

def bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italic(func):
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

@bold
@italic
def hello():
    return "안녕하세요!"

print(hello())

# 6. 프로퍼티 데코레이터 고급 사용
print("\n=== 프로퍼티 데코레이터 고급 예제 ===")

class Person:
    def __init__(self, name):
        self._name = name
        self._age = 0
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("이름은 빈 문자열일 수 없습니다.")
        self._name = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("나이는 정수여야 합니다.")
        if value < 0:
            raise ValueError("나이는 음수일 수 없습니다.")
        self._age = value

# 7. 클래스 메서드와 정적 메서드
print("\n=== 클래스 메서드와 정적 메서드 예제 ===")

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)
    
    @staticmethod
    def is_valid_date(date_string):
        try:
            year, month, day = map(int, date_string.split('-'))
            return 1 <= month <= 12 and 1 <= day <= 31
        except:
            return False

# 8. 추상 베이스 클래스
print("\n=== 추상 베이스 클래스 예제 ===")

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# 9. 데이터 클래스
print("\n=== 데이터 클래스 예제 ===")

from dataclasses import dataclass, field
from typing import List

@dataclass
class Student:
    name: str
    age: int
    grades: List[float] = field(default_factory=list)
    
    def average_grade(self) -> float:
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

# 10. 타입 힌팅 고급 사용
print("\n=== 타입 힌팅 고급 예제 ===")

from typing import TypeVar, Generic, Optional, Union, Callable

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []
    
    def push(self, item: T) -> None:
        self.items.append(item)
    
    def pop(self) -> Optional[T]:
        return self.items.pop() if self.items else None

# 11. 비동기 프로그래밍 고급 기능
print("\n=== 비동기 프로그래밍 고급 예제 ===")

import asyncio
from typing import List

async def fetch_data(url: str) -> str:
    await asyncio.sleep(1)  # 실제로는 HTTP 요청이 들어갈 것입니다
    return f"데이터 from {url}"

async def process_all(urls: List[str]) -> List[str]:
    tasks = [fetch_data(url) for url in urls]
    return await asyncio.gather(*tasks)

# 12. 컨텍스트 변수
print("\n=== 컨텍스트 변수 예제 ===")

from contextvars import ContextVar

request_id = ContextVar('request_id')

async def process_request():
    request_id.set('12345')
    print(f"현재 요청 ID: {request_id.get()}")
    await asyncio.sleep(1)
    print(f"요청 처리 후 ID: {request_id.get()}")

# 13. 프로토콜
print("\n=== 프로토콜 예제 ===")

from typing import Protocol, runtime_checkable

@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> None: ...

class Circle:
    def draw(self) -> None:
        print("원을 그립니다.")

class Square:
    def draw(self) -> None:
        print("사각형을 그립니다.")

def draw_shape(shape: Drawable) -> None:
    shape.draw()

# 14. 매직 메서드
print("\n=== 매직 메서드 예제 ===")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"
    
    def __len__(self):
        return 2
    
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError("Vector 인덱스는 0 또는 1이어야 합니다.") 