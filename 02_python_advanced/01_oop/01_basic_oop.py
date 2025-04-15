"""
파이썬 객체 지향 프로그래밍: 기본 개념
이 파일은 클래스와 객체의 기본적인 개념을 설명합니다.
"""

# 1. 기본 클래스 정의
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

# 2. 객체 생성 및 사용
print("=== 기본 클래스 예제 ===")

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

# 3. 클래스 변수와 인스턴스 변수
print("\n=== 클래스 변수와 인스턴스 변수 ===")

class Counter:
    # 클래스 변수
    count = 0
    
    def __init__(self):
        # 인스턴스 변수
        self.instance_count = 0
    
    def increment(self):
        Counter.count += 1
        self.instance_count += 1

# 객체 생성
counter1 = Counter()
counter2 = Counter()

# 카운터 증가
counter1.increment()
counter2.increment()
counter2.increment()

print(f"Counter.count: {Counter.count}")
print(f"counter1.instance_count: {counter1.instance_count}")
print(f"counter2.instance_count: {counter2.instance_count}")

# 4. 메서드 오버라이딩
print("\n=== 메서드 오버라이딩 ===")

class Animal:
    def speak(self):
        return "동물 소리"

class Dog(Animal):
    def speak(self):
        return "멍멍!"

class Cat(Animal):
    def speak(self):
        return "야옹!"

# 객체 생성
dog = Dog()
cat = Cat()

print(f"강아지: {dog.speak()}")
print(f"고양이: {cat.speak()}")

print("\n프로그램 종료") 