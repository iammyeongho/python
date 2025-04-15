"""
파이썬 객체 지향 프로그래밍: SOLID 원칙
이 파일은 SOLID 원칙의 개념을 설명합니다.
"""

from abc import ABC, abstractmethod

# 1. 단일 책임 원칙 (SRP)
print("=== 단일 책임 원칙 (SRP) ===")

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    def save(self, user):
        print(f"사용자 {user.name} 저장")
        # 실제로는 데이터베이스에 저장하는 코드가 들어감

class EmailService:
    def send_email(self, user, message):
        print(f"{user.email}로 이메일 전송: {message}")

# SRP 적용
user = User("홍길동", "hong@example.com")
repository = UserRepository()
email_service = EmailService()

repository.save(user)
email_service.send_email(user, "환영합니다!")

# 2. 개방-폐쇄 원칙 (OCP)
print("\n=== 개방-폐쇄 원칙 (OCP) ===")

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

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class AreaCalculator:
    def calculate_area(self, shapes):
        total_area = 0
        for shape in shapes:
            total_area += shape.area()
        return total_area

# OCP 적용
shapes = [
    Rectangle(5, 3),
    Circle(4)
]

calculator = AreaCalculator()
print(f"총 면적: {calculator.calculate_area(shapes):.2f}")

# 3. 리스코프 치환 원칙 (LSP)
print("\n=== 리스코프 치환 원칙 (LSP) ===")

class Bird:
    def fly(self):
        return "날아갑니다."

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("펭귄은 날 수 없습니다.")
    
    def swim(self):
        return "수영합니다."

# LSP 위반 예시
def make_bird_fly(bird):
    try:
        print(bird.fly())
    except NotImplementedError as e:
        print(f"에러: {e}")

# LSP 적용
bird = Bird()
penguin = Penguin()

make_bird_fly(bird)
make_bird_fly(penguin)

# 4. 인터페이스 분리 원칙 (ISP)
print("\n=== 인터페이스 분리 원칙 (ISP) ===")

class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

class Fax(ABC):
    @abstractmethod
    def send_fax(self):
        pass

class SimplePrinter(Printer):
    def print_document(self):
        return "문서를 출력합니다."

class MultiFunctionPrinter(Printer, Scanner, Fax):
    def print_document(self):
        return "문서를 출력합니다."
    
    def scan_document(self):
        return "문서를 스캔합니다."
    
    def send_fax(self):
        return "팩스를 전송합니다."

# ISP 적용
simple_printer = SimplePrinter()
multi_printer = MultiFunctionPrinter()

print(simple_printer.print_document())
print(multi_printer.print_document())
print(multi_printer.scan_document())
print(multi_printer.send_fax())

# 5. 의존성 역전 원칙 (DIP)
print("\n=== 의존성 역전 원칙 (DIP) ===")

class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase(Database):
    def save(self, data):
        return f"MySQL에 데이터 저장: {data}"

class PostgreSQLDatabase(Database):
    def save(self, data):
        return f"PostgreSQL에 데이터 저장: {data}"

class DataService:
    def __init__(self, database):
        self.database = database
    
    def process_data(self, data):
        return self.database.save(data)

# DIP 적용
mysql_db = MySQLDatabase()
postgres_db = PostgreSQLDatabase()

service1 = DataService(mysql_db)
service2 = DataService(postgres_db)

print(service1.process_data("데이터1"))
print(service2.process_data("데이터2"))

print("\n프로그램 종료") 