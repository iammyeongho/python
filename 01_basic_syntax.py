# 파이썬 기본 문법과 변수

# 1. 변수 선언과 기본 데이터 타입
name = "홍길동"  # 문자열(str)
age = 25        # 정수(int)
height = 175.5  # 실수(float)
is_student = True  # 불리언(bool)

# 2. 출력하기
print("안녕하세요!")
print(f"이름: {name}, 나이: {age}")

# 3. 기본 연산
a = 10
b = 3
print(f"덧셈: {a + b}")
print(f"뺄셈: {a - b}")
print(f"곱셈: {a * b}")
print(f"나눗셈: {a / b}")
print(f"나눗셈 몫: {a // b}")
print(f"나머지: {a % b}")
print(f"제곱: {a ** b}")

# 4. 문자열 연산
first_name = "파이"
last_name = "썬"
full_name = first_name + last_name
print(f"전체 이름: {full_name}")
print(f"이름 반복: {first_name * 3}")

# 5. 타입 변환
number_str = "100"
number = int(number_str)
print(f"문자열을 숫자로 변환: {number + 1}")

# 6. 주석
# 한 줄 주석
"""
여러 줄
주석
"""