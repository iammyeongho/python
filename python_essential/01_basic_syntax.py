# 파이썬 기본 문법 예제
# 작성일: 2024-04-08
# 목적: 파이썬의 기본 문법과 관련된 다양한 기능을 설명하는 예제 코드

# 1. 변수와 데이터 타입
# 파이썬은 동적 타입 언어로, 변수 선언 시 타입을 명시하지 않습니다.
print("=== 1. 변수와 데이터 타입 ===")

# 숫자형 (정수, 실수)
integer = 42  # 정수
float_num = 3.14  # 실수
complex_num = 1 + 2j  # 복소수
print(f"정수: {integer}, 타입: {type(integer)}")
print(f"실수: {float_num}, 타입: {type(float_num)}")
print(f"복소수: {complex_num}, 타입: {type(complex_num)}")

# 문자열
string = "안녕하세요"  # 문자열
multi_line = """여러 줄
문자열입니다."""  # 여러 줄 문자열
print(f"문자열: {string}, 타입: {type(string)}")
print(f"여러 줄 문자열:\n{multi_line}")

# 불리언
boolean = True  # 불리언
print(f"불리언: {boolean}, 타입: {type(boolean)}")

# None 타입
none_value = None  # None 타입
print(f"None: {none_value}, 타입: {type(none_value)}")

# 2. 문자열 포맷팅
# 문자열을 다양한 방식으로 포맷팅할 수 있습니다.
print("\n=== 2. 문자열 포맷팅 ===")

# f-string (Python 3.6+)
name = "홍길동"
age = 25
print(f"이름: {name}, 나이: {age}")

# format() 메서드
print("이름: {}, 나이: {}".format(name, age))
print("이름: {n}, 나이: {a}".format(n=name, a=age))

# % 연산자 (구식)
print("이름: %s, 나이: %d" % (name, age))

# 3. 연산자
# 파이썬의 다양한 연산자를 사용할 수 있습니다.
print("\n=== 3. 연산자 ===")

# 산술 연산자
a, b = 10, 3
print(f"덧셈: {a + b}")  # 13
print(f"뺄셈: {a - b}")  # 7
print(f"곱셈: {a * b}")  # 30
print(f"나눗셈: {a / b}")  # 3.3333...
print(f"몫: {a // b}")  # 3
print(f"나머지: {a % b}")  # 1
print(f"제곱: {a ** b}")  # 1000

# 비교 연산자
print(f"\n비교 연산자:")
print(f"a > b: {a > b}")  # True
print(f"a < b: {a < b}")  # False
print(f"a >= b: {a >= b}")  # True
print(f"a <= b: {a <= b}")  # False
print(f"a == b: {a == b}")  # False
print(f"a != b: {a != b}")  # True

# 논리 연산자
print(f"\n논리 연산자:")
print(f"True and True: {True and True}")  # True
print(f"True and False: {True and False}")  # False
print(f"True or False: {True or False}")  # True
print(f"not True: {not True}")  # False

# 4. 조건문
# 조건에 따라 다른 코드를 실행할 수 있습니다.
print("\n=== 4. 조건문 ===")

# if-elif-else 문
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")

# 조건부 표현식 (삼항 연산자)
age = 20
status = "성인" if age >= 18 else "미성년자"

# 5. 반복문
# 코드를 반복해서 실행할 수 있습니다.
print("\n=== 5. 반복문 ===")

# for 문
print("for 문:")
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4
print()

# while 문
print("\nwhile 문:")
i = 0
while i < 5:
    print(i, end=" ")
    i += 1
print()  # 0 1 2 3 4

# break 문
print("\nbreak 문:")
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print()  # 0 1 2 3 4

# continue 문
print("\ncontinue 문:")
for i in range(5):
    if i == 2:
        continue
    print(i, end=" ")
print()  # 0 1 3 4

# 6. 리스트 컴프리헨션
# 리스트를 간단하게 생성할 수 있습니다.
print("\n=== 6. 리스트 컴프리헨션 ===")

# 기본 리스트 컴프리헨션
squares = [x**2 for x in range(5)]
print(f"제곱수 리스트: {squares}")  # [0, 1, 4, 9, 16]

# 조건부 리스트 컴프리헨션
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"짝수의 제곱: {even_squares}")  # [0, 4, 16, 36, 64]

# 7. 함수 정의
# 함수를 정의하고 호출할 수 있습니다.
print("\n=== 7. 함수 정의 ===")

# 기본 함수
def greet(name):
    return f"안녕하세요, {name}님!"

print(greet("홍길동"))  # 안녕하세요, 홍길동님!

# 기본값 매개변수
def greet_with_title(name, title="님"):
    return f"안녕하세요, {name}{title}!"

print(greet_with_title("홍길동"))  # 안녕하세요, 홍길동님!
print(greet_with_title("홍길동", "선생님"))  # 안녕하세요, 홍길동선생님!

# 가변 매개변수
def sum_numbers(*args):
    return sum(args)

print(f"sum_numbers(1, 2, 3): {sum_numbers(1, 2, 3)}")  # 6
print(f"sum_numbers(1, 2, 3, 4, 5): {sum_numbers(1, 2, 3, 4, 5)}")  # 15

# 8. 예외 처리
# 예외를 처리할 수 있습니다.
print("\n=== 8. 예외 처리 ===")

# try-except 문
try:
    number = int("abc")
except ValueError:
    print("숫자로 변환할 수 없습니다.")

# try-except-else 문
try:
    number = int("123")
except ValueError:
    print("숫자로 변환할 수 없습니다.")
else:
    print("성공적으로 변환되었습니다.")

# try-except-finally 문
try:
    number = int("abc")
except ValueError:
    print("숫자로 변환할 수 없습니다.")
finally:
    print("항상 실행됩니다.")

# 9. 모듈 임포트
# 모듈을 임포트하여 사용할 수 있습니다.
print("\n=== 9. 모듈 임포트 ===")

# 기본 임포트
import math
print(f"파이: {math.pi}")  # 3.141592653589793
print(f"제곱근: {math.sqrt(16)}")  # 4.0

# from 임포트
from random import randint
print(f"랜덤 정수: {randint(1, 10)}")  # 1부터 10 사이의 랜덤 정수

# as 임포트
import datetime as dt
now = dt.datetime.now()
print(f"현재 시간: {now}")

print("\n프로그램 종료") 