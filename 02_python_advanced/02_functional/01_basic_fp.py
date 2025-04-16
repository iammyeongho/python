"""
함수형 프로그래밍의 기본 개념
이 파일은 함수형 프로그래밍의 기본 개념을 다룹니다.
"""

from typing import List, Callable, Any

class BasicFunctionalProgramming:
    """기본 함수형 프로그래밍 예제 클래스"""

    def __init__(self):
        self.numbers: List[int] = [1, 2, 3, 4, 5]
        self.names: List[str] = ["John", "Jane", "Doe", "Alice", "Bob"]

    def first_class_functions(self) -> None:
        """일급 함수 예제"""
        print("\n=== First-Class Functions ===")
        
        # 함수를 변수에 할당
        def greet(name: str) -> str:
            return f"Hello, {name}!"
        
        say_hello = greet
        print(say_hello("Python"))
        
        # 함수를 리스트에 저장
        functions = [greet, str.upper, str.lower]
        for func in functions:
            print(func("Python"))

    def pure_functions(self) -> None:
        """순수 함수 예제"""
        print("\n=== Pure Functions ===")
        
        # 순수 함수 예제
        def add(a: int, b: int) -> int:
            return a + b
        
        # 부수 효과가 없는 함수
        result = add(3, 4)
        print(f"Pure function result: {result}")

    def immutability(self) -> None:
        """불변성 예제"""
        print("\n=== Immutability ===")
        
        # 불변 객체 사용
        original_tuple = (1, 2, 3)
        new_tuple = original_tuple + (4,)
        print(f"Original tuple: {original_tuple}")
        print(f"New tuple: {new_tuple}")

def main():
    """메인 함수"""
    examples = BasicFunctionalProgramming()
    
    # 기본 함수형 프로그래밍 예제 실행
    examples.first_class_functions()
    examples.pure_functions()
    examples.immutability()

if __name__ == "__main__":
    main() 