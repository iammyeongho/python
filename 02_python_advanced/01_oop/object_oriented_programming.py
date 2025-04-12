"""
PHP와 Python의 객체지향 프로그래밍 비교
이 파일은 PHP 개발자가 Python의 객체지향 프로그래밍을 이해하는 데 도움을 주기 위한 예제입니다.
"""

from typing import List, Dict, Optional, Any
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum

class UserRole(Enum):
    """사용자 역할을 정의하는 열거형 (PHP의 enum과 유사)"""
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

@dataclass
class User:
    """사용자 데이터 클래스 (PHP의 클래스와 유사)"""
    name: str
    email: str
    role: UserRole
    age: Optional[int] = None

    def __post_init__(self):
        """초기화 후 검증"""
        if not self.email or "@" not in self.email:
            raise ValueError("Invalid email address")

    def get_info(self) -> str:
        """사용자 정보 반환"""
        return f"Name: {self.name}, Email: {self.email}, Role: {self.role.value}"

class Animal(ABC):
    """추상 클래스 (PHP의 추상 클래스와 유사)"""
    
    @abstractmethod
    def make_sound(self) -> str:
        """추상 메서드"""
        pass

    def sleep(self) -> str:
        """일반 메서드"""
        return "Zzz..."

class Dog(Animal):
    """상속 예제 (PHP의 상속과 유사)"""
    
    def __init__(self, name: str):
        self.name = name
    
    def make_sound(self) -> str:
        return "Woof!"
    
    def fetch(self) -> str:
        return f"{self.name} is fetching the ball"

class Cat(Animal):
    """다른 동물 클래스"""
    
    def __init__(self, name: str):
        self.name = name
    
    def make_sound(self) -> str:
        return "Meow!"
    
    def climb(self) -> str:
        return f"{self.name} is climbing the tree"

class UserManager:
    """싱글톤 패턴 예제 (PHP의 싱글톤과 유사)"""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.users: Dict[str, User] = {}
        return cls._instance
    
    def add_user(self, user: User) -> None:
        """사용자 추가"""
        self.users[user.email] = user
    
    def get_user(self, email: str) -> Optional[User]:
        """사용자 조회"""
        return self.users.get(email)
    
    def remove_user(self, email: str) -> bool:
        """사용자 삭제"""
        if email in self.users:
            del self.users[email]
            return True
        return False

class Logger:
    """정적 메서드 예제 (PHP의 정적 메서드와 유사)"""
    
    @staticmethod
    def log(message: str) -> None:
        """로그 메시지 출력"""
        print(f"[LOG] {message}")
    
    @classmethod
    def log_with_timestamp(cls, message: str) -> None:
        """타임스탬프가 포함된 로그 메시지 출력"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {message}")

class PropertyExample:
    """프로퍼티 예제 (PHP의 매직 메서드와 유사)"""
    
    def __init__(self):
        self._value = 0
    
    @property
    def value(self) -> int:
        """게터 메서드"""
        return self._value
    
    @value.setter
    def value(self, new_value: int) -> None:
        """세터 메서드"""
        if new_value < 0:
            raise ValueError("Value cannot be negative")
        self._value = new_value
    
    @value.deleter
    def value(self) -> None:
        """딜리터 메서드"""
        self._value = 0

def main():
    """메인 함수"""
    
    # 데이터 클래스 사용
    user = User("John Doe", "john@example.com", UserRole.ADMIN, 30)
    print(user.get_info())
    
    # 상속과 다형성
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    
    animals: List[Animal] = [dog, cat]
    for animal in animals:
        print(f"{animal.__class__.__name__} says: {animal.make_sound()}")
        if isinstance(animal, Dog):
            print(animal.fetch())
        elif isinstance(animal, Cat):
            print(animal.climb())
    
    # 싱글톤 패턴
    manager1 = UserManager()
    manager2 = UserManager()
    print(f"Same instance: {manager1 is manager2}")
    
    manager1.add_user(user)
    print(manager2.get_user("john@example.com").get_info())
    
    # 정적 메서드
    Logger.log("This is a log message")
    Logger.log_with_timestamp("This is a timestamped log message")
    
    # 프로퍼티
    prop = PropertyExample()
    prop.value = 42
    print(f"Value: {prop.value}")
    del prop.value
    print(f"Value after deletion: {prop.value}")

if __name__ == "__main__":
    main() 