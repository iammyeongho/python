"""
파이썬 객체 지향 프로그래밍: 디자인 패턴
이 파일은 다양한 디자인 패턴의 개념을 설명합니다.
"""

from abc import ABC, abstractmethod

# 1. 팩토리 패턴
print("=== 팩토리 패턴 ===")

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "멍멍!"

class Cat(Animal):
    def speak(self):
        return "야옹!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"알 수 없는 동물 타입: {animal_type}")

# 팩토리 패턴 사용
factory = AnimalFactory()
dog = factory.create_animal("dog")
cat = factory.create_animal("cat")

print(f"강아지: {dog.speak()}")
print(f"고양이: {cat.speak()}")

# 2. 옵저버 패턴
print("\n=== 옵저버 패턴 ===")

class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def __init__(self, name):
        self.name = name
    
    def update(self, message):
        print(f"{self.name}이(가) 메시지를 받았습니다: {message}")

# 옵저버 패턴 사용
subject = Subject()
observer1 = Observer("옵저버1")
observer2 = Observer("옵저버2")

subject.attach(observer1)
subject.attach(observer2)
subject.notify("안녕하세요!")

# 3. 전략 패턴
print("\n=== 전략 패턴 ===")

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"신용카드로 {amount}원 결제"

class CashPayment(PaymentStrategy):
    def pay(self, amount):
        return f"현금으로 {amount}원 결제"

class PaymentContext:
    def __init__(self, strategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy):
        self._strategy = strategy
    
    def execute_payment(self, amount):
        return self._strategy.pay(amount)

# 전략 패턴 사용
context = PaymentContext(CreditCardPayment())
print(context.execute_payment(10000))

context.set_strategy(CashPayment())
print(context.execute_payment(5000))

# 4. 어댑터 패턴
print("\n=== 어댑터 패턴 ===")

class OldSystem:
    def old_method(self):
        return "구 시스템의 메서드"

class NewSystem:
    def new_method(self):
        return "새 시스템의 메서드"

class Adapter:
    def __init__(self, old_system):
        self.old_system = old_system
    
    def new_method(self):
        return f"어댑터: {self.old_system.old_method()}"

# 어댑터 패턴 사용
old_system = OldSystem()
adapter = Adapter(old_system)
print(adapter.new_method())

# 5. 데코레이터 패턴
print("\n=== 데코레이터 패턴 ===")

class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        return "기본 컴포넌트"

class Decorator(Component):
    def __init__(self, component):
        self._component = component
    
    def operation(self):
        return self._component.operation()

class ConcreteDecoratorA(Decorator):
    def operation(self):
        return f"데코레이터 A: {super().operation()}"

class ConcreteDecoratorB(Decorator):
    def operation(self):
        return f"데코레이터 B: {super().operation()}"

# 데코레이터 패턴 사용
component = ConcreteComponent()
decorator_a = ConcreteDecoratorA(component)
decorator_b = ConcreteDecoratorB(decorator_a)

print(component.operation())
print(decorator_a.operation())
print(decorator_b.operation())

print("\n프로그램 종료") 