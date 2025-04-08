# 파이썬 데이터 구조 예제
# 작성일: 2024-04-08
# 목적: 파이썬의 기본 데이터 구조와 관련된 다양한 기능을 설명하는 예제 코드

# 1. 리스트 (List)
# 리스트는 순서가 있는 가변 시퀀스입니다.
print("=== 1. 리스트 (List) ===")

# 리스트 생성
numbers = [1, 2, 3, 4, 5]
print(f"기본 리스트: {numbers}")

# 리스트 인덱싱
print(f"첫 번째 요소: {numbers[0]}")
print(f"마지막 요소: {numbers[-1]}")

# 리스트 슬라이싱
print(f"처음부터 3번째까지: {numbers[:3]}")
print(f"2번째부터 끝까지: {numbers[1:]}")

# 리스트 수정
numbers[0] = 10
print(f"첫 번째 요소 수정: {numbers}")

# 리스트 메서드
numbers.append(6)
print(f"append(6): {numbers}")

numbers.insert(0, 0)
print(f"insert(0, 0): {numbers}")

numbers.remove(3)
print(f"remove(3): {numbers}")

popped = numbers.pop()
print(f"pop(): {popped}, 리스트: {numbers}")

# 리스트 정렬
numbers.sort()
print(f"정렬: {numbers}")

numbers.reverse()
print(f"역순 정렬: {numbers}")

# 2. 튜플 (Tuple)
# 튜플은 순서가 있는 불변 시퀀스입니다.
print("\n=== 2. 튜플 (Tuple) ===")

# 튜플 생성
coordinates = (10, 20)
print(f"기본 튜플: {coordinates}")

# 튜플 언패킹
x, y = coordinates
print(f"x: {x}, y: {y}")

# 튜플 메서드
numbers_tuple = (1, 2, 2, 3, 2, 4)
print(f"2의 개수: {numbers_tuple.count(2)}")
print(f"2의 인덱스: {numbers_tuple.index(2)}")

# 3. 딕셔너리 (Dictionary)
# 딕셔너리는 키-값 쌍의 집합입니다.
print("\n=== 3. 딕셔너리 (Dictionary) ===")

# 딕셔너리 생성
person = {
    "name": "홍길동",
    "age": 25,
    "city": "서울"
}
print(f"기본 딕셔너리: {person}")

# 딕셔너리 접근
print(f"이름: {person['name']}")
print(f"나이: {person.get('age')}")

# 딕셔너리 수정
person["age"] = 26
print(f"나이 수정: {person}")

# 딕셔너리 메서드
print(f"키 목록: {list(person.keys())}")
print(f"값 목록: {list(person.values())}")
print(f"키-값 쌍: {list(person.items())}")

# 4. 집합 (Set)
# 집합은 중복되지 않는 요소들의 집합입니다.
print("\n=== 4. 집합 (Set) ===")

# 집합 생성
numbers_set = {1, 2, 3, 4, 5}
print(f"기본 집합: {numbers_set}")

# 집합 연산
other_set = {4, 5, 6, 7, 8}
print(f"합집합: {numbers_set | other_set}")
print(f"교집합: {numbers_set & other_set}")
print(f"차집합: {numbers_set - other_set}")
print(f"대칭차집합: {numbers_set ^ other_set}")

# 집합 메서드
numbers_set.add(6)
print(f"add(6): {numbers_set}")

numbers_set.remove(1)
print(f"remove(1): {numbers_set}")

# 5. 문자열 (String)
# 문자열은 문자들의 시퀀스입니다.
print("\n=== 5. 문자열 (String) ===")

# 문자열 생성
text = "Hello, Python!"
print(f"기본 문자열: {text}")

# 문자열 메서드
print(f"대문자: {text.upper()}")
print(f"소문자: {text.lower()}")
print(f"첫 글자 대문자: {text.capitalize()}")
print(f"단어 첫 글자 대문자: {text.title()}")

# 문자열 분할과 결합
words = text.split(", ")
print(f"분할: {words}")
print(f"결합: {', '.join(words)}")

# 6. 리스트 컴프리헨션
# 리스트를 간단하게 생성할 수 있는 방법입니다.
print("\n=== 6. 리스트 컴프리헨션 ===")

# 기본 리스트 컴프리헨션
squares = [x**2 for x in range(5)]
print(f"제곱수 리스트: {squares}")

# 조건부 리스트 컴프리헨션
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"짝수의 제곱: {even_squares}")

# 7. 딕셔너리 컴프리헨션
# 딕셔너리를 간단하게 생성할 수 있는 방법입니다.
print("\n=== 7. 딕셔너리 컴프리헨션 ===")

# 기본 딕셔너리 컴프리헨션
square_dict = {x: x**2 for x in range(5)}
print(f"제곱수 딕셔너리: {square_dict}")

# 조건부 딕셔너리 컴프리헨션
even_square_dict = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"짝수의 제곱 딕셔너리: {even_square_dict}")

# 8. 집합 컴프리헨션
# 집합을 간단하게 생성할 수 있는 방법입니다.
print("\n=== 8. 집합 컴프리헨션 ===")

# 기본 집합 컴프리헨션
square_set = {x**2 for x in range(5)}
print(f"제곱수 집합: {square_set}")

# 조건부 집합 컴프리헨션
even_square_set = {x**2 for x in range(10) if x % 2 == 0}
print(f"짝수의 제곱 집합: {even_square_set}")

# 9. 중첩 데이터 구조
# 데이터 구조 안에 다른 데이터 구조를 포함할 수 있습니다.
print("\n=== 9. 중첩 데이터 구조 ===")

# 중첩 리스트
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"중첩 리스트: {matrix}")
print(f"matrix[1][1]: {matrix[1][1]}")

# 중첩 딕셔너리
users = {
    "user1": {
        "name": "홍길동",
        "age": 25
    },
    "user2": {
        "name": "김철수",
        "age": 30
    }
}
print(f"중첩 딕셔너리: {users}")
print(f"user1의 이름: {users['user1']['name']}")

# 10. 데이터 구조 변환
# 한 데이터 구조를 다른 데이터 구조로 변환할 수 있습니다.
print("\n=== 10. 데이터 구조 변환 ===")

# 리스트를 집합으로 변환
numbers_list = [1, 2, 2, 3, 3, 4]
unique_numbers = set(numbers_list)
print(f"리스트를 집합으로 변환: {unique_numbers}")

# 집합을 리스트로 변환
numbers_list = list(unique_numbers)
print(f"집합을 리스트로 변환: {numbers_list}")

# 리스트를 딕셔너리로 변환
pairs = [('a', 1), ('b', 2), ('c', 3)]
pairs_dict = dict(pairs)
print(f"리스트를 딕셔너리로 변환: {pairs_dict}")

print("\n프로그램 종료") 