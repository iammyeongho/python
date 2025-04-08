# 파이썬 데이터 구조

# 1. 리스트 (List)
print("=== 리스트 (List) ===")

# 리스트 생성
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True, [1, 2, 3]]
print(f"빈 리스트: {empty_list}")
print(f"숫자 리스트: {numbers}")
print(f"혼합 리스트: {mixed_list}")

# 리스트 인덱싱
print(f"\n리스트 인덱싱:")
print(f"첫 번째 요소: {numbers[0]}")
print(f"마지막 요소: {numbers[-1]}")
print(f"뒤에서 두 번째 요소: {numbers[-2]}")

# 리스트 슬라이싱
print(f"\n리스트 슬라이싱:")
print(f"처음부터 3번 인덱스까지: {numbers[:3]}")
print(f"2번 인덱스부터 끝까지: {numbers[2:]}")
print(f"처음부터 끝까지 2칸씩: {numbers[::2]}")
print(f"역순으로: {numbers[::-1]}")

# 리스트 메서드
print(f"\n리스트 메서드:")
numbers.append(6)
print(f"append(6) 후: {numbers}")

numbers.insert(1, 1.5)
print(f"insert(1, 1.5) 후: {numbers}")

numbers.extend([7, 8, 9])
print(f"extend([7, 8, 9]) 후: {numbers}")

removed = numbers.pop()
print(f"pop() 후: {numbers}, 제거된 요소: {removed}")

removed = numbers.pop(1)
print(f"pop(1) 후: {numbers}, 제거된 요소: {removed}")

numbers.remove(3)
print(f"remove(3) 후: {numbers}")

index = numbers.index(4)
print(f"index(4): {index}")

count = numbers.count(2)
print(f"count(2): {count}")

numbers.sort()
print(f"sort() 후: {numbers}")

numbers.reverse()
print(f"reverse() 후: {numbers}")

# 리스트 컴프리헨션
print(f"\n리스트 컴프리헨션:")
squares = [x**2 for x in range(5)]
print(f"제곱 리스트: {squares}")

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"짝수의 제곱 리스트: {even_squares}")

# 2. 튜플 (Tuple)
print("\n=== 튜플 (Tuple) ===")

# 튜플 생성
empty_tuple = ()
single_tuple = (1,)  # 단일 요소 튜플은 쉼표 필요
numbers_tuple = (1, 2, 3, 4, 5)
mixed_tuple = (1, "hello", 3.14, True, [1, 2, 3])

print(f"빈 튜플: {empty_tuple}")
print(f"단일 요소 튜플: {single_tuple}")
print(f"숫자 튜플: {numbers_tuple}")
print(f"혼합 튜플: {mixed_tuple}")

# 튜플은 불변(immutable)이므로 수정 불가
# numbers_tuple[0] = 10  # TypeError 발생

# 튜플 메서드
print(f"\n튜플 메서드:")
index = numbers_tuple.index(3)
print(f"index(3): {index}")

count = numbers_tuple.count(2)
print(f"count(2): {count}")

# 튜플 언패킹
print(f"\n튜플 언패킹:")
a, b, c, d, e = numbers_tuple
print(f"a={a}, b={b}, c={c}, d={d}, e={e}")

# 3. 딕셔너리 (Dictionary)
print("\n=== 딕셔너리 (Dictionary) ===")

# 딕셔너리 생성
empty_dict = {}
person = {
    "name": "홍길동",
    "age": 25,
    "city": "서울",
    "is_student": True
}
print(f"빈 딕셔너리: {empty_dict}")
print(f"사람 정보: {person}")

# 딕셔너리 접근
print(f"\n딕셔너리 접근:")
print(f"이름: {person['name']}")
print(f"나이: {person.get('age')}")
print(f"존재하지 않는 키: {person.get('height', '정보 없음')}")

# 딕셔너리 수정
print(f"\n딕셔너리 수정:")
person["age"] = 26
print(f"나이 수정 후: {person}")

person["height"] = 175
print(f"키 추가 후: {person}")

del person["is_student"]
print(f"is_student 삭제 후: {person}")

# 딕셔너리 메서드
print(f"\n딕셔너리 메서드:")
print(f"키 목록: {list(person.keys())}")
print(f"값 목록: {list(person.values())}")
print(f"키-값 쌍 목록: {list(person.items())}")

# 딕셔너리 컴프리헨션
print(f"\n딕셔너리 컴프리헨션:")
squares_dict = {x: x**2 for x in range(5)}
print(f"제곱 딕셔너리: {squares_dict}")

# 4. 집합 (Set)
print("\n=== 집합 (Set) ===")

# 집합 생성
empty_set = set()
numbers_set = {1, 2, 3, 4, 5}
mixed_set = {1, "hello", 3.14, True}
print(f"빈 집합: {empty_set}")
print(f"숫자 집합: {numbers_set}")
print(f"혼합 집합: {mixed_set}")

# 집합 연산
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"\n집합 연산:")
print(f"합집합: {set1 | set2}")
print(f"합집합 (union): {set1.union(set2)}")
print(f"교집합: {set1 & set2}")
print(f"교집합 (intersection): {set1.intersection(set2)}")
print(f"차집합: {set1 - set2}")
print(f"차집합 (difference): {set1.difference(set2)}")
print(f"대칭차집합: {set1 ^ set2}")
print(f"대칭차집합 (symmetric_difference): {set1.symmetric_difference(set2)}")

# 집합 메서드
print(f"\n집합 메서드:")
numbers_set.add(6)
print(f"add(6) 후: {numbers_set}")

numbers_set.update([7, 8, 9])
print(f"update([7, 8, 9]) 후: {numbers_set}")

numbers_set.remove(1)
print(f"remove(1) 후: {numbers_set}")

numbers_set.discard(10)  # 존재하지 않는 요소도 오류 없음
print(f"discard(10) 후: {numbers_set}")

popped = numbers_set.pop()
print(f"pop() 후: {numbers_set}, 제거된 요소: {popped}")

numbers_set.clear()
print(f"clear() 후: {numbers_set}")

# 집합 컴프리헨션
print(f"\n집합 컴프리헨션:")
squares_set = {x**2 for x in range(5)}
print(f"제곱 집합: {squares_set}")

# 5. 문자열 (String) - 시퀀스 타입
print("\n=== 문자열 (String) ===")

# 문자열 생성
empty_string = ""
hello = "안녕하세요"
multi_line = """여러 줄
문자열
입니다."""

print(f"빈 문자열: '{empty_string}'")
print(f"인사: {hello}")
print(f"여러 줄 문자열: {multi_line}")

# 문자열 메서드
print(f"\n문자열 메서드:")
print(f"대문자 변환: {'hello'.upper()}")
print(f"소문자 변환: {'HELLO'.lower()}")
print(f"첫 글자 대문자: {'hello'.capitalize()}")
print(f"각 단어 첫 글자 대문자: {'hello world'.title()}")
print(f"좌우 공백 제거: {'  hello  '.strip()}")
print(f"좌측 공백 제거: {'  hello  '.lstrip()}")
print(f"우측 공백 제거: {'  hello  '.rstrip()}")
print(f"문자열 치환: {'hello world'.replace('world', 'python')}")
print(f"문자열 분할: {'hello,world,python'.split(',')}")
print(f"문자열 결합: {','.join(['hello', 'world', 'python'])}")
print(f"문자열 시작 확인: {'hello'.startswith('he')}")
print(f"문자열 끝 확인: {'hello'.endswith('lo')}")
print(f"문자열 포함 확인: {'hello'.find('ll')}")
print(f"문자열 포함 확인: {'hello'.count('l')}")

# 6. 바이트 (Bytes)와 바이트 배열 (Bytearray)
print("\n=== 바이트 (Bytes)와 바이트 배열 (Bytearray) ===")

# 바이트 생성
byte_data = b'Hello'
print(f"바이트: {byte_data}")
print(f"바이트 타입: {type(byte_data)}")

# 바이트 배열 생성
bytearray_data = bytearray(b'Hello')
print(f"바이트 배열: {bytearray_data}")
print(f"바이트 배열 타입: {type(bytearray_data)}")

# 바이트 배열은 수정 가능
bytearray_data[0] = 74  # 'J'의 ASCII 코드
print(f"수정된 바이트 배열: {bytearray_data}")

# 7. None 타입
print("\n=== None 타입 ===")

none_value = None
print(f"None 값: {none_value}")
print(f"None 타입: {type(none_value)}")

# None은 False로 평가됨
if None:
    print("None은 True로 평가됩니다.")
else:
    print("None은 False로 평가됩니다.")

# 8. 복합 데이터 구조
print("\n=== 복합 데이터 구조 ===")

# 리스트 안의 딕셔너리
students = [
    {"name": "홍길동", "age": 20, "grades": [85, 90, 95]},
    {"name": "김철수", "age": 22, "grades": [75, 80, 85]},
    {"name": "이영희", "age": 21, "grades": [95, 95, 100]}
]
print(f"학생 리스트: {students}")

# 딕셔너리 안의 리스트와 딕셔너리
school = {
    "name": "파이썬 고등학교",
    "students": students,
    "departments": {
        "수학": {"teacher": "김수학", "students": 30},
        "과학": {"teacher": "이과학", "students": 25},
        "영어": {"teacher": "박영어", "students": 28}
    }
}
print(f"학교 정보: {school}")

# 복합 데이터 구조 접근
print(f"\n복합 데이터 구조 접근:")
print(f"첫 번째 학생 이름: {students[0]['name']}")
print(f"첫 번째 학생 첫 번째 성적: {students[0]['grades'][0]}")
print(f"수학 부서 교사: {school['departments']['수학']['teacher']}") 