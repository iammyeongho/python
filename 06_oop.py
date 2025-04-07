# 클래스와 객체지향 프로그래밍

# 1. 기본 클래스 정의와 객체 생성
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"안녕하세요, 저는 {self.name}이고 {self.age}살입니다."

# 객체 생성
person1 = Person("홍길동", 25)
print(person1.introduce())

# 2. 클래스 변수와 인스턴스 변수
class Student:
    # 클래스 변수
    school = "파이썬 고등학교"
    
    def __init__(self, name, grade):
        # 인스턴스 변수
        self.name = name
        self.grade = grade
    
    def study(self):
        return f"{self.name} 학생이 {self.grade}학년에서 공부합니다."

# 클래스 변수와 인스턴스 변수 사용
student1 = Student("김철수", 2)
print(f"{student1.name}의 학교: {Student.school}")
print(student1.study())

# 3. 상속
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name}가 멍멍!"

class Cat(Animal):
    def speak(self):
        return f"{self.name}가 야옹!"

# 상속 사용
dog = Dog("멍멍이")
cat = Cat("야옹이")
print(dog.speak())
print(cat.speak())

# 4. 다중 상속
class Flyable:
    def fly(self):
        return "날아갑니다!"

class Swimmable:
    def swim(self):
        return "수영합니다!"

class Duck(Animal, Flyable, Swimmable):
    def speak(self):
        return f"{self.name}가 꽥꽥!"

# 다중 상속 사용
duck = Duck("도날드")
print(duck.speak())
print(duck.fly())
print(duck.swim())

# 5. 프로퍼티
class BankAccount:
    def __init__(self, owner, balance):
        self._owner = owner
        self._balance = balance
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("잔액은 음수일 수 없습니다.")
        self._balance = value

# 프로퍼티 사용
account = BankAccount("홍길동", 1000)
print(f"잔액: {account.balance}")
account.balance = 2000
print(f"새 잔액: {account.balance}")

# 6. 정적 메서드와 클래스 메서드
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y
    
    @classmethod
    def multiply(cls, x, y):
        return x * y

# 정적 메서드와 클래스 메서드 사용
print(MathOperations.add(5, 3))
print(MathOperations.multiply(4, 2))

# 7. 추상 클래스
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# 추상 클래스 사용
rectangle = Rectangle(5, 3)
print(f"사각형의 넓이: {rectangle.area()}")

# 8. 매직 메서드
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# 매직 메서드 사용
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p1)
print(p2)
print(p3)
print(p1 == p2) 