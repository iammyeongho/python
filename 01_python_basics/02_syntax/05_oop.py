# 파이썬 객체지향 프로그래밍

# 1. 클래스와 객체
print("=== 클래스와 객체 ===")

class Person:
    """사람을 나타내는 클래스"""
    
    # 클래스 변수
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        """생성자 메서드"""
        # 인스턴스 변수
        self.name = name
        self.age = age
    
    def greet(self):
        """인사 메서드"""
        return f"안녕하세요, {self.name}입니다."
    
    def get_info(self):
        """정보 반환 메서드"""
        return f"이름: {self.name}, 나이: {self.age}, 종: {self.species}"

# 객체 생성과 메서드 호출
person1 = Person("홍길동", 25)
person2 = Person("김철수", 30)

print(person1.greet())
print(person1.get_info())
print(person2.get_info())

# 2. 상속
print("\n=== 상속 ===")

class Student(Person):
    """학생을 나타내는 클래스"""
    
    def __init__(self, name, age, student_id):
        """생성자 메서드"""
        super().__init__(name, age)  # 부모 클래스의 생성자 호출
        self.student_id = student_id
    
    def study(self):
        """공부 메서드"""
        return f"{self.name}이(가) 공부합니다."
    
    def get_info(self):
        """정보 반환 메서드 (메서드 오버라이딩)"""
        return f"{super().get_info()}, 학번: {self.student_id}"

# Student 객체 생성과 메서드 호출
student = Student("이영희", 20, "2024001")
print(student.greet())  # 부모 클래스의 메서드 호출
print(student.study())  # 자식 클래스의 메서드 호출
print(student.get_info())  # 오버라이딩된 메서드 호출

# 3. 다중 상속
print("\n=== 다중 상속 ===")

class Employee:
    """직원을 나타내는 클래스"""
    
    def __init__(self, employee_id, department):
        self.employee_id = employee_id
        self.department = department
    
    def work(self):
        return f"{self.department}에서 일합니다."

class TeachingAssistant(Student, Employee):
    """조교를 나타내는 클래스"""
    
    def __init__(self, name, age, student_id, employee_id, department):
        Student.__init__(self, name, age, student_id)
        Employee.__init__(self, employee_id, department)
    
    def assist(self):
        return f"{self.name}이(가) {self.department}에서 조교 일을 합니다."

# TeachingAssistant 객체 생성과 메서드 호출
ta = TeachingAssistant("박지성", 25, "2024002", "E001", "컴퓨터공학과")
print(ta.greet())
print(ta.study())
print(ta.work())
print(ta.assist())
print(ta.get_info())

# 4. 캡슐화
print("\n=== 캡슐화 ===")

class BankAccount:
    """은행 계좌를 나타내는 클래스"""
    
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # private 변수
        self.__balance = balance  # private 변수
    
    def deposit(self, amount):
        """입금 메서드"""
        if amount > 0:
            self.__balance += amount
            return f"{amount}원이 입금되었습니다. 현재 잔액: {self.__balance}원"
        return "입금액은 0보다 커야 합니다."
    
    def withdraw(self, amount):
        """출금 메서드"""
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f"{amount}원이 출금되었습니다. 현재 잔액: {self.__balance}원"
        return "잔액이 부족하거나 출금액이 0 이하입니다."
    
    def get_balance(self):
        """잔액 조회 메서드"""
        return self.__balance

# BankAccount 객체 생성과 메서드 호출
account = BankAccount("123-456-789", 10000)
print(account.deposit(5000))
print(account.withdraw(3000))
print(f"현재 잔액: {account.get_balance()}원")

# 5. 프로퍼티
print("\n=== 프로퍼티 ===")

class Rectangle:
    """사각형을 나타내는 클래스"""
    
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        """너비 프로퍼티"""
        return self._width
    
    @width.setter
    def width(self, value):
        """너비 설정자"""
        if value > 0:
            self._width = value
        else:
            raise ValueError("너비는 0보다 커야 합니다.")
    
    @property
    def height(self):
        """높이 프로퍼티"""
        return self._height
    
    @height.setter
    def height(self, value):
        """높이 설정자"""
        if value > 0:
            self._height = value
        else:
            raise ValueError("높이는 0보다 커야 합니다.")
    
    @property
    def area(self):
        """면적 프로퍼티"""
        return self._width * self._height

# Rectangle 객체 생성과 프로퍼티 사용
rect = Rectangle(5, 3)
print(f"너비: {rect.width}, 높이: {rect.height}, 면적: {rect.area}")
rect.width = 6
print(f"너비 변경 후 면적: {rect.area}")

# 6. 정적 메서드와 클래스 메서드
print("\n=== 정적 메서드와 클래스 메서드 ===")

class MathUtils:
    """수학 유틸리티 클래스"""
    
    PI = 3.14159
    
    @staticmethod
    def square(x):
        """정적 메서드: 제곱 계산"""
        return x ** 2
    
    @classmethod
    def circle_area(cls, radius):
        """클래스 메서드: 원의 면적 계산"""
        return cls.PI * radius ** 2

# 정적 메서드와 클래스 메서드 호출
print(f"5의 제곱: {MathUtils.square(5)}")
print(f"반지름 3의 원의 면적: {MathUtils.circle_area(3)}")

# 7. 추상 클래스
print("\n=== 추상 클래스 ===")

from abc import ABC, abstractmethod

class Shape(ABC):
    """도형을 나타내는 추상 클래스"""
    
    @abstractmethod
    def area(self):
        """면적 계산 추상 메서드"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """둘레 계산 추상 메서드"""
        pass

class Circle(Shape):
    """원을 나타내는 클래스"""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """면적 계산 메서드"""
        return MathUtils.PI * self.radius ** 2
    
    def perimeter(self):
        """둘레 계산 메서드"""
        return 2 * MathUtils.PI * self.radius

# Circle 객체 생성과 메서드 호출
circle = Circle(3)
print(f"원의 면적: {circle.area():.2f}")
print(f"원의 둘레: {circle.perimeter():.2f}")

# 8. 매직 메서드
print("\n=== 매직 메서드 ===")

class Point:
    """점을 나타내는 클래스"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """문자열 표현"""
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        """상세 문자열 표현"""
        return f"Point(x={self.x}, y={self.y})"
    
    def __eq__(self, other):
        """동등성 비교"""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
    
    def __add__(self, other):
        """덧셈 연산"""
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return Point(self.x + other, self.y + other)
    
    def __len__(self):
        """길이 계산 (원점으로부터의 거리)"""
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

# Point 객체 생성과 매직 메서드 사용
p1 = Point(1, 2)
p2 = Point(3, 4)
print(f"p1: {p1}")
print(f"p2: {p2}")
print(f"p1 == p2: {p1 == p2}")
print(f"p1 + p2: {p1 + p2}")
print(f"p1 + 5: {p1 + 5}")
print(f"p1의 길이: {len(p1)}")

# 9. 믹스인
print("\n=== 믹스인 ===")

class SerializableMixin:
    """직렬화 믹스인"""
    
    def to_dict(self):
        """객체를 딕셔너리로 변환"""
        return {key: value for key, value in self.__dict__.items()}
    
    def from_dict(self, data):
        """딕셔너리에서 객체 속성 설정"""
        for key, value in data.items():
            setattr(self, key, value)

class JSONSerializableMixin:
    """JSON 직렬화 믹스인"""
    
    def to_json(self):
        """객체를 JSON 문자열로 변환"""
        import json
        return json.dumps(self.to_dict())
    
    def from_json(self, json_str):
        """JSON 문자열에서 객체 속성 설정"""
        import json
        data = json.loads(json_str)
        self.from_dict(data)

class Product(SerializableMixin, JSONSerializableMixin):
    """제품을 나타내는 클래스"""
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

# Product 객체 생성과 믹스인 메서드 사용
product = Product("노트북", 1000000, 5)
print(f"제품 정보: {product.to_dict()}")
print(f"제품 JSON: {product.to_json()}")

# 10. 메타클래스
print("\n=== 메타클래스 ===")

class Singleton(type):
    """싱글톤 메타클래스"""
    
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):
    """데이터베이스 클래스"""
    
    def __init__(self):
        print("데이터베이스 연결 초기화")
    
    def query(self, sql):
        return f"실행된 쿼리: {sql}"

# Database 객체 생성 (싱글톤 패턴)
db1 = Database()
db2 = Database()
print(f"db1과 db2는 같은 객체: {db1 is db2}")
print(db1.query("SELECT * FROM users"))

# 11. 프로토콜 (덕 타이핑)
print("\n=== 프로토콜 (덕 타이핑) ===")

class Duck:
    """오리를 나타내는 클래스"""
    
    def quack(self):
        return "꽥꽥!"
    
    def fly(self):
        return "오리가 날아갑니다."

class Person:
    """사람을 나타내는 클래스"""
    
    def quack(self):
        return "사람이 오리 소리를 냅니다."
    
    def fly(self):
        return "사람이 비행기를 타고 날아갑니다."

def make_quack_and_fly(animal):
    """오리처럼 행동하는 객체를 처리하는 함수"""
    print(animal.quack())
    print(animal.fly())

# Duck과 Person 객체 생성 및 함수 호출
duck = Duck()
person = Person()

print("오리처럼 행동하는 오리:")
make_quack_and_fly(duck)
print("\n오리처럼 행동하는 사람:")
make_quack_and_fly(person) 