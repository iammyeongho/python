# 파이썬 객체 지향 프로그래밍 예제
# 작성일: 2024-04-08
# 목적: 파이썬의 객체 지향 프로그래밍과 관련된 다양한 기능을 설명하는 예제 코드

# 1. 클래스와 객체
# 클래스를 정의하고 객체를 생성하는 기본적인 방법을 보여줍니다.
print("=== 1. 클래스와 객체 ===")

class Person:
    # 클래스 변수 (모든 인스턴스가 공유)
    species = "Homo sapiens"
    
    # 생성자 메서드
    def __init__(self, name, age):
        # 인스턴스 변수 (각 인스턴스마다 독립적)
        self.name = name
        self.age = age
    
    # 인스턴스 메서드
    def introduce(self):
        return f"안녕하세요, 저는 {self.name}이고 {self.age}살입니다."
    
    # 클래스 메서드
    @classmethod
    def create_anonymous(cls):
        return cls("익명", 0)
    
    # 정적 메서드
    @staticmethod
    def is_adult(age):
        return age >= 18

# 객체 생성
person1 = Person("홍길동", 25)
person2 = Person("김철수", 17)

# 메서드 호출
print(person1.introduce())
print(person2.introduce())

# 클래스 메서드 호출
anonymous = Person.create_anonymous()
print(anonymous.introduce())

# 정적 메서드 호출
print(f"{person1.name}은(는) 성인인가요? {Person.is_adult(person1.age)}")
print(f"{person2.name}은(는) 성인인가요? {Person.is_adult(person2.age)}")

# 2. 상속
# 클래스 상속의 기본적인 방법을 보여줍니다.
print("\n=== 2. 상속 ===")

class Student(Person):
    def __init__(self, name, age, student_id):
        # 부모 클래스의 생성자 호출
        super().__init__(name, age)
        self.student_id = student_id
    
    # 메서드 오버라이딩
    def introduce(self):
        return f"{super().introduce()} 학번은 {self.student_id}입니다."
    
    # 새로운 메서드 추가
    def study(self, subject):
        return f"{self.name}이(가) {subject}을(를) 공부합니다."

# Student 객체 생성
student = Student("이영희", 20, "2024001")
print(student.introduce())
print(student.study("파이썬"))

# 3. 다중 상속
# 여러 클래스를 상속받는 방법을 보여줍니다.
print("\n=== 3. 다중 상속 ===")

class Employee:
    def __init__(self, employee_id, department):
        self.employee_id = employee_id
        self.department = department
    
    def work(self):
        return f"{self.department}에서 일합니다."

class WorkingStudent(Student, Employee):
    def __init__(self, name, age, student_id, employee_id, department):
        # 각 부모 클래스의 생성자 호출
        Student.__init__(self, name, age, student_id)
        Employee.__init__(self, employee_id, department)
    
    def introduce(self):
        return f"{Student.introduce(self)} {Employee.work(self)}"

# WorkingStudent 객체 생성
working_student = WorkingStudent("박지성", 22, "2024002", "E001", "개발팀")
print(working_student.introduce())

# 4. 캡슐화
# 데이터와 메서드를 캡슐화하는 방법을 보여줍니다.
print("\n=== 4. 캡슐화 ===")

class BankAccount:
    def __init__(self, account_number, balance):
        # private 변수 (이름 앞에 언더스코어 2개)
        self.__account_number = account_number
        self.__balance = balance
    
    # getter 메서드
    def get_balance(self):
        return self.__balance
    
    # setter 메서드
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"{amount}원이 입금되었습니다. 현재 잔액: {self.__balance}원"
        return "입금액은 0보다 커야 합니다."
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f"{amount}원이 출금되었습니다. 현재 잔액: {self.__balance}원"
        return "출금액이 잔액보다 크거나 0보다 작습니다."

# BankAccount 객체 생성
account = BankAccount("1234567890", 10000)
print(account.deposit(5000))
print(account.withdraw(3000))
print(f"현재 잔액: {account.get_balance()}원")

# 5. 프로퍼티
# 프로퍼티를 사용하여 getter와 setter를 구현하는 방법을 보여줍니다.
print("\n=== 5. 프로퍼티 ===")

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    # width 프로퍼티
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError("너비는 0보다 커야 합니다.")
    
    # height 프로퍼티
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise ValueError("높이는 0보다 커야 합니다.")
    
    # area 프로퍼티 (읽기 전용)
    @property
    def area(self):
        return self._width * self._height

# Rectangle 객체 생성
rectangle = Rectangle(5, 10)
print(f"너비: {rectangle.width}, 높이: {rectangle.height}, 면적: {rectangle.area}")

# 프로퍼티 수정
rectangle.width = 8
print(f"너비 변경 후 - 너비: {rectangle.width}, 높이: {rectangle.height}, 면적: {rectangle.area}")

# 6. 추상 클래스
# 추상 클래스를 정의하고 사용하는 방법을 보여줍니다.
print("\n=== 6. 추상 클래스 ===")

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side

# Shape 객체 생성 (오류 발생)
# shape = Shape()  # TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter

# Circle 객체 생성
circle = Circle(5)
print(f"원의 면적: {circle.area():.2f}")
print(f"원의 둘레: {circle.perimeter():.2f}")

# Square 객체 생성
square = Square(4)
print(f"정사각형의 면적: {square.area()}")
print(f"정사각형의 둘레: {square.perimeter()}")

# 7. 매직 메서드
# 파이썬의 특수 메서드(매직 메서드)를 사용하는 방법을 보여줍니다.
print("\n=== 7. 매직 메서드 ===")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # 문자열 표현
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    # 객체 표현
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
    
    # 덧셈 연산
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    # 뺄셈 연산
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    # 곱셈 연산
    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)
    
    # 비교 연산
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        return (self.x ** 2 + self.y ** 2) < (other.x ** 2 + other.y ** 2)

# Point 객체 생성
p1 = Point(1, 2)
p2 = Point(3, 4)

# 문자열 표현
print(f"p1: {p1}")
print(f"p2: {repr(p2)}")

# 연산
p3 = p1 + p2
print(f"p1 + p2 = {p3}")

p4 = p2 - p1
print(f"p2 - p1 = {p4}")

p5 = p1 * 2
print(f"p1 * 2 = {p5}")

# 비교
print(f"p1 == p2: {p1 == p2}")
print(f"p1 < p2: {p1 < p2}")

# 8. 클래스 데코레이터
# 클래스 데코레이터를 사용하는 방법을 보여줍니다.
print("\n=== 8. 클래스 데코레이터 ===")

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
        print("데이터베이스 연결 초기화")
    
    def query(self, sql):
        return f"실행된 쿼리: {sql}"

# Database 객체 생성
db1 = Database()
db2 = Database()

# 같은 객체인지 확인
print(f"db1과 db2는 같은 객체인가요? {db1 is db2}")

# 9. 메타클래스
# 메타클래스를 사용하는 방법을 보여줍니다.
print("\n=== 9. 메타클래스 ===")

class AutoRegister(type):
    def __new__(cls, name, bases, attrs):
        # 클래스 생성 시 자동으로 등록
        print(f"클래스 '{name}'이(가) 생성되었습니다.")
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=AutoRegister):
    def __init__(self):
        print("MyClass 인스턴스가 생성되었습니다.")
    
    def my_method(self):
        return "my_method가 호출되었습니다."

# MyClass 객체 생성
my_obj = MyClass()
print(my_obj.my_method())

print("\n프로그램 종료") 