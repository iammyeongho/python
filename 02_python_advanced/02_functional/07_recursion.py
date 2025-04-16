"""
재귀 함수와 관련된 예제
이 파일은 재귀 함수의 개념과 사용법을 다룹니다.
"""

from typing import List, Any
import sys
from functools import lru_cache

class RecursionExamples:
    """재귀 함수 예제 클래스"""

    def __init__(self):
        # 재귀 깊이 제한 설정
        sys.setrecursionlimit(10000)

    def factorial(self, n: int) -> int:
        """팩토리얼 계산 (재귀)"""
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)

    def fibonacci(self, n: int) -> int:
        """피보나치 수열 (재귀)"""
        if n <= 1:
            return n
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    @lru_cache(maxsize=None)
    def fibonacci_memoized(self, n: int) -> int:
        """메모이제이션을 사용한 피보나치 수열"""
        if n <= 1:
            return n
        return self.fibonacci_memoized(n - 1) + self.fibonacci_memoized(n - 2)

    def binary_search(self, arr: List[int], target: int, left: int = 0, right: int = None) -> int:
        """이진 검색 (재귀)"""
        if right is None:
            right = len(arr) - 1

        if left > right:
            return -1

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return self.binary_search(arr, target, mid + 1, right)
        else:
            return self.binary_search(arr, target, left, mid - 1)

    def tower_of_hanoi(self, n: int, source: str, target: str, auxiliary: str) -> None:
        """하노이 탑 (재귀)"""
        if n == 1:
            print(f"Move disk 1 from {source} to {target}")
            return
        
        self.tower_of_hanoi(n - 1, source, auxiliary, target)
        print(f"Move disk {n} from {source} to {target}")
        self.tower_of_hanoi(n - 1, auxiliary, target, source)

    def quick_sort(self, arr: List[int]) -> List[int]:
        """퀵 정렬 (재귀)"""
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return self.quick_sort(left) + middle + self.quick_sort(right)

def main():
    """메인 함수"""
    examples = RecursionExamples()
    
    # 팩토리얼 예제
    print("\n=== Factorial ===")
    for n in range(1, 6):
        print(f"{n}! = {examples.factorial(n)}")

    # 피보나치 수열 예제
    print("\n=== Fibonacci ===")
    for n in range(10):
        print(f"F({n}) = {examples.fibonacci(n)}")

    # 메모이제이션을 사용한 피보나치 수열 예제
    print("\n=== Fibonacci (Memoized) ===")
    for n in range(10):
        print(f"F({n}) = {examples.fibonacci_memoized(n)}")

    # 이진 검색 예제
    print("\n=== Binary Search ===")
    arr = [1, 3, 5, 7, 9, 11, 13]
    target = 7
    index = examples.binary_search(arr, target)
    print(f"Target {target} found at index {index}")

    # 하노이 탑 예제
    print("\n=== Tower of Hanoi ===")
    examples.tower_of_hanoi(3, 'A', 'C', 'B')

    # 퀵 정렬 예제
    print("\n=== Quick Sort ===")
    arr = [3, 6, 8, 10, 1, 2, 1]
    sorted_arr = examples.quick_sort(arr)
    print(f"Original array: {arr}")
    print(f"Sorted array: {sorted_arr}")

if __name__ == "__main__":
    main() 