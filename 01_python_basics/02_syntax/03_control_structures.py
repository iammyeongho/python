# 파이썬 제어 구조 예제
# 작성일: 2024-04-08
# 목적: 파이썬의 제어 구조와 관련된 다양한 기능을 설명하는 예제 코드

# 1. 조건문 (if-elif-else)
# 조건에 따라 다른 코드를 실행하는 구조
print("=== 1. 조건문 (if-elif-else) ===")

# 기본 if 문
# if 조건문: 조건이 참일 때 실행할 코드
age = 20
if age >= 18:
    print("성인입니다.")

# if-else 문
# if 조건문: 조건이 참일 때 실행할 코드
# else: 조건이 거짓일 때 실행할 코드
age = 15
if age >= 18:
    print("성인입니다.")
else:
    print("미성년자입니다.")

# if-elif-else 문
# if 조건문1: 조건1이 참일 때 실행할 코드
# elif 조건문2: 조건1이 거짓이고 조건2가 참일 때 실행할 코드
# else: 모든 조건이 거짓일 때 실행할 코드
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")

# 중첩 if 문
# if 문 안에 또 다른 if 문을 사용하여 복잡한 조건 처리
age = 20
has_ticket = True
if age >= 18:
    if has_ticket:
        print("입장 가능합니다.")
    else:
        print("티켓이 필요합니다.")
else:
    print("미성년자는 입장할 수 없습니다.")

# 2. 반복문 (for)
# 시퀀스를 순회하며 반복하는 구조
print("\n=== 2. 반복문 (for) ===")

# 기본 for 문
# for 변수 in range(시작, 끝, 간격): 반복할 코드
print("기본 for 문:")
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4
print()

# 리스트 순회
# for 변수 in 리스트: 리스트의 각 요소에 대해 실행할 코드
print("\n리스트 순회:")
fruits = ["사과", "바나나", "오렌지"]
for fruit in fruits:
    print(fruit, end=" ")  # 사과 바나나 오렌지
print()

# 딕셔너리 순회
# for 키 in 딕셔너리: 딕셔너리의 각 키에 대해 실행할 코드
print("\n딕셔너리 순회:")
person = {"name": "홍길동", "age": 25, "city": "서울"}
for key in person:
    print(f"{key}: {person[key]}", end=", ")  # name: 홍길동, age: 25, city: 서울
print()

# enumerate() 함수 사용
# for 인덱스, 값 in enumerate(시퀀스): 인덱스와 값을 함께 사용하는 반복문
print("\nenumerate() 함수 사용:")
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}", end=", ")  # 0: 사과, 1: 바나나, 2: 오렌지
print()

# zip() 함수 사용
# for 변수1, 변수2 in zip(시퀀스1, 시퀀스2): 여러 시퀀스를 동시에 순회하는 반복문
print("\nzip() 함수 사용:")
names = ["홍길동", "김철수", "이영희"]
ages = [25, 30, 28]
for name, age in zip(names, ages):
    print(f"{name}: {age}세", end=", ")  # 홍길동: 25세, 김철수: 30세, 이영희: 28세
print()

# 3. 반복문 (while)
# 조건이 참인 동안 반복하는 구조
print("\n=== 3. 반복문 (while) ===")

# 기본 while 문
# while 조건문: 조건이 참인 동안 반복 실행할 코드
print("기본 while 문:")
i = 0
while i < 5:
    print(i, end=" ")
    i += 1
print()  # 0 1 2 3 4

# break 문
# while True: 무한 반복문에서 break를 만나면 반복문을 즉시 종료
print("\nbreak 문:")
i = 0
while True:
    if i >= 5:
        break
    print(i, end=" ")
    i += 1
print()  # 0 1 2 3 4

# continue 문
# while 조건문: continue를 만나면 현재 반복을 건너뛰고 다음 반복으로 진행
print("\ncontinue 문:")
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()  # 1 3 5 7 9

# 4. 예외 처리 (try-except)
# 예외가 발생할 수 있는 코드를 처리하는 구조
print("\n=== 4. 예외 처리 (try-except) ===")

# 기본 try-except 문
# try: 예외가 발생할 수 있는 코드
# except 예외타입: 예외 발생 시 실행할 코드
print("기본 try-except 문:")
try:
    number = int("abc")
except ValueError:
    print("숫자로 변환할 수 없습니다.")

# 여러 예외 처리
# try: 예외가 발생할 수 있는 코드
# except 예외타입1: 예외1 발생 시 실행할 코드
# except 예외타입2: 예외2 발생 시 실행할 코드
print("\n여러 예외 처리:")
try:
    number = int("abc")
    result = 10 / number
except ValueError:
    print("숫자로 변환할 수 없습니다.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except Exception as e:
    print(f"예외 발생: {e}")

# try-except-else 문
# try: 예외가 발생할 수 있는 코드
# except: 예외 발생 시 실행할 코드
# else: 예외가 발생하지 않았을 때 실행할 코드
print("\ntry-except-else 문:")
try:
    number = int("123")
except ValueError:
    print("숫자로 변환할 수 없습니다.")
else:
    print("성공적으로 변환되었습니다.")

# try-except-finally 문
# try: 예외가 발생할 수 있는 코드
# except: 예외 발생 시 실행할 코드
# finally: 예외 발생 여부와 관계없이 항상 실행할 코드
print("\ntry-except-finally 문:")
try:
    number = int("abc")
except ValueError:
    print("숫자로 변환할 수 없습니다.")
finally:
    print("항상 실행됩니다.")

# 5. 컨텍스트 관리자 (with)
# 리소스를 자동으로 관리하는 구조
print("\n=== 5. 컨텍스트 관리자 (with) ===")

# 파일 처리
# with open(파일경로, 모드) as 변수: 파일을 자동으로 열고 닫는 컨텍스트 관리자
print("파일 처리:")
with open("example.txt", "w") as f:
    f.write("Hello, Python!")

with open("example.txt", "r") as f:
    content = f.read()
    print(f"파일 내용: {content}")

# 6. match 문 (Python 3.10+)
# 패턴 매칭을 위한 구조
print("\n=== 6. match 문 (Python 3.10+) ===")

# 기본 match 문
# match 변수:
#     case 패턴1: 패턴1과 일치할 때 실행할 코드
#     case 패턴2: 패턴2와 일치할 때 실행할 코드
print("기본 match 문:")
command = "start"
match command:
    case "start":
        print("시작합니다.")
    case "stop":
        print("중지합니다.")
    case "restart":
        print("재시작합니다.")
    case _:
        print("알 수 없는 명령입니다.")

# 패턴 매칭
# match 변수:
#     case (x, y): 튜플 패턴 매칭
print("\n패턴 매칭:")
point = (3, 4)
match point:
    case (0, 0):
        print("원점입니다.")
    case (0, y):
        print(f"y축 위의 점입니다. y={y}")
    case (x, 0):
        print(f"x축 위의 점입니다. x={x}")
    case (x, y):
        print(f"좌표 ({x}, {y})입니다.")

# 7. 컴프리헨션
# 시퀀스를 간단하게 생성하는 방법
print("\n=== 7. 컴프리헨션 ===")

# 리스트 컴프리헨션
# [표현식 for 변수 in 시퀀스]: 시퀀스의 각 요소에 대해 표현식을 적용한 리스트 생성
print("리스트 컴프리헨션:")
squares = [x**2 for x in range(5)]
print(f"제곱수 리스트: {squares}")  # [0, 1, 4, 9, 16]

# 조건부 리스트 컴프리헨션
# [표현식 for 변수 in 시퀀스 if 조건]: 조건을 만족하는 요소에 대해서만 표현식을 적용
print("\n조건부 리스트 컴프리헨션:")
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"짝수의 제곱: {even_squares}")  # [0, 4, 16, 36, 64]

# 딕셔너리 컴프리헨션
# {키: 값 for 변수 in 시퀀스}: 시퀀스의 각 요소에 대해 키-값 쌍을 생성
print("\n딕셔너리 컴프리헨션:")
square_dict = {x: x**2 for x in range(5)}
print(f"제곱수 딕셔너리: {square_dict}")  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 집합 컴프리헨션
# {표현식 for 변수 in 시퀀스}: 시퀀스의 각 요소에 대해 표현식을 적용한 집합 생성
print("\n집합 컴프리헨션:")
square_set = {x**2 for x in range(5)}
print(f"제곱수 집합: {square_set}")  # {0, 1, 4, 9, 16}

# 8. 함수를 이용한 제어
# 함수를 사용하여 코드 흐름을 제어하는 방법
print("\n=== 8. 함수를 이용한 제어 ===")

# 함수를 이용한 조건 처리
# def 함수명(매개변수): 함수 정의
print("함수를 이용한 조건 처리:")
def process_number(n):
    if n < 0:
        return "음수"
    elif n > 0:
        return "양수"
    else:
        return "0"

print(f"process_number(-5): {process_number(-5)}")  # 음수
print(f"process_number(0): {process_number(0)}")  # 0
print(f"process_number(5): {process_number(5)}")  # 양수

# 함수를 이용한 반복 처리
# def 함수명(매개변수): 함수 정의
print("\n함수를 이용한 반복 처리:")
def process_items(items):
    result = []
    for item in items:
        if isinstance(item, int):
            result.append(item * 2)
        elif isinstance(item, str):
            result.append(item.upper())
    return result

items = [1, "hello", 3, "world", 5]
print(f"process_items(items): {process_items(items)}")  # [2, 'HELLO', 6, 'WORLD', 10]

# 9. 클래스를 이용한 제어
# 클래스를 사용하여 코드 흐름을 제어하는 방법
print("\n=== 9. 클래스를 이용한 제어 ===")

# 클래스를 이용한 상태 관리
# class 클래스명: 클래스 정의
print("클래스를 이용한 상태 관리:")
class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1
        return self.count
    
    def decrement(self):
        self.count -= 1
        return self.count
    
    def reset(self):
        self.count = 0
        return self.count

counter = Counter()
print(f"counter.increment(): {counter.increment()}")  # 1
print(f"counter.increment(): {counter.increment()}")  # 2
print(f"counter.decrement(): {counter.decrement()}")  # 1
print(f"counter.reset(): {counter.reset()}")  # 0

print("\n프로그램 종료") 