"""
PHP 개발자를 위한 Python 테스트 예제
이 파일은 PHP 개발자가 Python의 테스트 방식을 이해하는 데 도움을 주기 위한 예제입니다.
"""

import unittest
from typing import List, Dict, Any

class TestPHPDeveloper(unittest.TestCase):
    """PHP 개발자를 위한 Python 테스트 예제 클래스"""

    def setUp(self):
        """각 테스트 메서드 실행 전에 호출되는 설정 메서드"""
        self.test_array = [1, 2, 3, 4, 5]
        self.test_dict = {"name": "John", "age": 30}
        self.test_string = " Hello World! "

    def test_array_operations(self):
        """PHP의 array_* 함수들과 Python의 리스트 연산 비교"""
        # PHP: array_map(function($x) { return $x * 2; }, $array)
        mapped = [x * 2 for x in self.test_array]
        self.assertEqual(mapped, [2, 4, 6, 8, 10])

        # PHP: array_filter($array, function($x) { return $x > 3; })
        filtered = [x for x in self.test_array if x > 3]
        self.assertEqual(filtered, [4, 5])

        # PHP: array_reduce($array, function($carry, $item) { return $carry + $item; }, 0)
        reduced = sum(self.test_array)
        self.assertEqual(reduced, 15)

    def test_string_operations(self):
        """PHP의 문자열 함수들과 Python의 문자열 메서드 비교"""
        # PHP: trim($string)
        trimmed = self.test_string.strip()
        self.assertEqual(trimmed, "Hello World!")

        # PHP: strtolower($string)
        lower = self.test_string.lower()
        self.assertEqual(lower, " hello world! ")

        # PHP: str_replace("World", "Python", $string)
        replaced = self.test_string.replace("World", "Python")
        self.assertEqual(replaced, " Hello Python! ")

    def test_associative_array(self):
        """PHP의 연관 배열과 Python의 딕셔너리 비교"""
        # PHP: $array["name"]
        self.assertEqual(self.test_dict["name"], "John")

        # PHP: isset($array["age"])
        self.assertTrue("age" in self.test_dict)

        # PHP: $array["email"] = "john@example.com"
        self.test_dict["email"] = "john@example.com"
        self.assertEqual(self.test_dict["email"], "john@example.com")

    def test_class_operations(self):
        """PHP의 클래스와 Python의 클래스 비교"""
        class User:
            def __init__(self, name: str, age: int):
                self.name = name
                self.age = age

            def greet(self) -> str:
                return f"Hello, {self.name}!"

        # PHP: $user = new User("John", 30);
        user = User("John", 30)

        # PHP: $user->name
        self.assertEqual(user.name, "John")

        # PHP: $user->greet()
        self.assertEqual(user.greet(), "Hello, John!")

    def test_exception_handling(self):
        """PHP의 예외 처리와 Python의 예외 처리 비교"""
        # PHP: try { ... } catch (Exception $e) { ... }
        try:
            result = 10 / 0
        except ZeroDivisionError as e:
            self.assertIsInstance(e, ZeroDivisionError)

    def test_type_hinting(self):
        """PHP의 타입 힌트와 Python의 타입 힌트 비교"""
        def add_numbers(a: int, b: int) -> int:
            return a + b

        result = add_numbers(5, 3)
        self.assertEqual(result, 8)

        # 타입 힌트는 실행 시점에 강제되지 않음
        result = add_numbers("5", "3")  # 문자열도 가능
        self.assertEqual(result, "53")

    def test_namespace_comparison(self):
        """PHP의 네임스페이스와 Python의 모듈 시스템 비교"""
        # PHP: use App\Models\User;
        # Python에서는 from app.models import User
        # (이 예제에서는 실제 import는 하지 않음)
        pass

if __name__ == '__main__':
    unittest.main() 