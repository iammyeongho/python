# 파이썬 파일 처리와 예외 처리

# 1. 기본 파일 처리
print("=== 기본 파일 처리 ===")

# 파일 쓰기
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요!\n")
    f.write("파이썬 파일 처리 예제입니다.\n")
    f.write("여러 줄의 텍스트를 작성할 수 있습니다.")

# 파일 읽기
with open("example.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("파일 내용:")
    print(content)

# 파일에 추가하기
with open("example.txt", "a", encoding="utf-8") as f:
    f.write("\n이 줄은 추가된 내용입니다.")

# 파일 읽기 (줄 단위)
with open("example.txt", "r", encoding="utf-8") as f:
    print("\n줄 단위로 읽기:")
    for line in f:
        print(line.strip())

# 2. 다양한 파일 처리
print("\n=== 다양한 파일 처리 ===")

# CSV 파일 처리
import csv

# CSV 파일 쓰기
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["이름", "나이", "도시"])
    writer.writerow(["홍길동", 25, "서울"])
    writer.writerow(["김철수", 30, "부산"])
    writer.writerow(["이영희", 28, "대구"])

# CSV 파일 읽기
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    print("CSV 파일 내용:")
    for row in reader:
        print(row)

# JSON 파일 처리
import json

# JSON 파일 쓰기
data = {
    "이름": "홍길동",
    "나이": 25,
    "도시": "서울",
    "취미": ["독서", "운동", "음악"],
    "가족": {
        "아버지": "홍판서",
        "어머니": "홍씨",
        "형제": ["홍길순", "홍길칠"]
    }
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# JSON 파일 읽기
with open("data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    print("\nJSON 파일 내용:")
    print(json.dumps(loaded_data, ensure_ascii=False, indent=2))

# 3. 파일 시스템 작업
print("\n=== 파일 시스템 작업 ===")

import os
import shutil

# 디렉토리 생성
os.makedirs("test_dir/sub_dir", exist_ok=True)
print("디렉토리 생성됨: test_dir/sub_dir")

# 파일 복사
shutil.copy("example.txt", "test_dir/example_copy.txt")
print("파일 복사됨: example.txt -> test_dir/example_copy.txt")

# 파일 이동
shutil.move("data.csv", "test_dir/data.csv")
print("파일 이동됨: data.csv -> test_dir/data.csv")

# 디렉토리 내용 나열
print("\n디렉토리 내용:")
for item in os.listdir("test_dir"):
    print(f"- {item}")

# 파일 정보 확인
file_path = "test_dir/example_copy.txt"
print(f"\n파일 정보 ({file_path}):")
print(f"존재 여부: {os.path.exists(file_path)}")
print(f"파일 크기: {os.path.getsize(file_path)} 바이트")
print(f"수정 시간: {os.path.getmtime(file_path)}")
print(f"절대 경로: {os.path.abspath(file_path)}")

# 4. 기본 예외 처리
print("\n=== 기본 예외 처리 ===")

# try-except 블록
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다."
    except TypeError:
        return "숫자만 입력 가능합니다."

print(f"10 / 2 = {divide(10, 2)}")
print(f"10 / 0 = {divide(10, 0)}")
print(f"10 / '2' = {divide(10, '2')}")

# try-except-else 블록
def read_file_safely(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        return f"파일을 찾을 수 없습니다: {filename}"
    except IOError:
        return f"파일을 읽는 중 오류가 발생했습니다: {filename}"
    else:
        return f"파일을 성공적으로 읽었습니다. 내용 길이: {len(content)} 문자"

print(read_file_safely("example.txt"))
print(read_file_safely("nonexistent.txt"))

# try-except-finally 블록
def process_file(filename):
    f = None
    try:
        f = open(filename, "r", encoding="utf-8")
        content = f.read()
        return content
    except FileNotFoundError:
        return f"파일을 찾을 수 없습니다: {filename}"
    finally:
        if f:
            f.close()
            print("파일이 닫혔습니다.")

print(process_file("example.txt"))

# 5. 사용자 정의 예외
print("\n=== 사용자 정의 예외 ===")

class ValidationError(Exception):
    """데이터 검증 오류를 나타내는 예외"""
    pass

class AgeError(ValidationError):
    """나이 관련 오류를 나타내는 예외"""
    pass

class NameError(ValidationError):
    """이름 관련 오류를 나타내는 예외"""
    pass

def validate_person(name, age):
    if not name or len(name) < 2:
        raise NameError("이름은 최소 2자 이상이어야 합니다.")
    
    if not isinstance(age, int):
        raise ValidationError("나이는 정수여야 합니다.")
    
    if age < 0 or age > 150:
        raise AgeError("나이는 0에서 150 사이여야 합니다.")
    
    return True

# 예외 처리 예제
def register_person(name, age):
    try:
        validate_person(name, age)
        return f"등록 성공: {name}, {age}세"
    except NameError as e:
        return f"이름 오류: {e}"
    except AgeError as e:
        return f"나이 오류: {e}"
    except ValidationError as e:
        return f"검증 오류: {e}"

print(register_person("홍", 25))  # 이름 오류
print(register_person("홍길동", -5))  # 나이 오류
print(register_person("홍길동", "25"))  # 검증 오류
print(register_person("홍길동", 25))  # 성공

# 6. 컨텍스트 관리자
print("\n=== 컨텍스트 관리자 ===")

class FileManager:
    """파일 관리를 위한 컨텍스트 관리자"""
    
    def __init__(self, filename, mode="r", encoding="utf-8"):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding=self.encoding)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print(f"파일이 닫혔습니다: {self.filename}")
        
        # 예외 처리
        if exc_type is not None:
            print(f"오류 발생: {exc_val}")
            return True  # 예외를 처리했음을 나타냄

# 컨텍스트 관리자 사용
with FileManager("context_example.txt", "w") as f:
    f.write("컨텍스트 관리자 예제입니다.\n")
    f.write("with 문을 사용하면 자동으로 파일이 닫힙니다.")

with FileManager("context_example.txt", "r") as f:
    content = f.read()
    print("파일 내용:")
    print(content)

# 7. 예외 체인
print("\n=== 예외 체인 ===")

def process_data(data):
    try:
        result = int(data)
        return result
    except ValueError as e:
        raise RuntimeError("데이터 처리 중 오류가 발생했습니다.") from e

try:
    result = process_data("abc")
except RuntimeError as e:
    print(f"오류: {e}")
    print(f"원인: {e.__cause__}")

# 8. 예외 그룹
print("\n=== 예외 그룹 ===")

def validate_data(data_list):
    errors = []
    
    for i, data in enumerate(data_list):
        try:
            if not isinstance(data, str):
                raise TypeError(f"항목 {i}는 문자열이어야 합니다.")
            if len(data) < 2:
                raise ValueError(f"항목 {i}는 최소 2자 이상이어야 합니다.")
        except (TypeError, ValueError) as e:
            errors.append(e)
    
    if errors:
        raise ExceptionGroup("데이터 검증 오류", errors)
    
    return True

try:
    validate_data([1, "a", "홍길동", 3.14])
except ExceptionGroup as eg:
    print(f"발견된 오류 수: {len(eg.exceptions)}")
    for i, e in enumerate(eg.exceptions):
        print(f"오류 {i+1}: {e}")

# 9. 파일 시스템 예외 처리
print("\n=== 파일 시스템 예외 처리 ===")

def safe_file_operations():
    # 파일 생성 시도
    try:
        with open("test_file.txt", "w") as f:
            f.write("테스트 파일입니다.")
        print("파일이 생성되었습니다.")
    except IOError as e:
        print(f"파일 생성 오류: {e}")
    
    # 파일 복사 시도
    try:
        shutil.copy("test_file.txt", "test_file_copy.txt")
        print("파일이 복사되었습니다.")
    except IOError as e:
        print(f"파일 복사 오류: {e}")
    
    # 디렉토리 생성 시도
    try:
        os.makedirs("test_directory")
        print("디렉토리가 생성되었습니다.")
    except OSError as e:
        print(f"디렉토리 생성 오류: {e}")
    
    # 파일 삭제 시도
    try:
        os.remove("test_file.txt")
        print("파일이 삭제되었습니다.")
    except OSError as e:
        print(f"파일 삭제 오류: {e}")
    
    # 디렉토리 삭제 시도
    try:
        os.rmdir("test_directory")
        print("디렉토리가 삭제되었습니다.")
    except OSError as e:
        print(f"디렉토리 삭제 오류: {e}")

safe_file_operations()

# 10. 리소스 정리
print("\n=== 리소스 정리 ===")

class Resource:
    """리소스를 나타내는 클래스"""
    
    def __init__(self, name):
        self.name = name
        print(f"리소스 초기화: {name}")
    
    def use(self):
        print(f"리소스 사용 중: {self.name}")
    
    def close(self):
        print(f"리소스 정리: {self.name}")

class ResourceManager:
    """리소스 관리를 위한 컨텍스트 관리자"""
    
    def __init__(self, name):
        self.name = name
        self.resource = None
    
    def __enter__(self):
        self.resource = Resource(self.name)
        return self.resource
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.resource:
            self.resource.close()
        
        # 예외 처리
        if exc_type is not None:
            print(f"오류 발생: {exc_val}")
            return True  # 예외를 처리했음을 나타냄

# 리소스 관리자 사용
with ResourceManager("데이터베이스") as db:
    db.use()
    # 여기서 예외가 발생해도 리소스는 정리됨
    # raise Exception("테스트 예외")

print("프로그램 종료") 