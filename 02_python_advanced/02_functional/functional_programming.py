"""
PHP와 Python의 함수형 프로그래밍 비교
이 파일은 PHP 개발자가 Python의 함수형 프로그래밍을 이해하는 데 도움을 주기 위한 예제입니다.
"""

from typing import List, Callable, Any, Dict
from functools import reduce, partial
from operator import add, mul
import math

class FunctionalProgrammingExamples:
    """함수형 프로그래밍 예제 클래스"""

    def __init__(self):
        self.numbers: List[int] = [1, 2, 3, 4, 5]
        self.names: List[str] = ["John", "Jane", "Doe", "Alice", "Bob"]

    def map_example(self) -> None:
        """map 함수 예제 (PHP의 array_map과 유사)"""
        print("\n=== Map Example ===")
        
        # 기본 map 사용 (PHP: array_map(function($x) { return $x * 2; }, $array))
        doubled = list(map(lambda x: x * 2, self.numbers))
        print(f"Doubled numbers: {doubled}")
        
        # 리스트 컴프리헨션으로 동일한 작업
        doubled_comp = [x * 2 for x in self.numbers]
        print(f"Doubled numbers (comprehension): {doubled_comp}")

    def filter_example(self) -> None:
        """filter 함수 예제 (PHP의 array_filter와 유사)"""
        print("\n=== Filter Example ===")
        
        # 기본 filter 사용 (PHP: array_filter($array, function($x) { return $x > 3; }))
        evens = list(filter(lambda x: x % 2 == 0, self.numbers))
        print(f"Even numbers: {evens}")
        
        # 리스트 컴프리헨션으로 동일한 작업
        evens_comp = [x for x in self.numbers if x % 2 == 0]
        print(f"Even numbers (comprehension): {evens_comp}")

    def reduce_example(self) -> None:
        """reduce 함수 예제 (PHP의 array_reduce와 유사)"""
        print("\n=== Reduce Example ===")
        
        # 기본 reduce 사용 (PHP: array_reduce($array, function($carry, $item) { return $carry + $item; }, 0))
        sum_result = reduce(lambda x, y: x + y, self.numbers)
        print(f"Sum of numbers: {sum_result}")
        
        # operator 모듈 사용
        sum_operator = reduce(add, self.numbers)
        print(f"Sum using operator: {sum_operator}")
        
        # 곱셈 예제
        product = reduce(mul, self.numbers)
        print(f"Product of numbers: {product}")

    def lambda_example(self) -> None:
        """람다 함수 예제 (PHP의 익명 함수와 유사)"""
        print("\n=== Lambda Example ===")
        
        # 기본 람다 사용
        square = lambda x: x ** 2
        print(f"Square of 5: {square(5)}")
        
        # 람다를 map과 함께 사용
        squares = list(map(lambda x: x ** 2, self.numbers))
        print(f"Squares: {squares}")

    def partial_example(self) -> None:
        """partial 함수 예제 (PHP의 클로저와 유사)"""
        print("\n=== Partial Example ===")
        
        # 기본 partial 사용
        def power(base: float, exponent: float) -> float:
            return base ** exponent
        
        square = partial(power, exponent=2)
        cube = partial(power, exponent=3)
        
        print(f"Square of 5: {square(5)}")
        print(f"Cube of 5: {cube(5)}")

    def decorator_example(self) -> None:
        """데코레이터 예제 (PHP의 트레이트와 유사)"""
        print("\n=== Decorator Example ===")
        
        def timer(func: Callable) -> Callable:
            """함수 실행 시간을 측정하는 데코레이터"""
            def wrapper(*args, **kwargs):
                import time
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                print(f"Function {func.__name__} took {end - start:.6f} seconds")
                return result
            return wrapper
        
        @timer
        def slow_function(n: int) -> int:
            """느린 계산을 수행하는 함수"""
            result = 0
            for i in range(n):
                result += i
            return result
        
        print(f"Result: {slow_function(1000000)}")

    def generator_example(self) -> None:
        """제너레이터 예제 (PHP의 제너레이터와 유사)"""
        print("\n=== Generator Example ===")
        
        def fibonacci(n: int):
            """피보나치 수열을 생성하는 제너레이터"""
            a, b = 0, 1
            for _ in range(n):
                yield a
                a, b = b, a + b
        
        # 제너레이터 사용
        fib = fibonacci(10)
        print(f"First 10 Fibonacci numbers: {list(fib)}")
        
        # 제너레이터 표현식
        squares = (x ** 2 for x in self.numbers)
        print(f"Squares using generator: {list(squares)}")

    def composition_example(self) -> None:
        """함수 합성 예제"""
        print("\n=== Function Composition Example ===")
        
        def add_one(x: int) -> int:
            return x + 1
        
        def multiply_by_two(x: int) -> int:
            return x * 2
        
        # 함수 합성
        def compose(f: Callable, g: Callable) -> Callable:
            return lambda x: f(g(x))
        
        add_then_multiply = compose(multiply_by_two, add_one)
        print(f"Add 1 then multiply by 2 (5): {add_then_multiply(5)}")

def main():
    """메인 함수"""
    examples = FunctionalProgrammingExamples()
    
    # 각 함수형 프로그래밍 예제 실행
    examples.map_example()
    examples.filter_example()
    examples.reduce_example()
    examples.lambda_example()
    examples.partial_example()
    examples.decorator_example()
    examples.generator_example()
    examples.composition_example()

if __name__ == "__main__":
    main() 