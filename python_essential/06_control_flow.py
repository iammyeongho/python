# 파이썬 제어 흐름 예제
# 작성일: 2024-04-08
# 목적: 파이썬의 제어 흐름과 관련된 다양한 기능을 설명하는 예제 코드

# 1. 조건문 (if-elif-else)
# 조건에 따라 다른 코드를 실행합니다.
print("=== 1. 조건문 (if-elif-else) ===")

# 기본 if 문
age = 20
if age >= 18:
    print("성인입니다.")
else:
    print("미성년자입니다.")

# if-elif-else 문
score = 85
if score >= 90:
    print("A 등급")
elif score >= 80:
    print("B 등급")
elif score >= 70:
    print("C 등급")
else:
    print("D 등급")

# 중첩 if 문
age = 20
has_ticket = True
if age >= 18:
    if has_ticket:
        print("입장 가능합니다.")
    else:
        print("티켓이 필요합니다.")
else:
    print("미성년자는 입장할 수 없습니다.")

# 2. 반복문 (for)
# 시퀀스의 각 요소에 대해 반복합니다.
print("\n=== 2. 반복문 (for) ===")

# 기본 for 문
for i in range(5):
    print(f"i: {i}")

# 리스트 순회
fruits = ["사과", "바나나", "오렌지"]
for fruit in fruits:
    print(f"과일: {fruit}")

# 딕셔너리 순회
person = {"name": "홍길동", "age": 25, "city": "서울"}
for key in person:
    print(f"키: {key}, 값: {person[key]}")

for key, value in person.items():
    print(f"키: {key}, 값: {value}")

# enumerate() 사용
for index, fruit in enumerate(fruits):
    print(f"인덱스: {index}, 과일: {fruit}")

# 3. 반복문 (while)
# 조건이 참인 동안 반복합니다.
print("\n=== 3. 반복문 (while) ===")

# 기본 while 문
count = 0
while count < 5:
    print(f"count: {count}")
    count += 1

# break 문
count = 0
while True:
    if count >= 5:
        break
    print(f"count: {count}")
    count += 1

# continue 문
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"홀수: {i}")

# 4. 예외 처리 (try-except)
# 예외가 발생했을 때 처리합니다.
print("\n=== 4. 예외 처리 (try-except) ===")

# 기본 예외 처리
try:
    number = int("abc")
except ValueError:
    print("숫자로 변환할 수 없습니다.")

# 여러 예외 처리
try:
    number = int("abc")
    result = 10 / number
except ValueError:
    print("숫자로 변환할 수 없습니다.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except Exception as e:
    print(f"예외 발생: {e}")

# else 절
try:
    number = int("123")
    print("변환 성공")
except ValueError:
    print("숫자로 변환할 수 없습니다.")
else:
    print("예외가 발생하지 않았습니다.")

# finally 절
try:
    file = open("test.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
finally:
    print("파일을 닫습니다.")
    file.close()

# 5. 컨텍스트 매니저 (with)
# 리소스를 자동으로 관리합니다.
print("\n=== 5. 컨텍스트 매니저 (with) ===")

# 파일 처리
with open("test.txt", "w") as file:
    file.write("Hello, Python!")

# 6. 제너레이터 (Generator)
# 값을 하나씩 생성하는 함수입니다.
print("\n=== 6. 제너레이터 (Generator) ===")

# 제너레이터 함수
def count_up_to(n):
    i = 0
    while i <= n:
        yield i
        i += 1

# 제너레이터 사용
for number in count_up_to(5):
    print(f"숫자: {number}")

# 7. 데코레이터 (Decorator)
# 함수를 수정하는 함수입니다.
print("\n=== 7. 데코레이터 (Decorator) ===")

# 기본 데코레이터
def timer(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"실행 시간: {end - start}초")
        return result
    return wrapper

# 데코레이터 사용
@timer
def slow_function():
    import time
    time.sleep(1)
    print("함수 실행 완료")

slow_function()

# 8. 컨텍스트 매니저 클래스
# with 문에서 사용할 수 있는 클래스입니다.
print("\n=== 8. 컨텍스트 매니저 클래스 ===")

class Timer:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        end = time.time()
        print(f"{self.name} 실행 시간: {end - self.start}초")

# 컨텍스트 매니저 사용
with Timer("작업") as timer:
    import time
    time.sleep(1)
    print("작업 완료")

print("\n프로그램 종료") 