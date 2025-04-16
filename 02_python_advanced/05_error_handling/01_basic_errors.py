"""
기본적인 예외 처리
이 파일은 Python의 기본적인 예외 처리 방법을 다룹니다.
"""

def basic_try_except():
    """기본적인 try-except 예제"""
    print("\n=== 기본적인 try-except 예제 ===")
    
    try:
        # 0으로 나누기 시도
        result = 10 / 0
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다!")

def multiple_exceptions():
    """여러 예외 처리 예제"""
    print("\n=== 여러 예외 처리 예제 ===")
    
    try:
        # 리스트 인덱스 오류
        numbers = [1, 2, 3]
        print(numbers[5])
    except IndexError:
        print("리스트 인덱스가 범위를 벗어났습니다!")
    except Exception as e:
        print(f"예상치 못한 오류가 발생했습니다: {e}")

def try_except_else():
    """try-except-else 예제"""
    print("\n=== try-except-else 예제 ===")
    
    try:
        result = 10 / 2
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다!")
    else:
        print(f"계산 결과: {result}")

def try_except_finally():
    """try-except-finally 예제"""
    print("\n=== try-except-finally 예제 ===")
    
    try:
        file = open("nonexistent.txt", "r")
        content = file.read()
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다!")
    finally:
        print("항상 실행되는 finally 블록")

def raise_exception():
    """예외 발생 예제"""
    print("\n=== 예외 발생 예제 ===")
    
    try:
        raise ValueError("사용자 정의 오류 메시지")
    except ValueError as e:
        print(f"발생한 오류: {e}")

def main():
    """메인 함수"""
    basic_try_except()
    multiple_exceptions()
    try_except_else()
    try_except_finally()
    raise_exception()

if __name__ == "__main__":
    main() 