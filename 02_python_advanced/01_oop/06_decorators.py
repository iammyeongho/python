"""
파이썬 객체 지향 프로그래밍: 데코레이터와 메타클래스
이 파일은 데코레이터와 메타클래스의 개념을 설명합니다.
"""

import time
from functools import wraps

# 1. 함수 데코레이터
print("=== 함수 데코레이터 ===")

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 실행 시간: {end_time - start_time:.4f}초")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "완료!"

# 데코레이터 사용
result = slow_function()
print(f"결과: {result}")

# 2. 클래스 데코레이터
print("\n=== 클래스 데코레이터 ===")

def singleton(cls):
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class Database:
    def __init__(self):
        print("데이터베이스 연결")

# 싱글톤 패턴 확인
db1 = Database()
db2 = Database()
print(f"db1과 db2는 같은 인스턴스인가요? {db1 is db2}")

# 3. 메서드 데코레이터
print("\n=== 메서드 데코레이터 ===")

def validate_age(func):
    @wraps(func)
    def wrapper(self, age):
        if age < 0:
            raise ValueError("나이는 0보다 작을 수 없습니다.")
        return func(self, age)
    return wrapper

class Person:
    def __init__(self, name):
        self.name = name
        self._age = 0
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    @validate_age
    def age(self, value):
        self._age = value

# 데코레이터 사용
person = Person("홍길동")
try:
    person.age = -10
except ValueError as e:
    print(f"에러: {e}")

person.age = 25
print(f"{person.name}의 나이: {person.age}")

# 4. 메타클래스
print("\n=== 메타클래스 ===")

class Meta(type):
    def __new__(cls, name, bases, namespace):
        print(f"메타클래스 __new__ 호출: {name}")
        return super().__new__(cls, name, bases, namespace)
    
    def __init__(cls, name, bases, namespace):
        print(f"메타클래스 __init__ 호출: {name}")
        super().__init__(name, bases, namespace)

class MyClass(metaclass=Meta):
    def __init__(self):
        print("MyClass 인스턴스 생성")
    
    def method(self):
        print("MyClass 메서드 호출")

# 메타클래스 사용
obj = MyClass()
obj.method()

# 5. 데코레이터 팩토리
print("\n=== 데코레이터 팩토리 ===")

def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("안녕하세요!")

# 데코레이터 팩토리 사용
say_hello()

print("\n프로그램 종료") 