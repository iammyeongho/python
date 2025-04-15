"""
파이썬 객체 지향 프로그래밍: 다형성과 추상 클래스
이 파일은 다형성과 추상 클래스의 개념을 설명합니다.
"""

from abc import ABC, abstractmethod

# 1. 추상 클래스와 다형성
print("=== 추상 클래스와 다형성 ===")

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

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

# 객체 생성
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Rectangle(2, 6)
]

# 다형성 활용
for shape in shapes:
    print(f"면적: {shape.area():.2f}, 둘레: {shape.perimeter():.2f}")

# 2. 덕 타이핑 (Duck Typing)
print("\n=== 덕 타이핑 ===")

class Bird:
    def fly(self):
        return "새가 날아갑니다."

class Airplane:
    def fly(self):
        return "비행기가 날아갑니다."

class Superman:
    def fly(self):
        return "슈퍼맨이 날아갑니다."

# 덕 타이핑 활용
def make_it_fly(flying_object):
    print(flying_object.fly())

# 객체 생성
bird = Bird()
airplane = Airplane()
superman = Superman()

# 동일한 인터페이스 사용
make_it_fly(bird)
make_it_fly(airplane)
make_it_fly(superman)

# 3. 연산자 오버로딩
print("\n=== 연산자 오버로딩 ===")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# 객체 생성
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# 연산자 오버로딩 활용
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 2 = {v1 * 2}")

# 4. 메서드 오버로딩 (파이썬에서는 지원하지 않음)
print("\n=== 메서드 오버로딩 대체 방법 ===")

class Calculator:
    def add(self, *args):
        if len(args) == 2:
            return args[0] + args[1]
        elif len(args) == 3:
            return args[0] + args[1] + args[2]
        else:
            return sum(args)

# 객체 생성
calc = Calculator()

# 다양한 인자로 메서드 호출
print(f"두 수의 합: {calc.add(5, 3)}")
print(f"세 수의 합: {calc.add(5, 3, 2)}")
print(f"여러 수의 합: {calc.add(1, 2, 3, 4, 5)}")

print("\n프로그램 종료") 