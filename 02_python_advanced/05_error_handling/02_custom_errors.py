"""
사용자 정의 예외
이 파일은 Python에서 사용자 정의 예외 클래스를 만드는 방법을 다룹니다.
"""

class ValidationError(Exception):
    """데이터 검증 실패 시 발생하는 예외"""
    def __init__(self, message: str, field: str = None):
        self.message = message
        self.field = field
        super().__init__(self.message)

class DatabaseError(Exception):
    """데이터베이스 작업 실패 시 발생하는 예외"""
    def __init__(self, message: str, sql: str = None):
        self.message = message
        self.sql = sql
        super().__init__(self.message)

class UserNotFoundError(Exception):
    """사용자를 찾을 수 없을 때 발생하는 예외"""
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.message = f"User with ID {user_id} not found"
        super().__init__(self.message)

class UserService:
    """사용자 관련 서비스 클래스"""
    
    def __init__(self):
        self.users = {
            1: {"name": "John Doe", "email": "john@example.com"},
            2: {"name": "Jane Smith", "email": "jane@example.com"}
        }
    
    def validate_user(self, user_data: dict) -> None:
        """사용자 데이터 검증"""
        if not user_data.get("name"):
            raise ValidationError("Name is required", "name")
        if not user_data.get("email"):
            raise ValidationError("Email is required", "email")
        if "@" not in user_data["email"]:
            raise ValidationError("Invalid email format", "email")
    
    def get_user(self, user_id: int) -> dict:
        """사용자 정보 조회"""
        try:
            if user_id not in self.users:
                raise UserNotFoundError(user_id)
            return self.users[user_id]
        except Exception as e:
            raise DatabaseError("Failed to get user", f"SELECT * FROM users WHERE id = {user_id}") from e
    
    def create_user(self, user_data: dict) -> dict:
        """새로운 사용자 생성"""
        try:
            # 데이터 검증
            self.validate_user(user_data)
            
            # 사용자 생성
            user_id = max(self.users.keys()) + 1
            self.users[user_id] = user_data
            
            return {"id": user_id, **user_data}
        except ValidationError:
            raise
        except Exception as e:
            raise DatabaseError("Failed to create user", 
                              f"INSERT INTO users (name, email) VALUES ('{user_data['name']}', '{user_data['email']}')") from e

def main():
    """메인 함수"""
    service = UserService()
    
    # 사용자 조회 예제
    try:
        user = service.get_user(1)
        print(f"Found user: {user}")
    except UserNotFoundError as e:
        print(f"Error: {e}")
    except DatabaseError as e:
        print(f"Database error: {e}")
    
    # 사용자 생성 예제
    try:
        new_user = service.create_user({
            "name": "Alice",
            "email": "alice@example.com"
        })
        print(f"Created user: {new_user}")
    except ValidationError as e:
        print(f"Validation error: {e}")
    except DatabaseError as e:
        print(f"Database error: {e}")
    
    # 잘못된 이메일 형식 예제
    try:
        service.create_user({
            "name": "Bob",
            "email": "invalid-email"
        })
    except ValidationError as e:
        print(f"Validation error: {e}")

if __name__ == "__main__":
    main() 