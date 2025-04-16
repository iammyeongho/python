"""
고차 함수와 관련된 예제
이 파일은 고차 함수의 개념과 사용법을 다룹니다.
"""

from typing import List, Callable, Any
from functools import reduce

class HigherOrderFunctions:
    """고차 함수 예제 클래스"""

    def __init__(self):
        self.numbers: List[int] = [1, 2, 3, 4, 5]
        self.names: List[str] = ["John", "Jane", "Doe", "Alice", "Bob"]

    def map_example(self) -> None:
        """map 함수 예제"""
        print("\n=== Map Function ===")
        
        # 제곱 계산
        squares = list(map(lambda x: x ** 2, self.numbers))
        print(f"Squares: {squares}")
        
        # 이름 대문자로 변환
        upper_names = list(map(str.upper, self.names))
        print(f"Upper names: {upper_names}")

    def filter_example(self) -> None:
        """filter 함수 예제"""
        print("\n=== Filter Function ===")
        
        # 짝수 필터링
        evens = list(filter(lambda x: x % 2 == 0, self.numbers))
        print(f"Even numbers: {evens}")
        
        # 'J'로 시작하는 이름 필터링
        j_names = list(filter(lambda name: name.startswith('J'), self.names))
        print(f"Names starting with 'J': {j_names}")

    def reduce_example(self) -> None:
        """reduce 함수 예제"""
        print("\n=== Reduce Function ===")
        
        # 숫자 합계 계산
        sum_result = reduce(lambda x, y: x + y, self.numbers)
        print(f"Sum of numbers: {sum_result}")
        
        # 최대값 찾기
        max_result = reduce(lambda x, y: x if x > y else y, self.numbers)
        print(f"Maximum number: {max_result}")

    def function_composition(self) -> None:
        """함수 합성 예제"""
        print("\n=== Function Composition ===")
        
        def add_one(x: int) -> int:
            return x + 1
        
        def square(x: int) -> int:
            return x ** 2
        
        # 함수 합성
        composed = lambda x: square(add_one(x))
        result = list(map(composed, self.numbers))
        print(f"Composed function result: {result}")

def main():
    """메인 함수"""
    examples = HigherOrderFunctions()
    
    # 고차 함수 예제 실행
    examples.map_example()
    examples.filter_example()
    examples.reduce_example()
    examples.function_composition()

if __name__ == "__main__":
    main() 