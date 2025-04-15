"""
파이썬 객체 지향 프로그래밍: 상속과 다형성
이 파일은 상속과 다형성의 개념을 설명합니다.
"""

# 1. 기본 상속
print("=== 기본 상속 예제 ===")

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "동물 소리"
    
    def move(self):
        return f"{self.name}이(가) 움직입니다."

class Dog(Animal):
    def speak(self):
        return "멍멍!"
    
    def fetch(self):
        return f"{self.name}이(가) 공을 물어옵니다."

class Cat(Animal):
    def speak(self):
        return "야옹!"
    
    def climb(self):
        return f"{self.name}이(가) 나무를 올라갑니다."

# 객체 생성
dog = Dog("바둑이")
cat = Cat("나비")

print(dog.speak())
print(cat.speak())
print(dog.move())
print(cat.move())
print(dog.fetch())
print(cat.climb())

# 2. 다중 상속
print("\n=== 다중 상속 예제 ===")

class Flyable:
    def fly(self):
        return "날아갑니다."

class Swimmable:
    def swim(self):
        return "수영합니다."

class Duck(Animal, Flyable, Swimmable):
    def speak(self):
        return "꽥꽥!"
    
    def move(self):
        return f"{self.name}이(가) 걷고, {self.fly()} 그리고 {self.swim()}"

# 객체 생성
duck = Duck("도날드")
print(duck.speak())
print(duck.move())

# 3. 메서드 해석 순서 (MRO)
print("\n=== 메서드 해석 순서 (MRO) ===")

class A:
    def method(self):
        return "A의 메서드"

class B(A):
    def method(self):
        return "B의 메서드"

class C(A):
    def method(self):
        return "C의 메서드"

class D(B, C):
    pass

# MRO 확인
print("D 클래스의 MRO:", D.__mro__)

# 객체 생성
d = D()
print(d.method())  # B의 메서드가 호출됨

# 4. super() 함수 사용
print("\n=== super() 함수 사용 ===")

class Parent:
    def __init__(self, name):
        self.name = name
        print("Parent 초기화")
    
    def greet(self):
        return f"안녕하세요, {self.name}입니다."

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # 부모 클래스의 __init__ 호출
        self.age = age
        print("Child 초기화")
    
    def greet(self):
        parent_greet = super().greet()  # 부모 클래스의 greet 호출
        return f"{parent_greet} 나이는 {self.age}살입니다."

# 객체 생성
child = Child("홍길동", 10)
print(child.greet())

print("\n프로그램 종료") 