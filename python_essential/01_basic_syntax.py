# 파이썬 기본 문법과 데이터 타입

# 1. 변수와 데이터 타입
print("=== 변수와 데이터 타입 ===")

# 숫자형 (정수, 실수, 복소수)
integer = 42
float_num = 3.14
complex_num = 1 + 2j

print(f"정수: {integer}, 타입: {type(integer)}")
print(f"실수: {float_num}, 타입: {type(float_num)}")
print(f"복소수: {complex_num}, 타입: {type(complex_num)}")

# 문자열
string1 = "안녕하세요"
string2 = '파이썬'
string3 = """여러 줄
문자열
입니다."""

print(f"문자열1: {string1}, 타입: {type(string1)}")
print(f"문자열2: {string2}, 타입: {type(string2)}")
print(f"문자열3: {string3}, 타입: {type(string3)}")

# 불리언
boolean_true = True
boolean_false = False

print(f"참: {boolean_true}, 타입: {type(boolean_true)}")
print(f"거짓: {boolean_false}, 타입: {type(boolean_false)}")

# None 타입
none_value = None
print(f"None: {none_value}, 타입: {type(none_value)}")

# 2. 연산자
print("\n=== 연산자 ===")

# 산술 연산자
a, b = 10, 3
print(f"덧셈: {a + b}")
print(f"뺄셈: {a - b}")
print(f"곱셈: {a * b}")
print(f"나눗셈: {a / b}")
print(f"몫: {a // b}")
print(f"나머지: {a % b}")
print(f"거듭제곱: {a ** b}")

# 비교 연산자
print(f"\n비교 연산자:")
print(f"a > b: {a > b}")
print(f"a < b: {a < b}")
print(f"a >= b: {a >= b}")
print(f"a <= b: {a <= b}")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")

# 논리 연산자
x, y = True, False
print(f"\n논리 연산자:")
print(f"x and y: {x and y}")
print(f"x or y: {x or y}")
print(f"not x: {not x}")

# 할당 연산자
c = 10
print(f"\n할당 연산자:")
print(f"c = 10: {c}")
c += 5  # c = c + 5
print(f"c += 5: {c}")
c -= 3  # c = c - 3
print(f"c -= 3: {c}")
c *= 2  # c = c * 2
print(f"c *= 2: {c}")
c /= 4  # c = c / 4
print(f"c /= 4: {c}")

# 3. 문자열 포맷팅
print("\n=== 문자열 포맷팅 ===")

name = "홍길동"
age = 25
height = 175.5

# % 연산자 (오래된 방식)
print("이름: %s, 나이: %d, 키: %.1f" % (name, age, height))

# str.format() 메서드
print("이름: {}, 나이: {}, 키: {:.1f}".format(name, age, height))
print("이름: {0}, 나이: {1}, 키: {2:.1f}".format(name, age, height))
print("이름: {n}, 나이: {a}, 키: {h:.1f}".format(n=name, a=age, h=height))

# f-string (Python 3.6+)
print(f"이름: {name}, 나이: {age}, 키: {height:.1f}")

# 4. 타입 변환
print("\n=== 타입 변환 ===")

# 문자열을 숫자로
str_num = "123"
print(f"문자열 '{str_num}'을 정수로 변환: {int(str_num)}")
print(f"문자열 '{str_num}'을 실수로 변환: {float(str_num)}")

# 숫자를 문자열로
num = 456
print(f"숫자 {num}을 문자열로 변환: {str(num)}")

# 5. 입력과 출력
print("\n=== 입력과 출력 ===")

# 입력 예제 (실행 시 주석 해제)
# user_input = input("이름을 입력하세요: ")
# print(f"안녕하세요, {user_input}님!")

# 6. 주석
print("\n=== 주석 ===")

# 한 줄 주석
"""
여러 줄
주석입니다.
"""

'''
이것도
여러 줄
주석입니다.
'''

# 7. 들여쓰기
print("\n=== 들여쓰기 ===")

def example_function():
    print("들여쓰기가 적용된 코드")
    if True:
        print("더 들여쓰기된 코드")
        for i in range(3):
            print("가장 들여쓰기된 코드")

# 8. 라인 연결
print("\n=== 라인 연결 ===")

long_string = "이것은 매우 긴 문자열입니다. " \
              "백슬래시를 사용하여 " \
              "여러 줄로 나눌 수 있습니다."

long_calculation = 1 + 2 + 3 + \
                  4 + 5 + 6 + \
                  7 + 8 + 9

print(long_string)
print(f"계산 결과: {long_calculation}")

# 9. 특수 문자
print("\n=== 특수 문자 ===")

print("줄바꿈: 첫 번째 줄\n두 번째 줄")
print("탭: 첫 번째\t두 번째")
print("백슬래시: \\")
print("따옴표: \"큰따옴표\", \'작은따옴표\'")
print("유니코드: \u0041 (A)")

# 10. 식별자 규칙
print("\n=== 식별자 규칙 ===")

# 올바른 식별자
valid_name = "홍길동"
valid_age1 = 25
valid_age_2 = 26
ValidName = "김철수"  # 클래스 이름은 보통 이렇게 작성

# 잘못된 식별자 (주석으로 표시)
# 1name = "이름"  # 숫자로 시작할 수 없음
# my-name = "이름"  # 하이픈 사용 불가
# my name = "이름"  # 공백 사용 불가
# if = "이름"  # 예약어 사용 불가

# 11. 예약어
print("\n=== 예약어 ===")

import keyword
print("파이썬 예약어 목록:")
print(keyword.kwlist)

# 12. 모듈 임포트
print("\n=== 모듈 임포트 ===")

# 기본 모듈 임포트
import math
print(f"파이(π): {math.pi}")
print(f"5의 제곱근: {math.sqrt(25)}")

# 특정 함수만 임포트
from random import randint
print(f"1에서 10 사이의 랜덤 정수: {randint(1, 10)}")

# 별칭 사용
import datetime as dt
print(f"현재 날짜: {dt.datetime.now().strftime('%Y-%m-%d')}")

# 13. 기본 내장 함수
print("\n=== 기본 내장 함수 ===")

# 타입 변환 함수
print(f"int('123'): {int('123')}")
print(f"str(456): {str(456)}")
print(f"float('3.14'): {float('3.14')}")
print(f"bool(1): {bool(1)}")
print(f"bool(0): {bool(0)}")

# 수학 함수
print(f"abs(-10): {abs(-10)}")
print(f"max(1, 2, 3, 4, 5): {max(1, 2, 3, 4, 5)}")
print(f"min(1, 2, 3, 4, 5): {min(1, 2, 3, 4, 5)}")
print(f"sum([1, 2, 3, 4, 5]): {sum([1, 2, 3, 4, 5])}")

# 시퀀스 함수
numbers = [1, 2, 3, 4, 5]
print(f"len(numbers): {len(numbers)}")
print(f"list(range(5)): {list(range(5))}")
print(f"enumerate(numbers): {list(enumerate(numbers))}")
print(f"zip([1, 2, 3], ['a', 'b', 'c']): {list(zip([1, 2, 3], ['a', 'b', 'c']))}")

# 기타 유용한 함수
print(f"type(42): {type(42)}")
print(f"id(42): {id(42)}")
print(f"dir([]): {dir([])}")
print(f"help(list)")  # 주석 처리 - 너무 많은 출력을 방지하기 위해 