"""
이터레이터와 관련된 예제
이 파일은 이터레이터의 개념과 사용법을 다룹니다.
"""

from typing import Iterator, List, Any
from collections.abc import Iterable

class IteratorExamples:
    """이터레이터 예제 클래스"""

    def __init__(self):
        self.numbers: List[int] = [1, 2, 3, 4, 5]

    def basic_iterator(self) -> None:
        """기본 이터레이터 예제"""
        print("\n=== Basic Iterator ===")
        
        class CountDown:
            def __init__(self, start: int):
                self.start = start

            def __iter__(self) -> Iterator[int]:
                return self

            def __next__(self) -> int:
                if self.start <= 0:
                    raise StopIteration
                current = self.start
                self.start -= 1
                return current

        # 카운트다운 이터레이터 사용
        for number in CountDown(5):
            print(number)

    def custom_iterator(self) -> None:
        """커스텀 이터레이터 예제"""
        print("\n=== Custom Iterator ===")
        
        class Fibonacci:
            def __init__(self, limit: int):
                self.limit = limit
                self.a, self.b = 0, 1
                self.count = 0

            def __iter__(self) -> Iterator[int]:
                return self

            def __next__(self) -> int:
                if self.count >= self.limit:
                    raise StopIteration
                result = self.a
                self.a, self.b = self.b, self.a + self.b
                self.count += 1
                return result

        # 피보나치 이터레이터 사용
        for number in Fibonacci(10):
            print(number)

    def iterator_protocol(self) -> None:
        """이터레이터 프로토콜 예제"""
        print("\n=== Iterator Protocol ===")
        
        class Range:
            def __init__(self, start: int, stop: int, step: int = 1):
                self.start = start
                self.stop = stop
                self.step = step

            def __iter__(self) -> Iterator[int]:
                return RangeIterator(self.start, self.stop, self.step)

        class RangeIterator:
            def __init__(self, start: int, stop: int, step: int):
                self.current = start
                self.stop = stop
                self.step = step

            def __iter__(self) -> Iterator[int]:
                return self

            def __next__(self) -> int:
                if self.current >= self.stop:
                    raise StopIteration
                result = self.current
                self.current += self.step
                return result

        # 커스텀 Range 클래스 사용
        for number in Range(1, 10, 2):
            print(number)

    def iterator_tools(self) -> None:
        """이터레이터 도구 예제"""
        print("\n=== Iterator Tools ===")
        
        # 이터레이터 도구 사용
        numbers_iter = iter(self.numbers)
        print("First number:", next(numbers_iter))
        print("Second number:", next(numbers_iter))
        
        # 이터레이터 소진 확인
        remaining = list(numbers_iter)
        print("Remaining numbers:", remaining)

def main():
    """메인 함수"""
    examples = IteratorExamples()
    
    # 이터레이터 예제 실행
    examples.basic_iterator()
    examples.custom_iterator()
    examples.iterator_protocol()
    examples.iterator_tools()

if __name__ == "__main__":
    main() 