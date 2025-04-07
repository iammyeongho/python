# 파일 입출력과 예외 처리

# 1. 파일 쓰기
print("=== 파일 쓰기 예제 ===")
try:
    with open("example.txt", "w", encoding="utf-8") as file:
        file.write("안녕하세요!\n")
        file.write("파이썬 파일 입출력 예제입니다.\n")
        file.write("한글도 잘 저장됩니다.")
    print("파일이 성공적으로 생성되었습니다.")
except IOError as e:
    print(f"파일 쓰기 오류: {e}")

# 2. 파일 읽기
print("\n=== 파일 읽기 예제 ===")
try:
    with open("example.txt", "r", encoding="utf-8") as file:
        # 한 줄씩 읽기
        print("한 줄씩 읽기:")
        for line in file:
            print(line.strip())
        
        # 파일 포인터를 처음으로 이동
        file.seek(0)
        
        # 전체 내용 읽기
        print("\n전체 내용 읽기:")
        content = file.read()
        print(content)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
except IOError as e:
    print(f"파일 읽기 오류: {e}")

# 3. 파일 추가하기
print("\n=== 파일 추가 예제 ===")
try:
    with open("example.txt", "a", encoding="utf-8") as file:
        file.write("\n새로운 내용이 추가됩니다.")
    print("파일이 성공적으로 수정되었습니다.")
except IOError as e:
    print(f"파일 추가 오류: {e}")

# 4. with 문 사용하기
print("\n=== with 문 예제 ===")
try:
    with open("example.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        print("파일의 모든 줄:")
        for line in lines:
            print(line.strip())
except IOError as e:
    print(f"파일 읽기 오류: {e}")

# 5. 예외 처리
print("\n=== 예외 처리 예제 ===")
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
        return None
    except TypeError:
        print("숫자만 입력해주세요.")
        return None
    except Exception as e:
        print(f"예상치 못한 오류 발생: {e}")
        return None

# 예외 처리 테스트
print(divide_numbers(10, 2))  # 정상 동작
print(divide_numbers(10, 0))  # 0으로 나누기
print(divide_numbers(10, "2"))  # 타입 오류

# 6. 사용자 정의 예외
print("\n=== 사용자 정의 예외 예제 ===")
class AgeError(Exception):
    pass

def verify_age(age):
    try:
        age = int(age)
        if age < 0:
            raise AgeError("나이는 음수일 수 없습니다.")
        if age > 150:
            raise AgeError("나이가 너무 큽니다.")
        return True
    except ValueError:
        print("올바른 숫자를 입력해주세요.")
        return False
    except AgeError as e:
        print(f"나이 오류: {e}")
        return False

# 사용자 정의 예외 테스트
verify_age(25)  # 정상 동작
verify_age(-5)  # 음수 나이
verify_age(200)  # 너무 큰 나이
verify_age("abc")  # 잘못된 입력 