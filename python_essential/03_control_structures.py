# 파이썬 제어 구조

# 1. 조건문 (if-elif-else)
print("=== 조건문 (if-elif-else) ===")

# 기본 if문
age = 20
if age >= 18:
    print("성인입니다.")
else:
    print("미성년자입니다.")

# if-elif-else
score = 85
if score >= 90:
    print("A 등급")
elif score >= 80:
    print("B 등급")
elif score >= 70:
    print("C 등급")
else:
    print("D 등급")

# 중첩된 if문
age = 20
has_ticket = True
if age >= 18:
    if has_ticket:
        print("입장 가능합니다.")
    else:
        print("티켓이 필요합니다.")
else:
    print("나이가 부족합니다.")

# 조건부 표현식 (삼항 연산자)
age = 20
status = "성인" if age >= 18 else "미성년자"

# 2. 반복문 (for)
print("\n=== 반복문 (for) ===")

# 기본 for문
print("기본 for문:")
for i in range(5):
    print(f"i = {i}")

# range() 사용
print("\nrange() 사용:")
print("1부터 10까지:")
for i in range(1, 11):
    print(i, end=" ")
print()

print("2씩 증가:")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# 리스트 순회
print("\n리스트 순회:")
fruits = ["사과", "바나나", "오렌지"]
for fruit in fruits:
    print(fruit)

# enumerate() 사용
print("\nenumerate() 사용:")
for index, fruit in enumerate(fruits):
    print(f"인덱스 {index}: {fruit}")

# 딕셔너리 순회
print("\n딕셔너리 순회:")
person = {"name": "홍길동", "age": 25, "city": "서울"}
for key in person:
    print(f"키: {key}, 값: {person[key]}")

for key, value in person.items():
    print(f"키: {key}, 값: {value}")

# 3. 반복문 (while)
print("\n=== 반복문 (while) ===")

# 기본 while문
print("기본 while문:")
count = 0
while count < 5:
    print(f"count = {count}")
    count += 1

# break 사용
print("\nbreak 사용:")
count = 0
while True:
    if count >= 5:
        break
    print(f"count = {count}")
    count += 1

# continue 사용
print("\ncontinue 사용:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# 4. 예외 처리 (try-except)
print("\n=== 예외 처리 (try-except) ===")

# 기본 예외 처리
print("기본 예외 처리:")
try:
    number = int(input("숫자를 입력하세요: "))
    result = 10 / number
    print(f"결과: {result}")
except ValueError:
    print("올바른 숫자를 입력하세요.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except Exception as e:
    print(f"오류 발생: {e}")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("프로그램을 종료합니다.")

# 5. with 문 (컨텍스트 관리자)
print("\n=== with 문 (컨텍스트 관리자) ===")

# 파일 처리
print("파일 처리:")
try:
    with open("test.txt", "w") as file:
        file.write("Hello, Python!")
    print("파일이 성공적으로 생성되었습니다.")
except IOError as e:
    print(f"파일 처리 중 오류 발생: {e}")

# 6. match 문 (Python 3.10+)
print("\n=== match 문 (Python 3.10+) ===")

# 기본 match문
def check_command(command):
    match command:
        case "start":
            return "시작합니다."
        case "stop":
            return "중지합니다."
        case "restart":
            return "재시작합니다."
        case _:
            return "알 수 없는 명령입니다."

print(check_command("start"))
print(check_command("stop"))
print(check_command("unknown"))

# 패턴 매칭
def process_point(point):
    match point:
        case (x, y):
            return f"2D 좌표: ({x}, {y})"
        case (x, y, z):
            return f"3D 좌표: ({x}, {y}, {z})"
        case _:
            return "알 수 없는 좌표입니다."

print(process_point((1, 2)))
print(process_point((1, 2, 3)))

# 7. 제어문과 컴프리헨션
print("\n=== 제어문과 컴프리헨션 ===")

# 리스트 컴프리헨션과 조건문
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"짝수: {even_numbers}")

# 딕셔너리 컴프리헨션과 조건문
squares = {x: x**2 for x in range(5) if x % 2 == 0}
print(f"짝수의 제곱: {squares}")

# 8. 제어문과 함수
print("\n=== 제어문과 함수 ===")

# 조건부 반환
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"

print(f"85점의 등급: {get_grade(85)}")

# 재귀 함수
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"5의 팩토리얼: {factorial(5)}")

# 9. 제어문과 클래스
print("\n=== 제어문과 클래스 ===")

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        else:
            return "D"
    
    def is_passing(self):
        return self.score >= 60

student = Student("홍길동", 85)
print(f"{student.name}의 등급: {student.get_grade()}")
print(f"합격 여부: {'합격' if student.is_passing() else '불합격'}") 