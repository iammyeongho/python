# 파이썬 제어 구조 예제
# 작성일: 2024-04-08
# 목적: 파이썬의 다양한 제어 구조와 그 사용법을 설명하는 예제 코드

# 1. 조건문 (if-elif-else)
# 조건문은 특정 조건에 따라 다른 코드를 실행할 수 있게 해줍니다.
print("=== 1. 조건문 (if-elif-else) ===")

# 기본 if 문
age = 20
if age >= 20:
    print("성인입니다.")
else:
    print("미성년자입니다.")

# if-elif-else 문
score = 85
if score >= 90:
    print("A 등급")
elif score >= 80:
    print("B 등급")
elif score >= 70:
    print("C 등급")
else:
    print("D 등급")

# 중첩된 if 문
age = 20
has_ticket = True
if age >= 20:
    if has_ticket:
        print("입장 가능합니다.")
    else:
        print("티켓이 필요합니다.")
else:
    print("나이 제한으로 입장할 수 없습니다.")

# 조건부 표현식 (삼항 연산자)
age = 20
status = "성인" if age >= 18 else "미성년자"

# 2. 반복문 (for)
# for 문은 시퀀스(리스트, 튜플, 문자열 등)의 각 요소에 대해 반복합니다.
print("\n=== 2. 반복문 (for) ===")

# 기본 for 문
fruits = ["사과", "바나나", "오렌지"]
for fruit in fruits:
    print(fruit)

# range() 함수를 사용한 for 문
# range(n)은 0부터 n-1까지의 숫자를 생성합니다.
for i in range(5):
    print(i)

# range() 함수의 시작과 끝을 지정
# range(start, end)는 start부터 end-1까지의 숫자를 생성합니다.
for i in range(1, 6):
    print(i)

# range() 함수의 시작, 끝, 간격을 지정
# range(start, end, step)은 start부터 end-1까지 step 간격으로 숫자를 생성합니다.
for i in range(1, 10, 2):
    print(i)

# 3. 반복문 (while)
# while 문은 조건이 참인 동안 계속해서 반복합니다.
print("\n=== 3. 반복문 (while) ===")

# 기본 while 문
count = 0
while count < 5:
    print(count)
    count += 1

# break 문
# break 문은 반복문을 즉시 종료합니다.
count = 0
while True:
    if count >= 5:
        break
    print(count)
    count += 1

# continue 문
# continue 문은 현재 반복을 건너뛰고 다음 반복으로 넘어갑니다.
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# 4. 예외 처리 (try-except)
# 예외 처리는 프로그램 실행 중 발생할 수 있는 오류를 처리합니다.
print("\n=== 4. 예외 처리 (try-except) ===")

# 기본 예외 처리
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
    print("예외 처리 종료")

# 5. 컨텍스트 매니저 (with)
# with 문은 리소스를 자동으로 관리합니다.
print("\n=== 5. 컨텍스트 매니저 (with) ===")

# 파일 처리 예제
with open("example.txt", "w") as file:
    file.write("Hello, World!")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# 6. 패턴 매칭 (match)
# match 문은 Python 3.10에서 도입된 새로운 제어 구조입니다.
print("\n=== 6. 패턴 매칭 (match) ===")

# 기본 match 문
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

# 7. 컴프리헨션
# 컴프리헨션은 리스트, 딕셔너리, 집합을 간결하게 생성할 수 있게 해줍니다.
print("\n=== 7. 컴프리헨션 ===")

# 리스트 컴프리헨션
squares = [x**2 for x in range(5)]
print(f"제곱수 리스트: {squares}")

# 조건부 리스트 컴프리헨션
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"짝수의 제곱수 리스트: {even_squares}")

# 딕셔너리 컴프리헨션
square_dict = {x: x**2 for x in range(5)}
print(f"제곱수 딕셔너리: {square_dict}")

# 8. 함수와 재귀
# 함수는 코드를 재사용할 수 있게 해주며, 재귀는 함수가 자기 자신을 호출하는 방식입니다.
print("\n=== 8. 함수와 재귀 ===")

# 기본 함수
def greet(name):
    return f"안녕하세요, {name}님!"

print(greet("홍길동"))

# 재귀 함수
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(f"5의 팩토리얼: {factorial(5)}")

# 9. 클래스
# 클래스는 객체 지향 프로그래밍의 기본 단위입니다.
print("\n=== 9. 클래스 ===")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"안녕하세요, 저는 {self.name}이고 {self.age}살입니다."

person = Person("홍길동", 25)
print(person.greet())

print("\n프로그램 종료") 