# 파이썬 함수

# 1. 기본 함수 정의와 호출
print("=== 기본 함수 정의와 호출 ===")

def greet(name):
    """간단한 인사 함수"""
    return f"안녕하세요, {name}님!"

print(greet("홍길동"))

# 2. 매개변수
print("\n=== 매개변수 ===")

# 위치 매개변수
def add(a, b):
    return a + b

print(f"3 + 5 = {add(3, 5)}")

# 기본값 매개변수
def greet_with_title(name, title="님"):
    return f"안녕하세요, {name}{title}"

print(greet_with_title("홍길동"))
print(greet_with_title("홍길동", "선생님"))

# 키워드 매개변수
def create_profile(name, age, city):
    return {"name": name, "age": age, "city": city}

print(create_profile(name="홍길동", age=25, city="서울"))
print(create_profile(city="부산", name="김철수", age=30))

# 가변 매개변수 (*args)
def sum_numbers(*args):
    return sum(args)

print(f"1 + 2 + 3 = {sum_numbers(1, 2, 3)}")
print(f"1 + 2 + 3 + 4 + 5 = {sum_numbers(1, 2, 3, 4, 5)}")

# 키워드 가변 매개변수 (**kwargs)
def print_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_profile(name="홍길동", age=25, city="서울", job="학생")

# 3. 반환값
print("\n=== 반환값 ===")

# 단일 반환값
def square(x):
    return x ** 2

print(f"5의 제곱: {square(5)}")

# 다중 반환값
def get_coordinates():
    x = 10
    y = 20
    return x, y

x, y = get_coordinates()
print(f"좌표: ({x}, {y})")

# 4. 람다 함수
print("\n=== 람다 함수 ===")

# 기본 람다 함수
square = lambda x: x ** 2
print(f"5의 제곱 (람다): {square(5)}")

# 람다 함수와 내장 함수
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(f"제곱 리스트: {squares}")

# 5. 내부 함수
print("\n=== 내부 함수 ===")

def outer_function(x):
    def inner_function(y):
        return y * 2
    
    result = inner_function(x)
    return result

print(f"내부 함수 결과: {outer_function(5)}")

# 6. 클로저
print("\n=== 클로저 ===")

def create_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counter = create_counter()
print(f"카운터: {counter()}")
print(f"카운터: {counter()}")
print(f"카운터: {counter()}")

# 7. 데코레이터
print("\n=== 데코레이터 ===")

def timer(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"함수 {func.__name__} 실행 시간: {end - start:.4f}초")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(1)
    return "완료!"

print(slow_function())

# 8. 제너레이터 함수
print("\n=== 제너레이터 함수 ===")

def number_generator(n):
    for i in range(n):
        yield i

for num in number_generator(5):
    print(num, end=" ")
print()

# 9. 재귀 함수
print("\n=== 재귀 함수 ===")

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"5의 팩토리얼: {factorial(5)}")

# 10. 함수와 클래스
print("\n=== 함수와 클래스 ===")

class Calculator:
    def __init__(self):
        self.value = 0
    
    def add(self, x):
        self.value += x
        return self
    
    def subtract(self, x):
        self.value -= x
        return self
    
    def multiply(self, x):
        self.value *= x
        return self
    
    def divide(self, x):
        if x != 0:
            self.value /= x
        return self
    
    def get_value(self):
        return self.value

calc = Calculator()
result = calc.add(5).multiply(2).subtract(3).get_value()
print(f"계산 결과: {result}")

# 11. 함수와 예외 처리
print("\n=== 함수와 예외 처리 ===")

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다."
    except TypeError:
        return "숫자만 입력 가능합니다."

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("10", 2))

# 12. 함수와 타입 힌트
print("\n=== 함수와 타입 힌트 ===")

from typing import List, Dict, Union, Optional

def process_numbers(numbers: List[int]) -> int:
    return sum(numbers)

def create_user(name: str, age: int, city: Optional[str] = None) -> Dict[str, Union[str, int]]:
    user = {"name": name, "age": age}
    if city:
        user["city"] = city
    return user

print(f"숫자 합계: {process_numbers([1, 2, 3, 4, 5])}")
print(f"사용자 정보: {create_user('홍길동', 25, '서울')}")
print(f"사용자 정보: {create_user('김철수', 30)}") 