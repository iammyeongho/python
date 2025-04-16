"""
PHP와 Python의 데이터 구조 비교
이 파일은 PHP 개발자가 Python의 데이터 구조를 이해하는 데 도움을 주기 위한 예제입니다.
"""

from typing import List, Dict, Set, Tuple, Optional, Union, Any
from dataclasses import dataclass
from collections import defaultdict, Counter, deque

# 1. 배열/리스트 비교
def array_comparison():
    # Python 리스트 (PHP 배열과 유사)
    fruits = ["apple", "banana", "cherry"]
    
    # 요소 추가
    fruits.append("orange")  # PHP: array_push($fruits, "orange")
    
    # 요소 제거
    fruits.remove("banana")  # PHP: unset($fruits[array_search("banana", $fruits)])
    
    # 요소 접근
    first_fruit = fruits[0]  # PHP: $fruits[0]
    
    # 리스트 컴프리헨션 (PHP의 array_map과 유사)
    numbers = [1, 2, 3, 4, 5]
    squares = [x**2 for x in numbers]  # PHP: array_map(fn($x) => $x * $x, $numbers)
    
    return fruits, squares

# 2. 연관 배열/딕셔너리 비교
def dictionary_comparison():
    # Python 딕셔너리 (PHP 연관 배열과 유사)
    person = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    
    # 요소 추가/수정
    person["email"] = "john@example.com"  # PHP: $person["email"] = "john@example.com"
    
    # 요소 제거
    del person["age"]  # PHP: unset($person["age"])
    
    # 요소 접근
    name = person["name"]  # PHP: $person["name"]
    
    # 딕셔너리 컴프리헨션
    numbers = [1, 2, 3, 4, 5]
    squares_dict = {x: x**2 for x in numbers}  # PHP: array_combine($numbers, array_map(fn($x) => $x * $x, $numbers))
    
    return person, squares_dict

# 3. 세트 비교
def set_comparison():
    # Python 세트 (PHP의 array_unique와 유사)
    fruits = {"apple", "banana", "cherry", "apple"}
    
    # 요소 추가
    fruits.add("orange")  # PHP: $fruits[] = "orange"; $fruits = array_unique($fruits);
    
    # 요소 제거
    fruits.remove("banana")  # PHP: unset($fruits[array_search("banana", $fruits)]);
    
    # 세트 연산
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    
    union = set1 | set2  # PHP: array_unique(array_merge($set1, $set2))
    intersection = set1 & set2  # PHP: array_intersect($set1, $set2)
    difference = set1 - set2  # PHP: array_diff($set1, $set2)
    
    return fruits, union, intersection, difference

# 4. 튜플 비교
def tuple_comparison():
    # Python 튜플 (PHP의 배열과 유사하지만 불변)
    coordinates = (10, 20)
    
    # 요소 접근
    x, y = coordinates  # PHP: list($x, $y) = $coordinates;
    
    # 튜플 언패킹
    name, age, city = ("John", 30, "New York")  # PHP: list($name, $age, $city) = ["John", 30, "New York"];
    
    return coordinates, (x, y), (name, age, city)

# 5. 고급 데이터 구조
def advanced_structures():
    # defaultdict (PHP의 array와 유사하지만 기본값 제공)
    word_count = defaultdict(int)
    words = ["apple", "banana", "apple", "cherry"]
    for word in words:
        word_count[word] += 1  # PHP: $word_count[$word] = ($word_count[$word] ?? 0) + 1;
    
    # Counter (PHP의 array_count_values와 유사)
    counter = Counter(words)  # PHP: array_count_values($words)
    
    # deque (PHP의 array와 유사하지만 양쪽 끝에서 효율적인 작업 가능)
    queue = deque(["apple", "banana", "cherry"])
    queue.append("orange")  # PHP: array_push($queue, "orange")
    queue.popleft()  # PHP: array_shift($queue)
    
    return word_count, counter, queue

def main():
    # 배열/리스트 비교
    fruits, squares = array_comparison()
    print("\nArray/List Comparison:")
    print(f"Fruits: {fruits}")
    print(f"Squares: {squares}")
    
    # 연관 배열/딕셔너리 비교
    person, squares_dict = dictionary_comparison()
    print("\nDictionary Comparison:")
    print(f"Person: {person}")
    print(f"Squares Dictionary: {squares_dict}")
    
    # 세트 비교
    fruits_set, union, intersection, difference = set_comparison()
    print("\nSet Comparison:")
    print(f"Fruits Set: {fruits_set}")
    print(f"Union: {union}")
    print(f"Intersection: {intersection}")
    print(f"Difference: {difference}")
    
    # 튜플 비교
    coordinates, (x, y), (name, age, city) = tuple_comparison()
    print("\nTuple Comparison:")
    print(f"Coordinates: {coordinates}")
    print(f"X: {x}, Y: {y}")
    print(f"Name: {name}, Age: {age}, City: {city}")
    
    # 고급 데이터 구조
    word_count, counter, queue = advanced_structures()
    print("\nAdvanced Structures:")
    print(f"Word Count: {dict(word_count)}")
    print(f"Counter: {counter}")
    print(f"Queue: {list(queue)}")

if __name__ == "__main__":
    main() 