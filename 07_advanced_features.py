# 고급 파이썬 기능

# 1. 데코레이터
print("=== 데코레이터 예제 ===")

# 기본 데코레이터
def timer(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 함수 실행 시간: {end - start:.4f}초")
        return result
    return wrapper

# 데코레이터 사용
@timer
def slow_function():
    import time
    time.sleep(1)
    return "완료!"

print(slow_function())

# 데코레이터 with 매개변수
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"안녕하세요, {name}님!")

greet("홍길동")

# 2. 제너레이터
print("\n=== 제너레이터 예제 ===")

# 기본 제너레이터
def number_generator(n):
    for i in range(n):
        yield i

# 제너레이터 사용
for num in number_generator(5):
    print(num, end=" ")
print()

# 제너레이터 표현식
squares = (x**2 for x in range(5))
print(list(squares))

# 3. 컨텍스트 매니저
print("\n=== 컨텍스트 매니저 예제 ===")

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# 컨텍스트 매니저 사용
with FileManager("test.txt", "w") as f:
    f.write("테스트 파일입니다.")

# 4. 메타클래스
print("\n=== 메타클래스 예제 ===")

class Singleton(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):
    def __init__(self):
        print("데이터베이스 연결 초기화")

# 싱글톤 패턴 테스트
db1 = Database()
db2 = Database()
print(f"db1 is db2: {db1 is db2}")

# 5. 프로퍼티 데코레이터
print("\n=== 프로퍼티 데코레이터 예제 ===")

class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("이름은 빈 문자열일 수 없습니다.")
        self._name = value
    
    @name.deleter
    def name(self):
        del self._name

person = Person("홍길동")
print(person.name)
person.name = "김철수"
print(person.name)

# 6. 클래스 데코레이터
print("\n=== 클래스 데코레이터 예제 ===")

def add_method(cls):
    def new_method(self):
        return "새로운 메서드입니다!"
    
    cls.new_method = new_method
    return cls

@add_method
class MyClass:
    pass

obj = MyClass()
print(obj.new_method())

# 7. 비동기 프로그래밍
print("\n=== 비동기 프로그래밍 예제 ===")

import asyncio

async def async_function():
    print("비동기 함수 시작")
    await asyncio.sleep(1)
    print("비동기 함수 완료")
    return "결과"

async def main():
    result = await async_function()
    print(f"결과: {result}")

# 비동기 함수 실행
asyncio.run(main())

# 8. 타입 힌팅
print("\n=== 타입 힌팅 예제 ===")

from typing import List, Dict, Optional, Union

def process_data(numbers: List[int]) -> Dict[str, int]:
    return {"합계": sum(numbers), "개수": len(numbers)}

def greet_person(name: str, age: Optional[int] = None) -> str:
    if age is not None:
        return f"{name}님, {age}살이시군요!"
    return f"{name}님, 안녕하세요!"

# 타입 힌팅 사용
result = process_data([1, 2, 3, 4, 5])
print(result)
print(greet_person("홍길동", 25))
print(greet_person("김철수")) 