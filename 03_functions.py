# 함수와 모듈

# 1. 기본 함수 정의와 호출
def greet(name):
    return f"안녕하세요, {name}님!"

print(greet("홍길동"))

# 2. 매개변수 기본값
def greet_with_title(name, title="님"):
    return f"안녕하세요, {name}{title}"

print(greet_with_title("홍길동"))
print(greet_with_title("홍길동", "선생님"))

# 3. 여러 매개변수 받기
def sum_numbers(*args):
    return sum(args)

print(f"합계: {sum_numbers(1, 2, 3, 4, 5)}")

# 4. 키워드 매개변수
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="홍길동", age=25, city="서울")

# 5. 람다 함수
square = lambda x: x**2
print(f"5의 제곱: {square(5)}")

# 6. 함수를 매개변수로 전달
def apply_operation(func, number):
    return func(number)

def double(x):
    return x * 2

print(f"10을 두 배로: {apply_operation(double, 10)}")

# 7. 재귀 함수
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(f"5의 팩토리얼: {factorial(5)}")

# 8. 모듈 임포트 예제
import math
print(f"파이(π): {math.pi}")
print(f"5의 제곱근: {math.sqrt(25)}")

# 9. 사용자 정의 모듈 예제
# math_utils.py 파일을 만들어서 사용할 수 있습니다
"""
# math_utils.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
"""

# 10. 클로저
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