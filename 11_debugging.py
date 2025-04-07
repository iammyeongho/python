# 파이썬 디버깅 방법

# 1. print 디버깅
print("=== print 디버깅 예제 ===")

def calculate_factorial(n):
    print(f"함수 시작: n = {n}")  # 디버깅용 print
    result = 1
    for i in range(1, n + 1):
        result *= i
        print(f"i = {i}, result = {result}")  # 디버깅용 print
    print(f"함수 종료: 결과 = {result}")  # 디버깅용 print
    return result

print(calculate_factorial(5))

# 2. pdb 디버거 사용
print("\n=== pdb 디버거 예제 ===")

"""
import pdb

def complex_function(x, y):
    z = x + y
    pdb.set_trace()  # 디버거 중단점 설정
    result = z * 2
    return result

# 실행 방법:
# 1. 이 파일을 실행하면 pdb 프롬프트가 나타납니다
# 2. pdb 명령어:
#    - n(next): 다음 줄로 이동
#    - s(step): 함수 내부로 들어가기
#    - c(continue): 다음 중단점까지 실행
#    - p 변수명: 변수 값 출력
#    - l(list): 현재 위치 주변 코드 보기
#    - q(quit): 디버거 종료
#    - h(help): 도움말 보기

# complex_function(10, 20)
"""

# 3. logging 모듈을 이용한 디버깅
print("\n=== logging 디버깅 예제 ===")

import logging

# 로깅 설정
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='debug.log'
)

def process_data(data):
    logging.debug(f"함수 시작: 입력 데이터 = {data}")
    
    if not data:
        logging.warning("빈 데이터가 입력되었습니다.")
        return None
    
    try:
        result = sum(data) / len(data)
        logging.info(f"계산 완료: 결과 = {result}")
        return result
    except Exception as e:
        logging.error(f"오류 발생: {e}", exc_info=True)
        return None

# 로깅 테스트
process_data([1, 2, 3, 4, 5])
process_data([])
process_data("문자열")  # 타입 오류 발생

# 4. assert 문을 이용한 디버깅
print("\n=== assert 디버깅 예제 ===")

def divide(a, b):
    assert b != 0, "0으로 나눌 수 없습니다."
    assert isinstance(a, (int, float)) and isinstance(b, (int, float)), "숫자만 입력해주세요."
    return a / b

try:
    print(divide(10, 2))  # 정상 동작
    print(divide(10, 0))  # AssertionError 발생
except AssertionError as e:
    print(f"AssertionError: {e}")

# 5. 디버깅 데코레이터
print("\n=== 디버깅 데코레이터 예제 ===")

import functools
import time

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"함수 호출: {func.__name__}({args}, {kwargs})")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"함수 종료: {func.__name__}, 결과: {result}, 소요 시간: {end_time - start_time:.4f}초")
        return result
    return wrapper

@debug
def add(a, b):
    return a + b

print(add(3, 5))

# 6. 예외 처리와 디버깅
print("\n=== 예외 처리와 디버깅 예제 ===")

import traceback

def risky_operation():
    try:
        # 의도적으로 오류 발생
        result = 10 / 0
        return result
    except ZeroDivisionError:
        print("0으로 나누기 오류 발생")
        # 스택 트레이스 출력
        traceback.print_exc()
        return None
    except Exception as e:
        print(f"예상치 못한 오류 발생: {e}")
        traceback.print_exc()
        return None

risky_operation()

# 7. 디버깅을 위한 커스텀 예외
print("\n=== 커스텀 예외 디버깅 예제 ===")

class ValidationError(Exception):
    def __init__(self, message, value=None):
        self.message = message
        self.value = value
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.message} (값: {self.value})"

def validate_age(age):
    if not isinstance(age, int):
        raise ValidationError("나이는 정수여야 합니다.", age)
    if age < 0:
        raise ValidationError("나이는 음수일 수 없습니다.", age)
    if age > 150:
        raise ValidationError("나이가 너무 큽니다.", age)
    return True

try:
    validate_age(-5)
except ValidationError as e:
    print(f"검증 오류: {e}")

# 8. 디버깅 도구: cProfile
print("\n=== cProfile 디버깅 예제 ===")

"""
import cProfile
import pstats

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 프로파일링 실행
# cProfile.run('fibonacci(30)')

# 결과를 파일로 저장하고 분석
# profiler = cProfile.Profile()
# profiler.enable()
# fibonacci(30)
# profiler.disable()
# stats = pstats.Stats(profiler).sort_stats('cumulative')
# stats.print_stats()
# stats.dump_stats('fibonacci_profile.prof')
"""

# 9. 디버깅 도구: line_profiler
print("\n=== line_profiler 디버깅 예제 ===")

"""
# line_profiler 설치 필요: pip install line_profiler

from line_profiler import LineProfiler

def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

# 프로파일링 실행
# profiler = LineProfiler()
# profiler.add_function(slow_function)
# profiler.run('slow_function()')
# profiler.print_stats()
"""

# 10. 디버깅 도구: memory_profiler
print("\n=== memory_profiler 디버깅 예제 ===")

"""
# memory_profiler 설치 필요: pip install memory_profiler

from memory_profiler import profile

@profile
def memory_intensive_function():
    large_list = [i for i in range(1000000)]
    return sum(large_list)

# 메모리 프로파일링 실행
# memory_intensive_function()
""" 