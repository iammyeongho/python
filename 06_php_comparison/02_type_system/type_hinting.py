"""
PHP와 Python의 타입 힌팅 비교
이 파일은 PHP 개발자가 Python의 타입 힌팅을 이해하는 데 도움을 주기 위한 예제입니다.
"""

from typing import (
    List, Dict, Set, Tuple, Optional, Union, Any,
    Callable, TypeVar, Generic, Type, Literal
)
from dataclasses import dataclass
from datetime import datetime

# 기본 타입 힌팅 (PHP의 타입 힌팅과 유사)
def add_numbers(a: int, b: int) -> int:
    return a + b

# 복합 타입 힌팅
def process_data(data: List[Dict[str, Union[int, str]]]) -> Set[str]:
    return {str(item) for item in data}

# 옵셔널 타입 (PHP의 nullable 타입과 유사)
def get_user_name(user_id: Optional[int] = None) -> str:
    if user_id is None:
        return "Guest"
    return f"User_{user_id}"

# 제네릭 클래스 (PHP의 제네릭과 유사)
T = TypeVar('T')

class Container(Generic[T]):
    def __init__(self, value: T):
        self.value = value
    
    def get_value(self) -> T:
        return self.value

# 콜러블 타입 (PHP의 callable 타입과 유사)
def apply_function(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

# 리터럴 타입 (PHP의 enum과 유사)
Status = Literal["active", "inactive", "pending"]

def update_status(status: Status) -> None:
    print(f"Updating status to: {status}")

# 데이터 클래스 (PHP의 클래스와 유사)
@dataclass
class User:
    id: int
    name: str
    email: str
    created_at: datetime
    status: Status = "active"
    
    def get_full_info(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "created_at": self.created_at.isoformat(),
            "status": self.status
        }

# 타입 가드 (PHP의 instanceof와 유사)
def is_valid_user(obj: Any) -> bool:
    return isinstance(obj, User)

# 유니온 타입 (PHP의 union 타입과 유사)
def process_result(result: Union[int, str, List[int]]) -> str:
    if isinstance(result, int):
        return f"Number: {result}"
    elif isinstance(result, str):
        return f"String: {result}"
    else:
        return f"List: {result}"

def main():
    # 기본 타입 힌팅 사용
    result = add_numbers(5, 3)
    print(f"Addition result: {result}")
    
    # 복합 타입 사용
    data = [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]
    processed = process_data(data)
    print(f"Processed data: {processed}")
    
    # 옵셔널 타입 사용
    print(f"User name: {get_user_name()}")
    print(f"User name: {get_user_name(123)}")
    
    # 제네릭 클래스 사용
    container = Container[int](42)
    print(f"Container value: {container.get_value()}")
    
    # 콜러블 타입 사용
    def multiply(a: int, b: int) -> int:
        return a * b
    
    result = apply_function(multiply, 4, 5)
    print(f"Function result: {result}")
    
    # 리터럴 타입 사용
    update_status("active")
    
    # 데이터 클래스 사용
    user = User(
        id=1,
        name="John Doe",
        email="john@example.com",
        created_at=datetime.now()
    )
    print(f"User info: {user.get_full_info()}")
    
    # 타입 가드 사용
    print(f"Is valid user: {is_valid_user(user)}")
    
    # 유니온 타입 사용
    print(process_result(42))
    print(process_result("Hello"))
    print(process_result([1, 2, 3]))

if __name__ == "__main__":
    main() 