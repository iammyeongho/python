# 파이썬 모듈과 패키지

# 1. 기본 모듈 사용
print("=== 기본 모듈 사용 ===")

# 수학 모듈 사용
import math

print(f"파이(π) 값: {math.pi}")
print(f"5의 제곱근: {math.sqrt(25)}")
print(f"3.7의 올림: {math.ceil(3.7)}")
print(f"3.7의 내림: {math.floor(3.7)}")
print(f"3.7의 반올림: {round(3.7)}")

# 랜덤 모듈 사용
import random

print(f"\n랜덤 정수 (1-10): {random.randint(1, 10)}")
print(f"랜덤 실수 (0-1): {random.random()}")
print(f"랜덤 선택: {random.choice(['사과', '바나나', '오렌지'])}")

# 날짜/시간 모듈 사용
import datetime

now = datetime.datetime.now()
print(f"\n현재 날짜/시간: {now}")
print(f"연도: {now.year}")
print(f"월: {now.month}")
print(f"일: {now.day}")
print(f"시간: {now.hour}")
print(f"분: {now.minute}")
print(f"초: {now.second}")

# 2. 모듈 별칭 사용
print("\n=== 모듈 별칭 사용 ===")

import math as m
import random as r
import datetime as dt

print(f"파이(π) 값: {m.pi}")
print(f"랜덤 정수 (1-10): {r.randint(1, 10)}")
print(f"현재 날짜/시간: {dt.datetime.now()}")

# 3. 모듈에서 특정 항목만 가져오기
print("\n=== 모듈에서 특정 항목만 가져오기 ===")

from math import pi, sqrt, ceil, floor
from random import randint, choice
from datetime import datetime

print(f"파이(π) 값: {pi}")
print(f"25의 제곱근: {sqrt(25)}")
print(f"3.7의 올림: {ceil(3.7)}")
print(f"3.7의 내림: {floor(3.7)}")
print(f"랜덤 정수 (1-10): {randint(1, 10)}")
print(f"랜덤 선택: {choice(['사과', '바나나', '오렌지'])}")
print(f"현재 날짜/시간: {datetime.now()}")

# 4. 모든 항목 가져오기 (권장하지 않음)
print("\n=== 모든 항목 가져오기 (권장하지 않음) ===")

# 주의: 이 방식은 권장되지 않습니다. 이름 충돌이 발생할 수 있습니다.
from math import *

print(f"파이(π) 값: {pi}")
print(f"25의 제곱근: {sqrt(25)}")
print(f"3.7의 올림: {ceil(3.7)}")
print(f"3.7의 내림: {floor(3.7)}")

# 5. 모듈 검색 경로
print("\n=== 모듈 검색 경로 ===")

import sys

print("모듈 검색 경로:")
for path in sys.path:
    print(f"- {path}")

# 6. 사용자 정의 모듈
print("\n=== 사용자 정의 모듈 ===")

# 이 파일과 같은 디렉토리에 있는 모듈을 가져옵니다.
# 실제로는 별도의 파일로 만들어야 합니다.

# utils.py 파일을 생성합니다.
with open("utils.py", "w", encoding="utf-8") as f:
    f.write("""# 유틸리티 함수 모듈

def greet(name):
    \"\"\"인사 함수\"\"\"
    return f"안녕하세요, {name}님!"

def calculate_average(numbers):
    \"\"\"평균 계산 함수\"\"\"
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def is_palindrome(text):
    \"\"\"회문 검사 함수\"\"\"
    text = text.lower().replace(" ", "")
    return text == text[::-1]

# 모듈 레벨 변수
PI = 3.14159
MAX_RETRIES = 3
""")

# utils 모듈 가져오기
import utils

print(utils.greet("홍길동"))
print(f"평균: {utils.calculate_average([1, 2, 3, 4, 5])}")
print(f"'토마토'는 회문인가요? {utils.is_palindrome('토마토')}")
print(f"PI 값: {utils.PI}")

# 7. 패키지
print("\n=== 패키지 ===")

# 패키지 구조를 생성합니다.
# 실제로는 별도의 디렉토리로 만들어야 합니다.

# mypackage 디렉토리 생성
import os
os.makedirs("mypackage", exist_ok=True)

# __init__.py 파일 생성 (패키지 선언)
with open("mypackage/__init__.py", "w", encoding="utf-8") as f:
    f.write("""# mypackage 패키지

# 패키지 레벨 변수
VERSION = "1.0.0"
AUTHOR = "홍길동"

# 패키지 초기화 시 실행할 코드
print("mypackage 패키지가 로드되었습니다.")
""")

# submodule1.py 파일 생성
with open("mypackage/submodule1.py", "w", encoding="utf-8") as f:
    f.write("""# 서브모듈 1

def function1():
    \"\"\"서브모듈 1의 함수\"\"\"
    return "서브모듈 1의 함수가 호출되었습니다."

# 서브모듈 레벨 변수
VALUE1 = 100
""")

# submodule2.py 파일 생성
with open("mypackage/submodule2.py", "w", encoding="utf-8") as f:
    f.write("""# 서브모듈 2

def function2():
    \"\"\"서브모듈 2의 함수\"\"\"
    return "서브모듈 2의 함수가 호출되었습니다."

# 서브모듈 레벨 변수
VALUE2 = 200
""")

# 패키지 사용
import mypackage
from mypackage import submodule1, submodule2

print(f"패키지 버전: {mypackage.VERSION}")
print(f"패키지 작성자: {mypackage.AUTHOR}")
print(submodule1.function1())
print(submodule2.function2())
print(f"서브모듈 1의 값: {submodule1.VALUE1}")
print(f"서브모듈 2의 값: {submodule2.VALUE2}")

# 8. 패키지에서 특정 항목 가져오기
print("\n=== 패키지에서 특정 항목 가져오기 ===")

from mypackage.submodule1 import function1, VALUE1
from mypackage.submodule2 import function2, VALUE2

print(function1())
print(function2())
print(f"VALUE1: {VALUE1}")
print(f"VALUE2: {VALUE2}")

# 9. 패키지 내 상대 가져오기
print("\n=== 패키지 내 상대 가져오기 ===")

# submodule3.py 파일 생성 (상대 가져오기 예제)
with open("mypackage/submodule3.py", "w", encoding="utf-8") as f:
    f.write("""# 서브모듈 3 (상대 가져오기 예제)

# 상대 가져오기 (실제로는 이렇게 동작합니다)
# from .submodule1 import function1
# from .submodule2 import function2

def function3():
    \"\"\"서브모듈 3의 함수\"\"\"
    # 실제로는 이렇게 사용합니다
    # return f"{function1()} 그리고 {function2()}"
    return "서브모듈 3의 함수가 호출되었습니다."

# 서브모듈 레벨 변수
VALUE3 = 300
""")

# 서브모듈 3 사용
from mypackage import submodule3

print(submodule3.function3())
print(f"VALUE3: {submodule3.VALUE3}")

# 10. 패키지 실행
print("\n=== 패키지 실행 ===")

# __main__.py 파일 생성 (패키지 실행 예제)
with open("mypackage/__main__.py", "w", encoding="utf-8") as f:
    f.write("""# 패키지 메인 모듈

def main():
    \"\"\"패키지 메인 함수\"\"\"
    print("패키지가 직접 실행되었습니다.")
    from mypackage import submodule1, submodule2, submodule3
    
    print(submodule1.function1())
    print(submodule2.function2())
    print(submodule3.function3())
    
    print(f"VERSION: {__import__('mypackage').VERSION}")

if __name__ == "__main__":
    main()
""")

# 패키지 실행 시뮬레이션
print("패키지 실행 시뮬레이션:")
import importlib.util
spec = importlib.util.spec_from_file_location("__main__", "mypackage/__main__.py")
main_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(main_module)

# 11. 모듈 리로딩
print("\n=== 모듈 리로딩 ===")

# 모듈 리로딩 예제
import importlib

# utils 모듈 리로딩
importlib.reload(utils)
print("utils 모듈이 리로드되었습니다.")

# 12. 모듈 검사
print("\n=== 모듈 검사 ===")

# 모듈 속성 검사
print("utils 모듈 속성:")
for attr in dir(utils):
    if not attr.startswith("__"):
        print(f"- {attr}")

# 모듈 문서 검사
print("\nutils 모듈 문서:")
print(utils.__doc__)

# 13. 모듈 생성
print("\n=== 모듈 생성 ===")

# 동적으로 모듈 생성
module_code = """
def dynamic_function():
    return "이 함수는 동적으로 생성되었습니다."

DYNAMIC_VALUE = 42
"""

# 모듈 생성
import types
dynamic_module = types.ModuleType("dynamic_module")
exec(module_code, dynamic_module.__dict__)

# 동적 모듈 사용
print(dynamic_module.dynamic_function())
print(f"DYNAMIC_VALUE: {dynamic_module.DYNAMIC_VALUE}")

# 14. 패키지 배포 준비
print("\n=== 패키지 배포 준비 ===")

# setup.py 파일 생성 예제
with open("setup_example.py", "w", encoding="utf-8") as f:
    f.write("""# setup.py 예제

from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="1.0.0",
    author="홍길동",
    author_email="example@example.com",
    description="패키지 설명",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/username/mypackage",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
""")

print("setup.py 파일이 생성되었습니다.")

# 15. 가상 환경
print("\n=== 가상 환경 ===")

print("가상 환경 생성 및 활성화 명령어 예제:")
print("생성: python -m venv myenv")
print("활성화 (Windows): myenv\\Scripts\\activate")
print("활성화 (Linux/Mac): source myenv/bin/activate")
print("비활성화: deactivate")

print("\n프로그램 종료") 