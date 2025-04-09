# 파이썬 함수 예제
# 작성일: 2024-04-08
# 목적: 파이썬의 함수와 관련된 다양한 기능을 설명하는 예제 코드

# 1. 기본 함수 정의와 호출
# 함수는 코드를 재사용할 수 있게 해주는 기본적인 구조입니다.
print("=== 1. 기본 함수 정의와 호출 ===")

# 기본 함수 정의
def greet(name):
    """
    사용자에게 인사를 하는 함수
    
    Args:
        name (str): 사용자 이름
    
    Returns:
        str: 인사 메시지
    """
    return f"안녕하세요, {name}님!"

# 함수 호출
message = greet("홍길동")
print(message)  # 안녕하세요, 홍길동님!

# 2. 매개변수
# 함수에 다양한 방식으로 매개변수를 전달할 수 있습니다.
print("\n=== 2. 매개변수 ===")

# 위치 매개변수
def add(a, b):
    """
    두 숫자를 더하는 함수
    
    Args:
        a (int/float): 첫 번째 숫자
        b (int/float): 두 번째 숫자
    
    Returns:
        int/float: 두 숫자의 합
    """
    return a + b

print(f"add(3, 5): {add(3, 5)}")  # 8

# 기본값 매개변수
def greet_with_title(name, title="님"):
    """
    사용자에게 인사를 하는 함수 (호칭 지정 가능)
    
    Args:
        name (str): 사용자 이름
        title (str, optional): 호칭. 기본값은 "님"
    
    Returns:
        str: 인사 메시지
    """
    return f"안녕하세요, {name}{title}!"

print(f"greet_with_title('홍길동'): {greet_with_title('홍길동')}")  # 안녕하세요, 홍길동님!
print(f"greet_with_title('홍길동', '선생님'): {greet_with_title('홍길동', '선생님')}")  # 안녕하세요, 홍길동선생님!

# 키워드 매개변수
def create_person(name, age, city="서울", is_student=False):
    """
    사람 정보를 딕셔너리로 생성하는 함수
    
    Args:
        name (str): 이름
        age (int): 나이
        city (str, optional): 도시. 기본값은 "서울"
        is_student (bool, optional): 학생 여부. 기본값은 False
    
    Returns:
        dict: 사람 정보 딕셔너리
    """
    return {
        "name": name,
        "age": age,
        "city": city,
        "is_student": is_student
    }

# 위치 매개변수로 호출
person1 = create_person("홍길동", 25)
print(f"person1: {person1}")

# 키워드 매개변수로 호출
person2 = create_person(name="김철수", age=30, city="부산", is_student=True)
print(f"person2: {person2}")

# 가변 매개변수 (*args)
def sum_numbers(*args):
    """
    여러 숫자의 합을 계산하는 함수
    
    Args:
        *args: 숫자들
    
    Returns:
        int/float: 숫자들의 합
    """
    return sum(args)

print(f"sum_numbers(1, 2, 3): {sum_numbers(1, 2, 3)}")  # 6
print(f"sum_numbers(1, 2, 3, 4, 5): {sum_numbers(1, 2, 3, 4, 5)}")  # 15

# 키워드 가변 매개변수 (**kwargs)
def print_info(**kwargs):
    """
    키워드 매개변수로 전달된 정보를 출력하는 함수
    
    Args:
        **kwargs: 키워드 매개변수들
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="이영희", age=28, city="인천", job="교사")

# 3. 반환값
# 함수는 다양한 방식으로 값을 반환할 수 있습니다.
print("\n=== 3. 반환값 ===")

# 단일 반환값
def square(x):
    """
    숫자의 제곱을 계산하는 함수
    
    Args:
        x (int/float): 숫자
    
    Returns:
        int/float: 숫자의 제곱
    """
    return x ** 2

print(f"square(5): {square(5)}")  # 25

# 다중 반환값
def get_coordinates():
    """
    좌표를 반환하는 함수
    
    Returns:
        tuple: (x, y) 좌표
    """
    x = 10
    y = 20
    return x, y

x, y = get_coordinates()
print(f"x: {x}, y: {y}")  # x: 10, y: 20

# None 반환
def print_message(message):
    """
    메시지를 출력하는 함수
    
    Args:
        message (str): 출력할 메시지
    """
    print(message)
    # 반환값이 없으면 None이 반환됨

result = print_message("안녕하세요!")
print(f"result: {result}")  # None

# 4. 람다 함수
# 람다 함수는 간단한 함수를 한 줄로 정의할 수 있습니다.
print("\n=== 4. 람다 함수 ===")

# 기본 람다 함수
square_lambda = lambda x: x ** 2
print(f"square_lambda(5): {square_lambda(5)}")  # 25

# 여러 매개변수를 가진 람다 함수
add_lambda = lambda a, b: a + b
print(f"add_lambda(3, 5): {add_lambda(3, 5)}")  # 8

# 람다 함수를 매개변수로 사용
def apply_function(func, value):
    """
    함수를 매개변수로 받아 적용하는 함수
    
    Args:
        func (function): 적용할 함수
        value: 함수에 전달할 값
    
    Returns:
        함수의 결과값
    """
    return func(value)

print(f"apply_function(square_lambda, 5): {apply_function(square_lambda, 5)}")  # 25
print(f"apply_function(lambda x: x * 2, 5): {apply_function(lambda x: x * 2, 5)}")  # 10

# 5. 내부 함수
# 함수 안에 다른 함수를 정의할 수 있습니다.
print("\n=== 5. 내부 함수 ===")

def outer_function(x):
    """
    외부 함수
    
    Args:
        x (int/float): 숫자
    
    Returns:
        int/float: 내부 함수의 결과
    """
    def inner_function(y):
        """
        내부 함수
        
        Args:
            y (int/float): 숫자
        
        Returns:
            int/float: 숫자의 제곱
        """
        return y ** 2
    
    return inner_function(x)

print(f"outer_function(5): {outer_function(5)}")  # 25

# 클로저
def create_counter():
    """
    카운터를 생성하는 함수
    
    Returns:
        function: 카운터 함수
    """
    count = 0
    
    def counter():
        """
        카운터 함수
        
        Returns:
            int: 현재 카운트 값
        """
        nonlocal count
        count += 1
        return count
    
    return counter

counter = create_counter()
print(f"counter(): {counter()}")  # 1
print(f"counter(): {counter()}")  # 2
print(f"counter(): {counter()}")  # 3

# 6. 데코레이터
# 데코레이터는 함수를 수정하지 않고 기능을 추가할 수 있습니다.
print("\n=== 6. 데코레이터 ===")

# 기본 데코레이터
def simple_decorator(func):
    """
    간단한 데코레이터
    
    Args:
        func (function): 데코레이트할 함수
    
    Returns:
        function: 래핑된 함수
    """
    def wrapper():
        print("함수 실행 전")
        func()
        print("함수 실행 후")
    return wrapper

@simple_decorator
def say_hello():
    """
    인사를 하는 함수
    """
    print("안녕하세요!")

say_hello()

# 매개변수를 가진 데코레이터
def decorator_with_args(func):
    """
    매개변수를 가진 데코레이터
    
    Args:
        func (function): 데코레이트할 함수
    
    Returns:
        function: 래핑된 함수
    """
    def wrapper(*args, **kwargs):
        print(f"함수 실행 전: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"함수 실행 후: {func.__name__}")
        return result
    return wrapper

@decorator_with_args
def add_numbers(a, b):
    """
    두 숫자를 더하는 함수
    
    Args:
        a (int/float): 첫 번째 숫자
        b (int/float): 두 번째 숫자
    
    Returns:
        int/float: 두 숫자의 합
    """
    return a + b

print(f"add_numbers(3, 5): {add_numbers(3, 5)}")  # 8

# 7. 제너레이터
# 제너레이터는 이터레이터를 간단하게 만들 수 있습니다.
print("\n=== 7. 제너레이터 ===")

# 제너레이터 함수
def fibonacci(n):
    """
    피보나치 수열을 생성하는 제너레이터 함수
    
    Args:
        n (int): 생성할 피보나치 수의 개수
    
    Yields:
        int: 피보나치 수
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("피보나치 수열:")
for num in fibonacci(10):
    print(num, end=" ")  # 0 1 1 2 3 5 8 13 21 34
print()

# 제너레이터 표현식
squares_gen = (x**2 for x in range(5))
print(f"squares_gen: {list(squares_gen)}")  # [0, 1, 4, 9, 16]

# 8. 재귀 함수
# 재귀 함수는 자기 자신을 호출하는 함수입니다.
print("\n=== 8. 재귀 함수 ===")

# 팩토리얼 계산
def factorial(n):
    """
    팩토리얼을 계산하는 재귀 함수
    
    Args:
        n (int): 숫자
    
    Returns:
        int: n의 팩토리얼
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(f"factorial(5): {factorial(5)}")  # 120

# 피보나치 수열 계산
def fibonacci_recursive(n):
    """
    피보나치 수를 계산하는 재귀 함수
    
    Args:
        n (int): 인덱스
    
    Returns:
        int: n번째 피보나치 수
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

print(f"fibonacci_recursive(10): {fibonacci_recursive(10)}")  # 55

# 9. 클래스 메서드
# 클래스 메서드는 클래스와 관련된 함수입니다.
print("\n=== 9. 클래스 메서드 ===")

class Person:
    """
    사람 클래스
    """
    
    def __init__(self, name, age):
        """
        초기화 메서드
        
        Args:
            name (str): 이름
            age (int): 나이
        """
        self.name = name
        self.age = age
    
    def greet(self):
        """
        인사 메서드
        
        Returns:
            str: 인사 메시지
        """
        return f"안녕하세요, 저는 {self.name}이고 {self.age}살입니다."
    
    @staticmethod
    def is_adult(age):
        """
        성인 여부를 확인하는 정적 메서드
        
        Args:
            age (int): 나이
        
        Returns:
            bool: 성인 여부
        """
        return age >= 18
    
    @classmethod
    def create_anonymous(cls, age):
        """
        익명 사용자를 생성하는 클래스 메서드
        
        Args:
            age (int): 나이
        
        Returns:
            Person: 익명 사용자 객체
        """
        return cls("익명", age)

person = Person("홍길동", 25)
print(f"person.greet(): {person.greet()}")  # 안녕하세요, 저는 홍길동이고 25살입니다.
print(f"Person.is_adult(20): {Person.is_adult(20)}")  # True
print(f"Person.is_adult(15): {Person.is_adult(15)}")  # False

anonymous = Person.create_anonymous(30)
print(f"anonymous.greet(): {anonymous.greet()}")  # 안녕하세요, 저는 익명이고 30살입니다.

# 10. 함수 내 예외 처리
# 함수 내에서 예외를 처리할 수 있습니다.
print("\n=== 10. 함수 내 예외 처리 ===")

def divide(a, b):
    """
    두 숫자를 나누는 함수
    
    Args:
        a (int/float): 첫 번째 숫자
        b (int/float): 두 번째 숫자
    
    Returns:
        int/float: 두 숫자의 몫
    
    Raises:
        ZeroDivisionError: b가 0일 때
        TypeError: a나 b가 숫자가 아닐 때
    """
    try:
        return a / b
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
        return None
    except TypeError:
        print("숫자만 나눌 수 있습니다.")
        return None

print(f"divide(10, 2): {divide(10, 2)}")  # 5.0
print(f"divide(10, 0): {divide(10, 0)}")  # None
print(f"divide('10', 2): {divide('10', 2)}")  # None

# 11. 타입 힌트
# 타입 힌트는 함수의 매개변수와 반환값의 타입을 명시할 수 있습니다.
print("\n=== 11. 타입 힌트 ===")

from typing import List, Dict, Tuple, Optional, Union

def process_data(numbers: List[int]) -> Dict[str, int]:
    """
    숫자 리스트를 처리하는 함수
    
    Args:
        numbers (List[int]): 숫자 리스트
    
    Returns:
        Dict[str, int]: 처리 결과 딕셔너리
    """
    return {
        "합계": sum(numbers),
        "평균": sum(numbers) // len(numbers),
        "최대값": max(numbers),
        "최소값": min(numbers)
    }

result = process_data([1, 2, 3, 4, 5])
print(f"process_data([1, 2, 3, 4, 5]): {result}")

def find_user(user_id: int) -> Optional[Dict[str, Union[str, int]]]:
    """
    사용자를 찾는 함수
    
    Args:
        user_id (int): 사용자 ID
    
    Returns:
        Optional[Dict[str, Union[str, int]]]: 사용자 정보 또는 None
    """
    users = {
        1: {"name": "홍길동", "age": 25},
        2: {"name": "김철수", "age": 30}
    }
    return users.get(user_id)

user = find_user(1)
print(f"find_user(1): {user}")  # {'name': '홍길동', 'age': 25}
print(f"find_user(3): {find_user(3)}")  # None

print("\n프로그램 종료") 