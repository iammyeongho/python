# 파이썬 데이터 구조

# 1. 리스트 (List)
print("=== 리스트 예제 ===")
# 리스트 생성
numbers = [1, 2, 3, 4, 5]
fruits = ["사과", "바나나", "오렌지"]

# 리스트 조작
fruits.append("포도")  # 추가
fruits.insert(1, "키위")  # 삽입
fruits.remove("바나나")  # 삭제
popped = fruits.pop()  # 마지막 요소 제거

print(f"과일 목록: {fruits}")
print(f"제거된 과일: {popped}")

# 리스트 슬라이싱
print(f"numbers[1:3]: {numbers[1:3]}")
print(f"numbers[:3]: {numbers[:3]}")
print(f"numbers[2:]: {numbers[2:]}")

# 2. 튜플 (Tuple)
print("\n=== 튜플 예제 ===")
# 튜플 생성
coordinates = (10, 20)
person = ("홍길동", 25, "서울")

# 튜플 언패킹
name, age, city = person
print(f"이름: {name}, 나이: {age}, 도시: {city}")

# 3. 딕셔너리 (Dictionary)
print("\n=== 딕셔너리 예제 ===")
# 딕셔너리 생성
student = {
    "name": "홍길동",
    "age": 20,
    "grades": {"국어": 90, "수학": 85, "영어": 95}
}

# 딕셔너리 조작
student["email"] = "hong@example.com"  # 추가
del student["age"]  # 삭제
grades = student.get("grades")  # 값 가져오기

print(f"학생 정보: {student}")
print(f"성적: {grades}")

# 4. 집합 (Set)
print("\n=== 집합 예제 ===")
# 집합 생성
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 집합 연산
print(f"합집합: {set1 | set2}")
print(f"교집합: {set1 & set2}")
print(f"차집합: {set1 - set2}")
print(f"대칭차집합: {set1 ^ set2}")

# 5. 리스트 컴프리헨션
print("\n=== 리스트 컴프리헨션 예제 ===")
squares = [x**2 for x in range(5)]
even_numbers = [x for x in range(10) if x % 2 == 0]
print(f"제곱 수: {squares}")
print(f"짝수: {even_numbers}")

# 6. 딕셔너리 컴프리헨션
print("\n=== 딕셔너리 컴프리헨션 예제 ===")
square_dict = {x: x**2 for x in range(5)}
print(f"제곱 딕셔너리: {square_dict}")

# 7. 중첩 데이터 구조
print("\n=== 중첩 데이터 구조 예제 ===")
classroom = {
    "수학": {
        "홍길동": 85,
        "김철수": 92,
        "이영희": 78
    },
    "과학": {
        "홍길동": 90,
        "김철수": 88,
        "이영희": 95
    }
}

print(f"홍길동의 수학 점수: {classroom['수학']['홍길동']}")
print(f"이영희의 과학 점수: {classroom['과학']['이영희']}") 