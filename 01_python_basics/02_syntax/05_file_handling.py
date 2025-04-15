# 파이썬 파일 처리 예제
# 작성일: 2024-04-08
# 목적: 파이썬의 파일 처리와 관련된 다양한 기능을 설명하는 예제 코드

# 1. 기본 파일 읽기/쓰기
# 파일을 읽고 쓰는 기본적인 방법을 보여줍니다.
print("=== 1. 기본 파일 읽기/쓰기 ===")

# 파일 쓰기
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요!\n")
    f.write("파이썬 파일 처리 예제입니다.\n")
    f.write("한글도 잘 저장됩니다.")

# 파일 읽기
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("파일 내용:")
    print(content)

# 2. 파일 모드
# 다양한 파일 모드를 사용하는 방법을 보여줍니다.
print("\n=== 2. 파일 모드 ===")

# 추가 모드 (a)
with open("test.txt", "a", encoding="utf-8") as f:
    f.write("\n추가된 내용입니다.")

# 읽기 모드 (r)
with open("test.txt", "r", encoding="utf-8") as f:
    print("추가 후 파일 내용:")
    print(f.read())

# 3. 파일 메서드
# 파일 객체의 다양한 메서드를 사용하는 방법을 보여줍니다.
print("\n=== 3. 파일 메서드 ===")

with open("test.txt", "r", encoding="utf-8") as f:
    # 한 줄씩 읽기
    print("한 줄씩 읽기:")
    for line in f:
        print(line.strip())

with open("test.txt", "r", encoding="utf-8") as f:
    # 모든 줄을 리스트로 읽기
    lines = f.readlines()
    print("\n모든 줄을 리스트로 읽기:")
    for line in lines:
        print(line.strip())

# 4. 파일 포인터 조작
# 파일 포인터를 조작하는 방법을 보여줍니다.
print("\n=== 4. 파일 포인터 조작 ===")

with open("test.txt", "r", encoding="utf-8") as f:
    # 처음 5바이트 읽기
    print("처음 5바이트:", f.read(5))
    
    # 파일 포인터 이동
    f.seek(0)
    print("파일 포인터를 처음으로 이동 후:", f.read(5))
    
    # 파일 포인터를 끝에서 10바이트 앞으로 이동
    f.seek(-10, 2)
    print("파일 끝에서 10바이트 앞:", f.read())

# 5. 바이너리 파일 처리
# 바이너리 파일을 처리하는 방법을 보여줍니다.
print("\n=== 5. 바이너리 파일 처리 ===")

# 바이너리 파일 쓰기
with open("binary.bin", "wb") as f:
    f.write(bytes([65, 66, 67, 68, 69]))  # ASCII: ABCDE

# 바이너리 파일 읽기
with open("binary.bin", "rb") as f:
    binary_data = f.read()
    print("바이너리 데이터:", binary_data)
    print("문자로 변환:", binary_data.decode('ascii'))

# 6. CSV 파일 처리
# CSV 파일을 처리하는 방법을 보여줍니다.
print("\n=== 6. CSV 파일 처리 ===")

import csv

# CSV 파일 쓰기
with open("data.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["이름", "나이", "도시"])
    writer.writerow(["홍길동", 25, "서울"])
    writer.writerow(["김철수", 30, "부산"])
    writer.writerow(["이영희", 28, "인천"])

# CSV 파일 읽기
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    print("CSV 파일 내용:")
    for row in reader:
        print(row)

# 7. JSON 파일 처리
# JSON 파일을 처리하는 방법을 보여줍니다.
print("\n=== 7. JSON 파일 처리 ===")

import json

# JSON 파일 쓰기
data = {
    "이름": "홍길동",
    "나이": 25,
    "도시": "서울",
    "취미": ["독서", "운동", "음악"]
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# JSON 파일 읽기
with open("data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    print("JSON 파일 내용:")
    print(json.dumps(loaded_data, ensure_ascii=False, indent=4))

# 8. 파일 및 디렉토리 작업
# 파일과 디렉토리를 관리하는 방법을 보여줍니다.
print("\n=== 8. 파일 및 디렉토리 작업 ===")

import os

# 현재 작업 디렉토리
print("현재 작업 디렉토리:", os.getcwd())

# 디렉토리 생성
os.makedirs("test_dir", exist_ok=True)
print("디렉토리 생성됨: test_dir")

# 파일 이동
with open("test_dir/moved.txt", "w", encoding="utf-8") as f:
    f.write("이동된 파일입니다.")
print("파일 생성됨: test_dir/moved.txt")

# 파일 복사
import shutil
shutil.copy("test.txt", "test_dir/copied.txt")
print("파일 복사됨: test_dir/copied.txt")

# 파일 삭제
os.remove("test_dir/moved.txt")
print("파일 삭제됨: test_dir/moved.txt")

# 디렉토리 삭제
shutil.rmtree("test_dir")
print("디렉토리 삭제됨: test_dir")

# 9. 파일 경로 처리
# 파일 경로를 처리하는 방법을 보여줍니다.
print("\n=== 9. 파일 경로 처리 ===")

# 경로 결합
path = os.path.join("folder", "subfolder", "file.txt")
print("결합된 경로:", path)

# 경로 분리
dirname, filename = os.path.split(path)
print("디렉토리:", dirname)
print("파일명:", filename)

# 파일 확장자 분리
name, ext = os.path.splitext(filename)
print("파일명:", name)
print("확장자:", ext)

# 절대 경로
abs_path = os.path.abspath("test.txt")
print("절대 경로:", abs_path)

print("\n프로그램 종료") 