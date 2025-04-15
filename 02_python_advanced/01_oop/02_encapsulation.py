"""
파이썬 객체 지향 프로그래밍: 캡슐화와 접근 제어
이 파일은 캡슐화와 접근 제어의 개념을 설명합니다.
"""

# 1. 기본적인 캡슐화
print("=== 기본적인 캡슐화 ===")

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

# 객체 생성
account = BankAccount("1234567890", 10000)
print(account.deposit(5000))
print(account.withdraw(3000))
print(f"현재 잔액: {account.get_balance()}원")

# 2. 프로퍼티를 사용한 캡슐화
print("\n=== 프로퍼티를 사용한 캡슐화 ===")

class Person:
    def __init__(self, name, age):
        self._name = name  # protected 변수
        self._age = age    # protected 변수
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if len(value) >= 2:
            self._name = value
        else:
            raise ValueError("이름은 2글자 이상이어야 합니다.")
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("나이는 0 이상이어야 합니다.")

# 객체 생성
person = Person("홍길동", 25)
print(f"이름: {person.name}, 나이: {person.age}")

# 프로퍼티 수정
person.name = "김철수"
person.age = 30
print(f"수정 후 - 이름: {person.name}, 나이: {person.age}")

# 3. 접근 제어자
print("\n=== 접근 제어자 ===")

class AccessExample:
    def __init__(self):
        self.public_var = "public"      # public 변수
        self._protected_var = "protected"  # protected 변수
        self.__private_var = "private"  # private 변수
    
    def public_method(self):
        return "public 메서드"
    
    def _protected_method(self):
        return "protected 메서드"
    
    def __private_method(self):
        return "private 메서드"

# 객체 생성
example = AccessExample()

# public 접근
print(example.public_var)
print(example.public_method())

# protected 접근 (컨벤션에 따라 경고)
print(example._protected_var)
print(example._protected_method())

# private 접근 (에러 발생)
try:
    print(example.__private_var)
except AttributeError as e:
    print(f"에러: {e}")

try:
    print(example.__private_method())
except AttributeError as e:
    print(f"에러: {e}")

# 4. 이름 맹글링 (Name Mangling)
print("\n=== 이름 맹글링 ===")

class NameManglingExample:
    def __init__(self):
        self.__private_var = "private"
    
    def get_private_var(self):
        return self.__private_var

# 객체 생성
example = NameManglingExample()

# private 변수에 접근하는 방법
print("올바른 방법:", example.get_private_var())
print("이름 맹글링을 통한 접근:", example._NameManglingExample__private_var)

print("\n프로그램 종료") 