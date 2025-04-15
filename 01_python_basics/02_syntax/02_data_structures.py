# 파이썬 데이터 구조 예제
# 작성일: 2024-04-08
# 목적: 파이썬의 기본 데이터 구조와 관련된 다양한 기능을 설명하는 예제 코드

# 1. 리스트 (List) | 인덱스 배열
# 리스트는 순서가 있는 가변 시퀀스입니다.
# - 인덱스로 접근 가능 (0부터 시작)
# - 요소 추가/삭제/수정 가능
# - 중복 요소 허용
print("=== 1. 리스트 (List) ===")

# 리스트 생성
empty_list = []  # 빈 리스트
numbers = [1, 2, 3, 4, 5]  # 숫자 리스트
mixed_list = [1, "hello", 3.14, True, [1, 2, 3]]  # 혼합 리스트
print(f"빈 리스트: {empty_list}")
print(f"숫자 리스트: {numbers}")
print(f"혼합 리스트: {mixed_list}")

# 리스트 인덱싱
# - 양수 인덱스: 앞에서부터 (0부터 시작)
# - 음수 인덱스: 뒤에서부터 (-1부터 시작)
print(f"\n리스트 인덱싱:")
print(f"첫 번째 요소: {numbers[0]}")  # 1
print(f"마지막 요소: {numbers[-1]}")  # 5
print(f"뒤에서 두 번째 요소: {numbers[-2]}")  # 4

# 리스트 슬라이싱
# list[start:end:step]
# - start: 시작 인덱스 (포함)
# - end: 끝 인덱스 (미포함)
# - step: 간격 (기본값 1)
print(f"\n리스트 슬라이싱:")
print(f"처음부터 3번 인덱스까지: {numbers[:3]}")  # [1, 2, 3]
print(f"2번 인덱스부터 끝까지: {numbers[2:]}")  # [3, 4, 5]
print(f"처음부터 끝까지 2칸씩: {numbers[::2]}")  # [1, 3, 5]
print(f"역순으로: {numbers[::-1]}")  # [5, 4, 3, 2, 1]

# 리스트 메서드
print(f"\n리스트 메서드:")
numbers.append(6)  # 맨 끝에 요소 추가
print(f"append(6) 후: {numbers}")

numbers.insert(1, 1.5)  # 특정 위치에 요소 삽입
print(f"insert(1, 1.5) 후: {numbers}")

numbers.extend([7, 8, 9])  # 리스트 확장
print(f"extend([7, 8, 9]) 후: {numbers}")

removed = numbers.pop()  # 맨 끝 요소 제거
print(f"pop() 후: {numbers}, 제거된 요소: {removed}")

removed = numbers.pop(1)  # 특정 위치 요소 제거
print(f"pop(1) 후: {numbers}, 제거된 요소: {removed}")

numbers.remove(3)  # 특정 값 제거
print(f"remove(3) 후: {numbers}")

index = numbers.index(4)  # 값의 인덱스 찾기
print(f"index(4): {index}")

count = numbers.count(2)  # 값의 개수 세기
print(f"count(2): {count}")

numbers.sort()  # 오름차순 정렬
print(f"sort() 후: {numbers}")

numbers.reverse()  # 역순 정렬
print(f"reverse() 후: {numbers}")

# 리스트 컴프리헨션
# [표현식 for 변수 in 시퀀스 if 조건]
print(f"\n리스트 컴프리헨션:")
squares = [x**2 for x in range(5)]  # 제곱수 리스트
print(f"제곱 리스트: {squares}")

even_squares = [x**2 for x in range(10) if x % 2 == 0]  # 짝수의 제곱
print(f"짝수의 제곱 리스트: {even_squares}")

# 2. 튜플 (Tuple) | 상수 배열
# 튜플은 순서가 있는 불변 시퀀스입니다.
# - 인덱스로 접근 가능 (0부터 시작)
# - 요소 추가/삭제/수정 불가능
# - 중복 요소 허용
print("\n=== 2. 튜플 (Tuple) ===")

# 튜플 생성
empty_tuple = ()  # 빈 튜플
single_tuple = (1,)  # 단일 요소 튜플 (쉼표 필요)
numbers_tuple = (1, 2, 3, 4, 5)  # 숫자 튜플
mixed_tuple = (1, "hello", 3.14, True, [1, 2, 3])  # 혼합 튜플

print(f"빈 튜플: {empty_tuple}")
print(f"단일 요소 튜플: {single_tuple}")
print(f"숫자 튜플: {numbers_tuple}")
print(f"혼합 튜플: {mixed_tuple}")

# 튜플은 불변(immutable)이므로 수정 불가
# numbers_tuple[0] = 10  # TypeError 발생

# 튜플 메서드
print(f"\n튜플 메서드:")
index = numbers_tuple.index(3)  # 값의 인덱스 찾기
print(f"index(3): {index}")

count = numbers_tuple.count(2)  # 값의 개수 세기
print(f"count(2): {count}")

# 튜플 언패킹
# 튜플의 요소를 여러 변수에 할당
print(f"\n튜플 언패킹:")
a, b, c, d, e = numbers_tuple
print(f"a={a}, b={b}, c={c}, d={d}, e={e}")

# 3. 딕셔너리 (Dictionary) | 연상 배열
# 딕셔너리는 키-값 쌍의 집합입니다.
# - 키로 접근 가능
# - 키는 고유해야 함 (중복 불가)
# - 값은 중복 가능
print("\n=== 3. 딕셔너리 (Dictionary) ===")

# 딕셔너리 생성
empty_dict = {}  # 빈 딕셔너리
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
print(f"이름: {person['name']}")  # 대괄호([])를 사용한 접근: 키가 없으면 KeyError 발생
print(f"나이: {person.get('age')}")  # get() 메서드를 사용한 접근: 키가 없으면 None 반환
print(f"존재하지 않는 키: {person.get('height', '정보 없음')}")  # get() 메서드에 기본값 지정: 키가 없으면 '정보 없음' 반환

# 접근 방식 비교
try:
    print(f"존재하지 않는 키 접근: {person['height']}")  # KeyError 발생
except KeyError:
    print("KeyError: 'height' 키가 존재하지 않습니다.")

print(f"get()으로 존재하지 않는 키 접근: {person.get('height')}")  # None 반환
print(f"get()으로 존재하지 않는 키 접근 (기본값 지정): {person.get('height', '정보 없음')}")  # '정보 없음' 반환

# 딕셔너리 수정
print(f"\n딕셔너리 수정:")
person["age"] = 26  # 값 수정
print(f"나이 수정 후: {person}")

person["height"] = 175  # 새 키-값 쌍 추가
print(f"키 추가 후: {person}")

del person["is_student"]  # 키-값 쌍 삭제
print(f"is_student 삭제 후: {person}")

# 딕셔너리 메서드
print(f"\n딕셔너리 메서드:")
print(f"키 목록: {list(person.keys())}")  # 모든 키
print(f"값 목록: {list(person.values())}")  # 모든 값
print(f"키-값 쌍 목록: {list(person.items())}")  # 모든 키-값 쌍

# 딕셔너리 컴프리헨션
# {키: 값 for 변수 in 시퀀스 if 조건}
print(f"\n딕셔너리 컴프리헨션:")
squares_dict = {x: x**2 for x in range(5)}  # 제곱수 딕셔너리
print(f"제곱 딕셔너리: {squares_dict}")

# 4. 집합 (Set) | 순차 배열
# 집합은 중복되지 않는 요소들의 집합입니다.
# - 순서 없음
# - 중복 요소 불가
# - 수정 가능
print("\n=== 4. 집합 (Set) ===")

# 집합 생성
empty_set = set()  # 빈 집합
numbers_set = {1, 2, 3, 4, 5}  # 숫자 집합
mixed_set = {1, "hello", 3.14, True}  # 혼합 집합
print(f"빈 집합: {empty_set}")
print(f"숫자 집합: {numbers_set}")
print(f"혼합 집합: {mixed_set}")

# 집합 연산
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"\n집합 연산:")
# 1. 합집합 (Union): 두 집합의 모든 요소를 포함 (중복 제외)
print(f"합집합: {set1 | set2}")  # {1, 2, 3, 4, 5, 6, 7, 8}
print(f"합집합 (union): {set1.union(set2)}")  # union() 메서드 사용

# 2. 교집합 (Intersection): 두 집합에 공통으로 있는 요소만 포함
print(f"교집합: {set1 & set2}")  # {4, 5}
print(f"교집합 (intersection): {set1.intersection(set2)}")  # intersection() 메서드 사용

# 3. 차집합 (Difference): 첫 번째 집합에는 있지만 두 번째 집합에는 없는 요소
print(f"차집합: {set1 - set2}")  # {1, 2, 3}
print(f"차집합 (difference): {set1.difference(set2)}")  # difference() 메서드 사용

# 4. 대칭차집합 (Symmetric Difference): 한 집합에만 있는 요소들의 합집합
print(f"대칭차집합: {set1 ^ set2}")  # {1, 2, 3, 6, 7, 8}
print(f"대칭차집합 (symmetric_difference): {set1.symmetric_difference(set2)}")  # symmetric_difference() 메서드 사용

# 5. 부분집합과 상위집합 확인
print(f"\n부분집합과 상위집합:")
subset = {1, 2, 3}
print(f"{subset}는 {set1}의 부분집합인가? {subset.issubset(set1)}")  # True
print(f"{set1}는 {subset}의 상위집합인가? {set1.issuperset(subset)}")  # True

# 6. 서로소 집합 확인 (교집합이 없는지)
print(f"\n서로소 집합 확인:")
disjoint_set = {6, 7, 8}
print(f"{subset}와 {disjoint_set}는 서로소인가? {subset.isdisjoint(disjoint_set)}")  # True

# 7. 집합 연산의 결과를 새로운 집합으로 저장
union_set = set1 | set2
intersection_set = set1 & set2
difference_set = set1 - set2
symmetric_difference_set = set1 ^ set2

print(f"\n집합 연산 결과 저장:")
print(f"합집합: {union_set}")
print(f"교집합: {intersection_set}")
print(f"차집합: {difference_set}")
print(f"대칭차집합: {symmetric_difference_set}")

# 집합 메서드
print(f"\n집합 메서드:")
numbers_set.add(6)  # 요소 추가
print(f"add(6) 후: {numbers_set}")

numbers_set.update([7, 8, 9])  # 여러 요소 추가
print(f"update([7, 8, 9]) 후: {numbers_set}")

numbers_set.remove(1)  # 요소 제거 (없으면 에러)
print(f"remove(1) 후: {numbers_set}")

numbers_set.discard(10)  # 요소 제거 (없어도 에러 없음)
print(f"discard(10) 후: {numbers_set}")

popped = numbers_set.pop()  # 무작위 요소 제거
print(f"pop() 후: {numbers_set}, 제거된 요소: {popped}")

numbers_set.clear()  # 모든 요소 제거
print(f"clear() 후: {numbers_set}")

# 집합 컴프리헨션
# {표현식 for 변수 in 시퀀스 if 조건}
print(f"\n집합 컴프리헨션:")
squares_set = {x**2 for x in range(5)}  # 제곱수 집합
print(f"제곱 집합: {squares_set}")

# 5. 문자열 (String)
# 문자열은 문자들의 시퀀스입니다.
# - 인덱스로 접근 가능 (0부터 시작)
# - 불변(immutable)
print("\n=== 5. 문자열 (String) ===")

# 문자열 생성
empty_string = ""  # 빈 문자열
hello = "안녕하세요"  # 기본 문자열
multi_line = """여러 줄
문자열
입니다."""  # 여러 줄 문자열

print(f"빈 문자열: '{empty_string}'")
print(f"인사: {hello}")
print(f"여러 줄 문자열: {multi_line}")

# 문자열 메서드
print(f"\n문자열 메서드:")
print(f"대문자 변환: {'hello'.upper()}")  # HELLO
print(f"소문자 변환: {'HELLO'.lower()}")  # hello
print(f"첫 글자 대문자: {'hello'.capitalize()}")  # Hello
print(f"각 단어 첫 글자 대문자: {'hello world'.title()}")  # Hello World
print(f"좌우 공백 제거: {'  hello  '.strip()}")  # hello
print(f"좌측 공백 제거: {'  hello  '.lstrip()}")  # hello  
print(f"우측 공백 제거: {'  hello  '.rstrip()}")  #   hello
print(f"문자열 치환: {'hello world'.replace('world', 'python')}")  # hello python
print(f"문자열 분할: {'hello,world,python'.split(',')}")  # ['hello', 'world', 'python']
print(f"문자열 결합: {','.join(['hello', 'world', 'python'])}")  # hello,world,python
print(f"문자열 시작 확인: {'hello'.startswith('he')}")  # True
print(f"문자열 끝 확인: {'hello'.endswith('lo')}")  # True
print(f"문자열 포함 확인: {'hello'.find('ll')}")  # 2 (인덱스)
print(f"문자열 포함 확인: {'hello'.count('l')}")  # 2 (개수)

# 6. 바이트 (Bytes)와 바이트 배열 (Bytearray)
# 바이트는 바이트들의 시퀀스입니다.
# - 불변(immutable)
# - 바이트 배열은 가변(mutable)
print("\n=== 6. 바이트 (Bytes)와 바이트 배열 (Bytearray) ===")

# 바이트 생성
byte_data = b'Hello'  # 바이트 문자열
print(f"바이트: {byte_data}")
print(f"바이트 타입: {type(byte_data)}")

# 바이트 배열 생성
bytearray_data = bytearray(b'Hello')  # 바이트 배열
print(f"바이트 배열: {bytearray_data}")
print(f"바이트 배열 타입: {type(bytearray_data)}")

# 바이트 배열은 수정 가능
bytearray_data[0] = 74  # 'J'의 ASCII 코드
print(f"수정된 바이트 배열: {bytearray_data}")

# 7. None 타입
# None은 값이 없음을 나타내는 특수 타입입니다.
print("\n=== 7. None 타입 ===")

none_value = None
print(f"None 값: {none_value}")
print(f"None 타입: {type(none_value)}")

# None은 False로 평가됨
if None:
    print("None은 True로 평가됩니다.")
else:
    print("None은 False로 평가됩니다.")

# 8. 복합 데이터 구조
# 데이터 구조 안에 다른 데이터 구조를 포함할 수 있습니다.
print("\n=== 8. 복합 데이터 구조 ===")

# 리스트 안의 딕셔너리
students = [
    {"name": "홍길동", "age": 20, "grades": [85, 90, 95]},
    {"name": "김철수", "age": 22, "grades": [75, 80, 85]},
    {"name": "이영희", "age": 21, "grades": [95, 95, 100]}
]
print(f"학생 리스트: {students}")

# 딕셔너리 안의 리스트와 딕셔너리 | 2차원 배열
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
print(f"첫 번째 학생 이름: {students[0]['name']}")  # 리스트 인덱스 + 딕셔너리 키
print(f"첫 번째 학생 첫 번째 성적: {students[0]['grades'][0]}")  # 리스트 인덱스 + 딕셔너리 키 + 리스트 인덱스
print(f"수학 부서 교사: {school['departments']['수학']['teacher']}")  # 딕셔너리 키 + 딕셔너리 키 + 딕셔너리 키

print("\n프로그램 종료") 