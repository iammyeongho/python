# 1. PHP 개발자를 위한 Python 가이드

## 1. PHP와 Python의 주요 차이점

### 1.1 변수 선언과 타입 시스템
- PHP: 동적 타입, `$` 기호 사용
```php
$name = "John";
$age = 30;
```
- Python: 동적 타입, 타입 힌트 지원
```python
name: str = "John"
age: int = 30
```

### 1.2 네임스페이스와 모듈 시스템
- PHP: `namespace` 키워드 사용
```php
namespace App\Controllers;
```
- Python: 파일 기반 모듈 시스템
```python
from app.controllers import UserController
```

### 1.3 함수와 메서드 정의
- PHP: `function` 키워드 사용
```php
function greet($name) {
    return "Hello, " . $name;
}
```
- Python: `def` 키워드 사용
```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

### 1.4 클래스와 객체 지향 프로그래밍
- PHP: `class` 키워드, `$this` 사용
```php
class User {
    private $name;
    
    public function __construct($name) {
        $this->name = $name;
    }
}
```
- Python: `class` 키워드, `self` 사용
```python
class User:
    def __init__(self, name: str):
        self.name = name
```

## 2. Python에서 자주 하는 실수

### 2.1 들여쓰기 관련 실수
- Python은 들여쓰기가 문법의 일부
- PHP 개발자들이 자주 하는 실수:
  - 중괄호 대신 들여쓰기 사용
  - 일관되지 않은 들여쓰기

### 2.2 가변 객체와 불변 객체
- Python의 리스트는 가변(mutable)
- Python의 튜플은 불변(immutable)
- PHP의 배열은 모두 가변

### 2.3 리스트 컴프리헨션
- PHP의 `array_map`과 유사하지만 더 강력
```python
# Python
squares = [x**2 for x in range(10)]

# PHP
$squares = array_map(function($x) { return $x * $x; }, range(0, 9));
```

## 3. Python에서 PHP와 유사한 패턴

### 3.1 MVC 패턴
```python
# models/user.py
class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

# controllers/user_controller.py
class UserController:
    def create(self, user_data: dict) -> User:
        user = User(**user_data)
        return user

# views/user_view.py
class UserView:
    def render(self, user: User) -> str:
        return f"User: {user.name}, Email: {user.email}"
```

### 3.2 의존성 주입
```python
class Database:
    def connect(self):
        pass

class UserRepository:
    def __init__(self, db: Database):
        self.db = db

# 사용
db = Database()
user_repo = UserRepository(db)
```

### 3.3 미들웨어 패턴
```python
class Middleware:
    def __init__(self, next_middleware=None):
        self.next = next_middleware

    def handle(self, request):
        if self.next:
            return self.next.handle(request)
        return request

class AuthMiddleware(Middleware):
    def handle(self, request):
        # 인증 로직
        return super().handle(request)
```

## 4. Python에서 유용한 PHP 대체 기능

### 4.1 배열 조작
- PHP의 `array_*` 함수들
```php
$filtered = array_filter($array, function($item) { return $item > 0; });
$mapped = array_map(function($item) { return $item * 2; }, $array);
```
- Python의 리스트 컴프리헨션
```python
filtered = [x for x in array if x > 0]
mapped = [x * 2 for x in array]
```

### 4.2 문자열 처리
- PHP의 문자열 함수
```php
$trimmed = trim($string);
$lower = strtolower($string);
```
- Python의 문자열 메서드
```python
trimmed = string.strip()
lower = string.lower()
```

## 5. 학습 리소스

### 5.1 온라인 강의
- Python for PHP Developers
- Python Crash Course
- Real Python

### 5.2 문서
- Python 공식 문서
- PHP to Python Migration Guide
- Python Design Patterns

### 5.3 연습 프로젝트
1. 간단한 CRUD 애플리케이션
2. RESTful API 서버
3. 웹 스크래퍼
4. 데이터 처리 파이프라인 