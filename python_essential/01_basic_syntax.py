# 파이썬 기본 문법 예제
# 작성일: 2024-04-08
# 목적: 파이썬의 기본적인 문법과 사용법을 설명하는 예제 코드

# 1. 변수 선언과 기본 데이터 타입
# 파이썬은 동적 타입 언어로, 변수 선언 시 타입을 명시하지 않아도 됩니다.
# 변수명은 소문자와 언더스코어를 사용하는 것이 관례입니다.
print("=== 1. 변수 선언과 기본 데이터 타입 ===")

# 정수형 변수 (int)
age = 25  # 나이를 저장하는 정수형 변수
print(f"정수형 변수 age: {age}, 타입: {type(age)}")

# 실수형 변수 (float)
height = 175.5  # 키를 저장하는 실수형 변수
print(f"실수형 변수 height: {height}, 타입: {type(height)}")

# 문자열 변수 (str)
name = "홍길동"  # 이름을 저장하는 문자열 변수
print(f"문자열 변수 name: {name}, 타입: {type(name)}")

# 불리언 변수 (bool)
is_student = True  # 학생 여부를 저장하는 불리언 변수
print(f"불리언 변수 is_student: {is_student}, 타입: {type(is_student)}")

# 2. 기본 연산자
# 파이썬은 다양한 연산자를 지원합니다.
print("\n=== 2. 기본 연산자 ===")

# 산술 연산자
a = 10
b = 3
print(f"덧셈: {a + b}")  # 더하기
print(f"뺄셈: {a - b}")  # 빼기
print(f"곱셈: {a * b}")  # 곱하기
print(f"나눗셈: {a / b}")  # 나누기 (실수 결과)
print(f"몫: {a // b}")  # 몫 (정수 결과)
print(f"나머지: {a % b}")  # 나머지
print(f"제곱: {a ** b}")  # 제곱

# 비교 연산자
print(f"\n비교 연산자:")
print(f"a > b: {a > b}")  # 크다
print(f"a < b: {a < b}")  # 작다
print(f"a >= b: {a >= b}")  # 크거나 같다
print(f"a <= b: {a <= b}")  # 작거나 같다
print(f"a == b: {a == b}")  # 같다
print(f"a != b: {a != b}")  # 같지 않다

# 논리 연산자
x = True
y = False
print(f"\n논리 연산자:")
print(f"x and y: {x and y}")  # 논리곱
print(f"x or y: {x or y}")  # 논리합
print(f"not x: {not x}")  # 논리부정

# 3. 문자열 처리
# 파이썬은 강력한 문자열 처리 기능을 제공합니다.
print("\n=== 3. 문자열 처리 ===")

# 문자열 생성
greeting = "안녕하세요"
name = "파이썬"
print(f"기본 문자열: {greeting}")

# 문자열 연결
message = greeting + " " + name + "!"
print(f"문자열 연결: {message}")

# 문자열 반복
stars = "*" * 5
print(f"문자열 반복: {stars}")

# 문자열 인덱싱과 슬라이싱
text = "파이썬 프로그래밍"
print(f"첫 번째 문자: {text[0]}")  # 인덱싱
print(f"처음부터 3번째까지: {text[:3]}")  # 슬라이싱
print(f"3번째부터 끝까지: {text[2:]}")  # 슬라이싱
print(f"역순 출력: {text[::-1]}")  # 역순 슬라이싱

# 문자열 메서드
text = "  Python Programming  "
print(f"\n문자열 메서드:")
print(f"대문자 변환: {text.upper()}")  # 대문자로 변환
print(f"소문자 변환: {text.lower()}")  # 소문자로 변환
print(f"공백 제거: {text.strip()}")  # 양쪽 공백 제거
print(f"문자열 길이: {len(text)}")  # 문자열 길이
print(f"특정 문자 개수: {text.count('n')}")  # 특정 문자 개수 세기

# 4. f-string (문자열 포매팅)
# Python 3.6 이상에서 도입된 f-string은 문자열 포매팅을 더 쉽게 만듭니다.
print("\n=== 4. f-string (문자열 포매팅) ===")

name = "김철수"
age = 20
height = 175.5
print(f"이름: {name}, 나이: {age}, 키: {height}cm")
print(f"키는 {height:.1f}cm 입니다.")  # 소수점 한 자리까지 표시

# 5. 타입 변환
# 파이썬에서는 다양한 타입 변환 함수를 제공합니다.
print("\n=== 5. 타입 변환 ===")

# 문자열을 숫자로 변환
num_str = "123"
num_int = int(num_str)  # 문자열을 정수로 변환
num_float = float(num_str)  # 문자열을 실수로 변환
print(f"문자열 '{num_str}'을 정수로 변환: {num_int}, 타입: {type(num_int)}")
print(f"문자열 '{num_str}'을 실수로 변환: {num_float}, 타입: {type(num_float)}")

# 숫자를 문자열로 변환
num = 456
str_num = str(num)  # 숫자를 문자열로 변환
print(f"숫자 {num}을 문자열로 변환: {str_num}, 타입: {type(str_num)}")

print("\n프로그램 종료") 