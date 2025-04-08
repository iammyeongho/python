# 파이썬 함수 예제
# 작성일: 2024-04-08
# 목적: 파이썬의 함수와 관련된 다양한 기능을 설명하는 예제 코드

# 1. 기본 함수 정의와 호출
# 함수는 코드를 재사용할 수 있게 해주는 기본적인 구조입니다.
print("=== 1. 기본 함수 정의와 호출 ===")

# 기본 함수 정의
def greet(name):
    """
    사용자에게 인사를 하는 함수입니다.
    
    Args:
        name (str): 인사할 대상의 이름
    
    Returns:
        str: 인사 메시지
    """
    return f"안녕하세요, {name}님!"

# 함수 호출
print(greet("홍길동"))

# 2. 매개변수
# 함수는 다양한 방식으로 매개변수를 받을 수 있습니다.
print("\n=== 2. 매개변수 ===")

# 위치 매개변수
def add(a, b):
    """두 수를 더하는 함수"""
    return a + b

print(f"3 + 5 = {add(3, 5)}")

# 기본값 매개변수
def greet_with_title(name, title="님"):
    """이름과 호칭을 받아 인사하는 함수"""
    return f"안녕하세요, {name}{title}!"

print(greet_with_title("홍길동"))
print(greet_with_title("김철수", "선생님"))

# 키워드 매개변수
def create_profile(name, age, city):
    """사용자 프로필을 생성하는 함수"""
    return {"name": name, "age": age, "city": city}

print(create_profile(name="홍길동", age=25, city="서울"))

# 가변 매개변수 (*args)
def sum_numbers(*args):
    """여러 수의 합을 계산하는 함수"""
    return sum(args)

print(f"1 + 2 + 3 + 4 = {sum_numbers(1, 2, 3, 4)}")

# 키워드 가변 매개변수 (**kwargs)
def print_info(**kwargs):
    """키워드 매개변수를 출력하는 함수"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="홍길동", age=25, city="서울")

# 3. 반환값
# 함수는 다양한 방식으로 값을 반환할 수 있습니다.
print("\n=== 3. 반환값 ===")

# 단일 반환값
def square(x):
    """수의 제곱을 반환하는 함수"""
    return x ** 2

print(f"5의 제곱: {square(5)}")

# 다중 반환값
def get_coordinates():
    """좌표를 반환하는 함수"""
    x = 10
    y = 20
    return x, y

x, y = get_coordinates()
print(f"좌표: ({x}, {y})")

# 4. 람다 함수
# 람다 함수는 간단한 함수를 한 줄로 정의할 수 있게 해줍니다.
print("\n=== 4. 람다 함수 ===")

# 기본 람다 함수
square = lambda x: x ** 2
print(f"람다 함수로 5의 제곱 계산: {square(5)}")

# 람다 함수와 내장 함수
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(f"람다 함수로 리스트의 각 요소 제곱: {squares}")

# 5. 내부 함수
# 함수 안에 다른 함수를 정의할 수 있습니다.
print("\n=== 5. 내부 함수 ===")

def outer_function(x):
    """외부 함수"""
    def inner_function(y):
        """내부 함수"""
        return y ** 2
    
    return inner_function(x)

print(f"내부 함수를 사용한 5의 제곱: {outer_function(5)}")

# 6. 클로저
# 클로저는 내부 함수가 외부 함수의 변수를 기억하는 구조입니다.
print("\n=== 6. 클로저 ===")

def create_counter():
    """카운터를 생성하는 함수"""
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

counter = create_counter()
print(f"카운터 호출: {counter()}")
print(f"카운터 호출: {counter()}")
print(f"카운터 호출: {counter()}")

# 7. 데코레이터
# 데코레이터는 함수를 수정하지 않고 기능을 추가할 수 있게 해줍니다.
print("\n=== 7. 데코레이터 ===")

def timer(func):
    """함수의 실행 시간을 측정하는 데코레이터"""
    import time
    
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 함수 실행 시간: {end - start:.4f}초")
        return result
    
    return wrapper

@timer
def slow_function():
    """실행 시간이 오래 걸리는 함수"""
    import time
    time.sleep(1)
    return "완료!"

print(slow_function())

# 8. 제너레이터
# 제너레이터는 이터레이터를 생성하는 함수입니다.
print("\n=== 8. 제너레이터 ===")

def fibonacci(n):
    """피보나치 수열을 생성하는 제너레이터"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("피보나치 수열:")
for num in fibonacci(10):
    print(num, end=" ")
print()

# 9. 재귀 함수
# 재귀 함수는 자기 자신을 호출하는 함수입니다.
print("\n=== 9. 재귀 함수 ===")

def factorial(n):
    """팩토리얼을 계산하는 재귀 함수"""
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(f"5의 팩토리얼: {factorial(5)}")

# 10. 클래스 메서드
# 클래스 메서드는 클래스와 관련된 함수입니다.
print("\n=== 10. 클래스 메서드 ===")

class Calculator:
    """계산기 클래스"""
    
    @staticmethod
    def add(x, y):
        """두 수를 더하는 정적 메서드"""
        return x + y
    
    @classmethod
    def multiply(cls, x, y):
        """두 수를 곱하는 클래스 메서드"""
        return x * y

print(f"정적 메서드로 3 + 5 = {Calculator.add(3, 5)}")
print(f"클래스 메서드로 3 * 5 = {Calculator.multiply(3, 5)}")

# 11. 함수 내 예외 처리
# 함수 내에서 발생할 수 있는 예외를 처리할 수 있습니다.
print("\n=== 11. 함수 내 예외 처리 ===")

def divide(a, b):
    """두 수를 나누는 함수"""
    try:
        return a / b
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
        return None
    except TypeError:
        print("숫자만 나눌 수 있습니다.")
        return None

print(f"10 / 2 = {divide(10, 2)}")
print(f"10 / 0 = {divide(10, 0)}")
print(f"10 / '2' = {divide(10, '2')}")

# 12. 타입 힌트
# 타입 힌트는 함수의 매개변수와 반환값의 타입을 명시할 수 있게 해줍니다.
print("\n=== 12. 타입 힌트 ===")

from typing import List, Dict, Union

def process_data(numbers: List[int]) -> Dict[str, Union[int, float]]:
    """숫자 리스트를 처리하는 함수"""
    return {
        "합계": sum(numbers),
        "평균": sum(numbers) / len(numbers)
    }

result = process_data([1, 2, 3, 4, 5])
print(f"데이터 처리 결과: {result}")

print("\n프로그램 종료") 