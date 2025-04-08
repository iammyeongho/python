# 파이썬 테스트와 디버깅

# 1. 단위 테스트 (unittest)
print("=== 단위 테스트 (unittest) ===")

import unittest

class Calculator:
    """계산기 클래스"""
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y == 0:
            raise ValueError("0으로 나눌 수 없습니다.")
        return x / y

class TestCalculator(unittest.TestCase):
    """계산기 테스트 클래스"""
    def setUp(self):
        """테스트 설정"""
        self.calc = Calculator()
    
    def test_add(self):
        """덧셈 테스트"""
        self.assertEqual(self.calc.add(3, 5), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
    
    def test_subtract(self):
        """뺄셈 테스트"""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
    
    def test_multiply(self):
        """곱셈 테스트"""
        self.assertEqual(self.calc.multiply(3, 5), 15)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -2), 4)
    
    def test_divide(self):
        """나눗셈 테스트"""
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(-6, 2), -3)
        
        # 예외 테스트
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

# 테스트 실행
if __name__ == '__main__':
    unittest.main()

# 2. pytest 사용
print("\n=== pytest 사용 ===")

"""
# test_calculator.py
import pytest
from calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(3, 5) == 8
    assert calculator.add(-1, 1) == 0
    assert calculator.add(-1, -1) == -2

def test_subtract(calculator):
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(1, 1) == 0
    assert calculator.subtract(-1, -1) == 0

def test_multiply(calculator):
    assert calculator.multiply(3, 5) == 15
    assert calculator.multiply(-2, 3) == -6
    assert calculator.multiply(-2, -2) == 4

def test_divide(calculator):
    assert calculator.divide(6, 2) == 3
    assert calculator.divide(5, 2) == 2.5
    assert calculator.divide(-6, 2) == -3
    
    with pytest.raises(ValueError):
        calculator.divide(5, 0)

# 실행: pytest test_calculator.py
"""

# 3. 디버깅 기법
print("\n=== 디버깅 기법 ===")

import pdb
import logging

# 로깅 설정
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def complex_calculation(x, y):
    """복잡한 계산 함수"""
    logger.debug(f"입력값: x={x}, y={y}")
    
    # 중간 결과 로깅
    result = x * y
    logger.debug(f"곱셈 결과: {result}")
    
    # 조건부 디버깅
    if result > 100:
        logger.warning(f"결과가 100을 초과합니다: {result}")
    
    # pdb를 사용한 디버깅
    # pdb.set_trace()
    
    return result

# 디버깅 예제 실행
try:
    result = complex_calculation(10, 15)
    print(f"계산 결과: {result}")
except Exception as e:
    logger.error(f"오류 발생: {e}", exc_info=True)

# 4. 코드 품질 관리
print("\n=== 코드 품질 관리 ===")

"""
# pylint 설정
# .pylintrc
[MASTER]
ignore=CVS
persistent=yes
load-plugins=

[MESSAGES CONTROL]
disable=C0111,C0103

[FORMAT]
max-line-length=120

# black 설정
# pyproject.toml
[tool.black]
line-length = 120
include = '\.pyi?$'

# 실행 명령
# pylint your_file.py
# black your_file.py
"""

# 5. 프로파일링
print("\n=== 프로파일링 ===")

import cProfile
import pstats
from pstats import SortKey

def fibonacci(n):
    """피보나치 수열 계산"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 프로파일링 실행
def profile_fibonacci():
    """피보나치 함수 프로파일링"""
    profiler = cProfile.Profile()
    profiler.enable()
    
    # 함수 실행
    result = fibonacci(30)
    print(f"피보나치(30) = {result}")
    
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats(SortKey.TIME)
    stats.print_stats()

# 프로파일링 실행
profile_fibonacci()

# 6. 메모리 프로파일링
print("\n=== 메모리 프로파일링 ===")

"""
# memory_profiler 설치 필요: pip install memory_profiler

from memory_profiler import profile

@profile
def memory_intensive_function():
    # 대용량 데이터 생성
    data = [i for i in range(1000000)]
    return sum(data)

# 실행: python -m memory_profiler your_script.py
"""

# 7. 테스트 커버리지
print("\n=== 테스트 커버리지 ===")

"""
# coverage 설치 필요: pip install coverage

# 테스트 실행 및 커버리지 측정
# coverage run -m unittest test_calculator.py
# coverage report
# coverage html  # HTML 리포트 생성
"""

print("\n프로그램 종료") 