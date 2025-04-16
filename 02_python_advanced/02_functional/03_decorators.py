"""
데코레이터와 관련된 예제
이 파일은 데코레이터의 개념과 사용법을 다룹니다.
"""

from typing import Callable, Any
import time
import functools

class DecoratorExamples:
    """데코레이터 예제 클래스"""

    def __init__(self):
        pass

    def basic_decorator(self) -> None:
        """기본 데코레이터 예제"""
        print("\n=== Basic Decorator ===")
        
        def simple_decorator(func: Callable) -> Callable:
            def wrapper(*args, **kwargs):
                print(f"Before calling {func.__name__}")
                result = func(*args, **kwargs)
                print(f"After calling {func.__name__}")
                return result
            return wrapper

        @simple_decorator
        def greet(name: str) -> str:
            return f"Hello, {name}!"

        print(greet("Python"))

    def timing_decorator(self) -> None:
        """실행 시간 측정 데코레이터 예제"""
        print("\n=== Timing Decorator ===")
        
        def timer(func: Callable) -> Callable:
            @functools.wraps(func)
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

    def parameterized_decorator(self) -> None:
        """매개변수가 있는 데코레이터 예제"""
        print("\n=== Parameterized Decorator ===")
        
        def repeat(n: int):
            def decorator(func: Callable) -> Callable:
                @functools.wraps(func)
                def wrapper(*args, **kwargs):
                    for _ in range(n):
                        result = func(*args, **kwargs)
                    return result
                return wrapper
            return decorator

        @repeat(3)
        def say_hello():
            print("Hello!")

        say_hello()

    def class_decorator(self) -> None:
        """클래스 데코레이터 예제"""
        print("\n=== Class Decorator ===")
        
        def singleton(cls):
            instances = {}
            
            def get_instance(*args, **kwargs):
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
                return instances[cls]
            
            return get_instance

        @singleton
        class Database:
            def __init__(self):
                print("Database initialized")

        db1 = Database()
        db2 = Database()
        print(f"Same instance: {db1 is db2}")

def main():
    """메인 함수"""
    examples = DecoratorExamples()
    
    # 데코레이터 예제 실행
    examples.basic_decorator()
    examples.timing_decorator()
    examples.parameterized_decorator()
    examples.class_decorator()

if __name__ == "__main__":
    main() 