"""
파이썬 객체 지향 프로그래밍: 매직 메서드와 특수 메서드
이 파일은 매직 메서드와 특수 메서드의 개념을 설명합니다.
"""

# 1. 객체 생성과 소멸
print("=== 객체 생성과 소멸 ===")

class Lifecycle:
    def __new__(cls, *args, **kwargs):
        print("__new__ 메서드 호출")
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, name):
        print("__init__ 메서드 호출")
        self.name = name
    
    def __del__(self):
        print("__del__ 메서드 호출")

# 객체 생성
obj = Lifecycle("테스트")
print(f"객체 이름: {obj.name}")

# 객체 소멸
del obj

# 2. 문자열 표현
print("\n=== 문자열 표현 ===")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"제목: {self.title}, 저자: {self.author}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

# 객체 생성
book = Book("파이썬 프로그래밍", "홍길동")
print(str(book))      # __str__ 호출
print(repr(book))     # __repr__ 호출

# 3. 컨테이너 타입
print("\n=== 컨테이너 타입 ===")

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, value):
        self.items[index] = value
    
    def __delitem__(self, index):
        del self.items[index]
    
    def __contains__(self, item):
        return item in self.items
    
    def add_item(self, item):
        self.items.append(item)

# 객체 생성
cart = ShoppingCart()
cart.add_item("사과")
cart.add_item("바나나")
cart.add_item("오렌지")

# 컨테이너 메서드 사용
print(f"장바구니 항목 수: {len(cart)}")
print(f"첫 번째 항목: {cart[0]}")
print(f"사과가 장바구니에 있나요? {'사과' in cart}")

# 4. 비교 연산자
print("\n=== 비교 연산자 ===")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        return (self.x ** 2 + self.y ** 2) < (other.x ** 2 + other.y ** 2)
    
    def __le__(self, other):
        return (self.x ** 2 + self.y ** 2) <= (other.x ** 2 + other.y ** 2)
    
    def __gt__(self, other):
        return (self.x ** 2 + self.y ** 2) > (other.x ** 2 + other.y ** 2)
    
    def __ge__(self, other):
        return (self.x ** 2 + self.y ** 2) >= (other.x ** 2 + other.y ** 2)

# 객체 생성
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = Point(1, 2)

# 비교 연산자 사용
print(f"p1 == p3: {p1 == p3}")
print(f"p1 < p2: {p1 < p2}")
print(f"p1 <= p2: {p1 <= p2}")
print(f"p1 > p2: {p1 > p2}")
print(f"p1 >= p2: {p1 >= p2}")

# 5. 컨텍스트 매니저
print("\n=== 컨텍스트 매니저 ===")

class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print("파일을 엽니다.")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("파일을 닫습니다.")
        if self.file:
            self.file.close()

# 컨텍스트 매니저 사용
with FileHandler("test.txt", "w") as f:
    f.write("Hello, World!")

print("\n프로그램 종료") 