"""
PHP와 Python의 데이터 구조 비교
이 파일은 PHP 개발자가 Python의 데이터 구조를 이해하는 데 도움을 주기 위한 예제입니다.
"""

from typing import List, Dict, Set, Tuple, Any
from dataclasses import dataclass
from enum import Enum

class DataStructureExamples:
    """데이터 구조 예제 클래스"""

    def __init__(self):
        # 1. 리스트 (PHP의 배열과 유사)
        self.simple_list: List[int] = [1, 2, 3, 4, 5]
        self.mixed_list: List[Any] = [1, "two", 3.0, True]
        
        # 2. 딕셔너리 (PHP의 연관 배열과 유사)
        self.simple_dict: Dict[str, int] = {"one": 1, "two": 2, "three": 3}
        self.nested_dict: Dict[str, Dict[str, int]] = {
            "user1": {"age": 25, "score": 85},
            "user2": {"age": 30, "score": 90}
        }
        
        # 3. 세트 (PHP의 배열의 unique와 유사)
        self.simple_set: Set[int] = {1, 2, 3, 4, 5}
        self.another_set: Set[int] = {4, 5, 6, 7, 8}
        
        # 4. 튜플 (불변 리스트)
        self.simple_tuple: Tuple[int, str, float] = (1, "two", 3.0)
        
        # 5. 열거형 (PHP의 enum과 유사)
        self.status = Status

    def list_examples(self) -> None:
        """리스트 예제"""
        print("\n=== List Examples ===")
        
        # 리스트 생성 (PHP: $array = [1, 2, 3];)
        numbers: List[int] = [1, 2, 3, 4, 5]
        print(f"Original list: {numbers}")
        
        # 요소 추가 (PHP: $array[] = 6;)
        numbers.append(6)
        print(f"After append: {numbers}")
        
        # 요소 삭제 (PHP: unset($array[0]);)
        del numbers[0]
        print(f"After delete: {numbers}")
        
        # 리스트 컴프리헨션 (PHP: array_map())
        squares = [x**2 for x in numbers]
        print(f"Squares: {squares}")
        
        # 필터링 (PHP: array_filter())
        evens = [x for x in numbers if x % 2 == 0]
        print(f"Even numbers: {evens}")

    def dict_examples(self) -> None:
        """딕셔너리 예제"""
        print("\n=== Dictionary Examples ===")
        
        # 딕셔너리 생성 (PHP: $array = ["one" => 1, "two" => 2];)
        user: Dict[str, Any] = {
            "name": "John",
            "age": 30,
            "email": "john@example.com"
        }
        print(f"Original dict: {user}")
        
        # 요소 추가 (PHP: $array["city"] = "New York";)
        user["city"] = "New York"
        print(f"After add: {user}")
        
        # 요소 삭제 (PHP: unset($array["email"]);)
        del user["email"]
        print(f"After delete: {user}")
        
        # 딕셔너리 컴프리헨션
        squares = {x: x**2 for x in range(5)}
        print(f"Squares dict: {squares}")

    def set_examples(self) -> None:
        """세트 예제"""
        print("\n=== Set Examples ===")
        
        # 세트 생성 (PHP: $array = array_unique([1, 2, 2, 3]);)
        numbers: Set[int] = {1, 2, 2, 3, 3, 4}
        print(f"Original set: {numbers}")
        
        # 요소 추가 (PHP: $array[] = 5;)
        numbers.add(5)
        print(f"After add: {numbers}")
        
        # 요소 삭제 (PHP: unset($array[0]);)
        numbers.remove(1)
        print(f"After remove: {numbers}")
        
        # 세트 연산
        set1 = {1, 2, 3, 4, 5}
        set2 = {4, 5, 6, 7, 8}
        
        print(f"Union: {set1 | set2}")  # 합집합
        print(f"Intersection: {set1 & set2}")  # 교집합
        print(f"Difference: {set1 - set2}")  # 차집합

    def tuple_examples(self) -> None:
        """튜플 예제"""
        print("\n=== Tuple Examples ===")
        
        # 튜플 생성 (PHP에서는 배열을 const로 선언)
        point: Tuple[int, int] = (10, 20)
        print(f"Point: {point}")
        
        # 튜플 언패킹 (PHP에서는 list() 사용)
        x, y = point
        print(f"x: {x}, y: {y}")
        
        # 튜플은 불변 (수정 불가)
        try:
            point[0] = 30  # 에러 발생
        except TypeError as e:
            print(f"Error: {e}")

    def enum_examples(self) -> None:
        """열거형 예제"""
        print("\n=== Enum Examples ===")
        
        # 열거형 사용 (PHP의 enum과 유사)
        status = Status.ACTIVE
        print(f"Status: {status}")
        print(f"Status value: {status.value}")
        
        # 열거형 비교
        if status == Status.ACTIVE:
            print("User is active")

class Status(Enum):
    """상태 열거형"""
    ACTIVE = 1
    INACTIVE = 2
    SUSPENDED = 3

@dataclass
class User:
    """사용자 데이터 클래스"""
    name: str
    age: int
    email: str
    status: Status = Status.ACTIVE

def main():
    """메인 함수"""
    examples = DataStructureExamples()
    
    # 각 데이터 구조 예제 실행
    examples.list_examples()
    examples.dict_examples()
    examples.set_examples()
    examples.tuple_examples()
    examples.enum_examples()
    
    # 데이터 클래스 예제
    print("\n=== Data Class Example ===")
    user = User("John", 30, "john@example.com")
    print(f"User: {user}")
    print(f"User name: {user.name}")
    print(f"User status: {user.status}")

if __name__ == "__main__":
    main() 