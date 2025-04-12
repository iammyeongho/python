# 파이썬 모듈 예제
# 작성일: 2024-04-08
# 목적: 파이썬의 모듈 시스템과 관련된 다양한 기능을 설명하는 예제 코드

# 1. 기본 모듈 임포트
# 파이썬의 내장 모듈을 임포트하는 방법을 보여줍니다.
print("=== 1. 기본 모듈 임포트 ===")

# math 모듈 임포트
import math
print(f"파이(π): {math.pi}")
print(f"제곱근(√16): {math.sqrt(16)}")
print(f"사인(90도): {math.sin(math.radians(90))}")

# random 모듈 임포트
import random
print(f"랜덤 숫자(1-10): {random.randint(1, 10)}")
print(f"랜덤 선택: {random.choice(['사과', '바나나', '오렌지'])}")

# datetime 모듈 임포트
import datetime
now = datetime.datetime.now()
print(f"현재 시간: {now}")
print(f"현재 년도: {now.year}")
print(f"현재 월: {now.month}")
print(f"현재 일: {now.day}")

# 2. from ... import 구문
# 모듈에서 특정 기능만 임포트하는 방법을 보여줍니다.
print("\n=== 2. from ... import 구문 ===")

# math 모듈에서 특정 함수만 임포트
from math import sqrt, pi
print(f"제곱근(√25): {sqrt(25)}")
print(f"파이(π): {pi}")

# random 모듈에서 여러 함수 임포트
from random import randint, choice, shuffle
numbers = [1, 2, 3, 4, 5]
shuffle(numbers)
print(f"섞은 리스트: {numbers}")
print(f"랜덤 숫자(1-100): {randint(1, 100)}")
print(f"랜덤 선택: {choice(['빨강', '파랑', '초록'])}")

# 3. 별칭 사용 (as)
# 모듈에 별칭을 지정하여 사용하는 방법을 보여줍니다.
print("\n=== 3. 별칭 사용 (as) ===")

# numpy를 np로 별칭 지정
import numpy as np
array = np.array([1, 2, 3, 4, 5])
print(f"NumPy 배열: {array}")
print(f"평균: {np.mean(array)}")
print(f"표준편차: {np.std(array)}")

# pandas를 pd로 별칭 지정
import pandas as pd
data = {'이름': ['홍길동', '김철수', '이영희'],
        '나이': [25, 30, 28],
        '도시': ['서울', '부산', '인천']}
df = pd.DataFrame(data)
print("\nPandas 데이터프레임:")
print(df)

# 4. 패키지 임포트
# 파이썬 패키지를 임포트하는 방법을 보여줍니다.
print("\n=== 4. 패키지 임포트 ===")

# matplotlib 패키지 임포트
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.title('선 그래프 예제')
plt.xlabel('X 축')
plt.ylabel('Y 축')
plt.show()

# 5. 모듈 검색 경로
# 파이썬이 모듈을 찾는 경로를 보여줍니다.
print("\n=== 5. 모듈 검색 경로 ===")

import sys
print("모듈 검색 경로:")
for path in sys.path:
    print(path)

# 6. 모듈 리로딩
# 모듈을 다시 로드하는 방법을 보여줍니다.
print("\n=== 6. 모듈 리로딩 ===")

import importlib
import math
print(f"math 모듈 리로딩 전: {math.pi}")
importlib.reload(math)
print(f"math 모듈 리로딩 후: {math.pi}")

# 7. 모듈 속성과 메서드 확인
# 모듈의 속성과 메서드를 확인하는 방법을 보여줍니다.
print("\n=== 7. 모듈 속성과 메서드 확인 ===")

# math 모듈의 속성과 메서드 확인
print("math 모듈의 속성과 메서드:")
for item in dir(math):
    if not item.startswith('__'):
        print(item)

# 8. 커스텀 모듈 생성
# 사용자 정의 모듈을 만드는 방법을 보여줍니다.
print("\n=== 8. 커스텀 모듈 생성 ===")

# mymath.py 모듈 생성
with open("mymath.py", "w") as f:
    f.write("""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b
""")

# 커스텀 모듈 임포트
import mymath
print(f"더하기: {mymath.add(5, 3)}")
print(f"빼기: {mymath.subtract(5, 3)}")
print(f"곱하기: {mymath.multiply(5, 3)}")
print(f"나누기: {mymath.divide(6, 2)}")

# 9. 패키지 구조
# 파이썬 패키지의 구조를 보여줍니다.
print("\n=== 9. 패키지 구조 ===")

# mypackage 패키지 생성
import os
os.makedirs("mypackage", exist_ok=True)

# __init__.py 파일 생성
with open("mypackage/__init__.py", "w") as f:
    f.write("""
# 패키지 초기화 파일
print("mypackage 패키지가 임포트되었습니다.")
""")

# module1.py 파일 생성
with open("mypackage/module1.py", "w") as f:
    f.write("""
def function1():
    return "module1의 function1이 호출되었습니다."
""")

# module2.py 파일 생성
with open("mypackage/module2.py", "w") as f:
    f.write("""
def function2():
    return "module2의 function2가 호출되었습니다."
""")

# 패키지 임포트
import mypackage
from mypackage import module1, module2

print(module1.function1())
print(module2.function2())

print("\n프로그램 종료") 