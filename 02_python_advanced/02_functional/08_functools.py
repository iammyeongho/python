"""
functools 모듈과 관련된 예제
이 파일은 functools 모듈의 기능과 사용법을 다룹니다.
"""

from typing import List, Callable, Any
from functools import partial, reduce, wraps, lru_cache, total_ordering
import time

class FunctoolsExamples:
    """functools 모듈 예제 클래스"""

    def __init__(self):
        self.numbers: List[int] = [1, 2, 3, 4, 5]

    def partial_example(self) -> None:
        """partial 함수 예제"""
        print("\n=== Partial Function ===")
        
        # 기본 함수
        def power(base: int, exponent: int) -> int:
            return base ** exponent
        
        # 제곱 함수 생성
        square = partial(power, exponent=2)
        cube = partial(power, exponent=3)
        
        print(f"Square of 5: {square(5)}")
        print(f"Cube of 3: {cube(3)}")

    def reduce_example(self) -> None:
        """reduce 함수 예제"""
        print("\n=== Reduce Function ===")
        
        # 숫자 합계 계산
        sum_result = reduce(lambda x, y: x + y, self.numbers)
        print(f"Sum of numbers: {sum_result}")
        
        # 최대값 찾기
        max_result = reduce(lambda x, y: x if x > y else y, self.numbers)
        print(f"Maximum number: {max_result}")

    def wraps_example(self) -> None:
        """wraps 데코레이터 예제"""
        print("\n=== Wraps Decorator ===")
        
        def timer(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args, **kwargs):
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
                return result
            return wrapper

        @timer
        def slow_function():
            time.sleep(1)
            return "Done!"

        print(slow_function())
        print(f"Function name: {slow_function.__name__}")

    def lru_cache_example(self) -> None:
        """lru_cache 데코레이터 예제"""
        print("\n=== LRU Cache ===")
        
        @lru_cache(maxsize=32)
        def fibonacci(n: int) -> int:
            if n <= 1:
                return n
            return fibonacci(n - 1) + fibonacci(n - 2)

        # 첫 번째 실행 (캐시 미스)
        start_time = time.time()
        result = fibonacci(30)
        end_time = time.time()
        print(f"First run: {result} (took {end_time - start_time:.4f} seconds)")

        # 두 번째 실행 (캐시 히트)
        start_time = time.time()
        result = fibonacci(30)
        end_time = time.time()
        print(f"Second run: {result} (took {end_time - start_time:.4f} seconds)")

    def total_ordering_example(self) -> None:
        """total_ordering 데코레이터 예제"""
        print("\n=== Total Ordering ===")
        
        @total_ordering
        class Person:
            def __init__(self, name: str, age: int):
                self.name = name
                self.age = age

            def __eq__(self, other):
                return self.age == other.age

            def __lt__(self, other):
                return self.age < other.age

        # Person 객체 생성
        alice = Person("Alice", 25)
        bob = Person("Bob", 30)
        charlie = Person("Charlie", 25)

        # 비교 연산자 사용
        print(f"Alice == Charlie: {alice == charlie}")
        print(f"Alice < Bob: {alice < bob}")
        print(f"Bob > Alice: {bob > alice}")
        print(f"Alice <= Charlie: {alice <= charlie}")

def main():
    """메인 함수"""
    examples = FunctoolsExamples()
    
    # functools 예제 실행
    examples.partial_example()
    examples.reduce_example()
    examples.wraps_example()
    examples.lru_cache_example()
    examples.total_ordering_example()

if __name__ == "__main__":
    main() 