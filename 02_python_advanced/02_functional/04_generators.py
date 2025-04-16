"""
제너레이터와 관련된 예제
이 파일은 제너레이터의 개념과 사용법을 다룹니다.
"""

from typing import Generator, Iterator
import time

class GeneratorExamples:
    """제너레이터 예제 클래스"""

    def __init__(self):
        pass

    def basic_generator(self) -> None:
        """기본 제너레이터 예제"""
        print("\n=== Basic Generator ===")
        
        def count_up_to(n: int) -> Generator[int, None, None]:
            i = 1
            while i <= n:
                yield i
                i += 1

        for number in count_up_to(5):
            print(number)

    def infinite_generator(self) -> None:
        """무한 제너레이터 예제"""
        print("\n=== Infinite Generator ===")
        
        def fibonacci() -> Generator[int, None, None]:
            a, b = 0, 1
            while True:
                yield a
                a, b = b, a + b

        fib = fibonacci()
        for _ in range(10):
            print(next(fib))

    def generator_expression(self) -> None:
        """제너레이터 표현식 예제"""
        print("\n=== Generator Expression ===")
        
        # 제너레이터 표현식
        squares = (x ** 2 for x in range(5))
        print("Squares:", list(squares))

        # 필터링과 함께 사용
        even_squares = (x ** 2 for x in range(10) if x % 2 == 0)
        print("Even squares:", list(even_squares))

    def generator_pipeline(self) -> None:
        """제너레이터 파이프라인 예제"""
        print("\n=== Generator Pipeline ===")
        
        def numbers():
            for i in range(5):
                print(f"Generating {i}")
                yield i

        def square(nums: Iterator[int]) -> Generator[int, None, None]:
            for num in nums:
                print(f"Squaring {num}")
                yield num ** 2

        def add_one(nums: Iterator[int]) -> Generator[int, None, None]:
            for num in nums:
                print(f"Adding one to {num}")
                yield num + 1

        # 파이프라인 구성
        pipeline = add_one(square(numbers()))
        print("Pipeline result:", list(pipeline))

    def generator_with_send(self) -> None:
        """send 메서드를 사용하는 제너레이터 예제"""
        print("\n=== Generator with Send ===")
        
        def accumulator() -> Generator[int, int, None]:
            total = 0
            while True:
                value = yield total
                if value is None:
                    break
                total += value

        acc = accumulator()
        next(acc)  # 제너레이터 시작
        print(acc.send(1))  # 1
        print(acc.send(2))  # 3
        print(acc.send(3))  # 6

def main():
    """메인 함수"""
    examples = GeneratorExamples()
    
    # 제너레이터 예제 실행
    examples.basic_generator()
    examples.infinite_generator()
    examples.generator_expression()
    examples.generator_pipeline()
    examples.generator_with_send()

if __name__ == "__main__":
    main() 