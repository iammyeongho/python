"""
람다 함수와 관련된 예제
이 파일은 람다 함수의 개념과 사용법을 다룹니다.
"""

from typing import List, Callable, Any
from functools import reduce

class LambdaExamples:
    """람다 함수 예제 클래스"""

    def __init__(self):
        self.numbers: List[int] = [1, 2, 3, 4, 5]
        self.names: List[str] = ["John", "Jane", "Doe", "Alice", "Bob"]

    def basic_lambda(self) -> None:
        """기본 람다 함수 예제"""
        print("\n=== Basic Lambda ===")
        
        # 기본 람다 함수
        square = lambda x: x ** 2
        print(f"Square of 5: {square(5)}")
        
        # 여러 매개변수
        add = lambda x, y: x + y
        print(f"Add 3 and 4: {add(3, 4)}")

    def lambda_with_map(self) -> None:
        """map과 함께 사용하는 람다 함수 예제"""
        print("\n=== Lambda with Map ===")
        
        # 제곱 계산
        squares = list(map(lambda x: x ** 2, self.numbers))
        print(f"Squares: {squares}")
        
        # 이름 길이 계산
        lengths = list(map(lambda name: len(name), self.names))
        print(f"Name lengths: {lengths}")

    def lambda_with_filter(self) -> None:
        """filter와 함께 사용하는 람다 함수 예제"""
        print("\n=== Lambda with Filter ===")
        
        # 짝수 필터링
        evens = list(filter(lambda x: x % 2 == 0, self.numbers))
        print(f"Even numbers: {evens}")
        
        # 'J'로 시작하는 이름 필터링
        j_names = list(filter(lambda name: name.startswith('J'), self.names))
        print(f"Names starting with 'J': {j_names}")

    def lambda_with_reduce(self) -> None:
        """reduce와 함께 사용하는 람다 함수 예제"""
        print("\n=== Lambda with Reduce ===")
        
        # 숫자 합계 계산
        sum_result = reduce(lambda x, y: x + y, self.numbers)
        print(f"Sum of numbers: {sum_result}")
        
        # 최대값 찾기
        max_result = reduce(lambda x, y: x if x > y else y, self.numbers)
        print(f"Maximum number: {max_result}")

    def lambda_with_sort(self) -> None:
        """정렬과 함께 사용하는 람다 함수 예제"""
        print("\n=== Lambda with Sort ===")
        
        # 이름 길이로 정렬
        sorted_names = sorted(self.names, key=lambda name: len(name))
        print(f"Names sorted by length: {sorted_names}")
        
        # 숫자를 문자열로 변환하여 정렬
        sorted_numbers = sorted(self.numbers, key=lambda x: str(x))
        print(f"Numbers sorted as strings: {sorted_numbers}")

def main():
    """메인 함수"""
    examples = LambdaExamples()
    
    # 람다 함수 예제 실행
    examples.basic_lambda()
    examples.lambda_with_map()
    examples.lambda_with_filter()
    examples.lambda_with_reduce()
    examples.lambda_with_sort()

if __name__ == "__main__":
    main() 