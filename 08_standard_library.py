# 파이썬 표준 라이브러리

# 1. datetime 모듈
print("=== datetime 모듈 예제 ===")
from datetime import datetime, timedelta

now = datetime.now()
print(f"현재 시간: {now}")
print(f"년: {now.year}, 월: {now.month}, 일: {now.day}")
print(f"시: {now.hour}, 분: {now.minute}, 초: {now.second}")

# 시간 계산
tomorrow = now + timedelta(days=1)
print(f"내일: {tomorrow}")

# 2. json 모듈
print("\n=== json 모듈 예제 ===")
import json

# JSON 직렬화
data = {
    "name": "홍길동",
    "age": 25,
    "city": "서울",
    "hobbies": ["독서", "운동", "음악"]
}

json_str = json.dumps(data, ensure_ascii=False, indent=2)
print("JSON 문자열:")
print(json_str)

# JSON 역직렬화
parsed_data = json.loads(json_str)
print("\n파싱된 데이터:")
print(parsed_data)

# 3. random 모듈
print("\n=== random 모듈 예제 ===")
import random

# 랜덤 숫자 생성
print(f"1-10 사이의 랜덤 정수: {random.randint(1, 10)}")
print(f"0-1 사이의 랜덤 실수: {random.random()}")

# 리스트에서 랜덤 선택
items = ["사과", "바나나", "오렌지", "포도"]
print(f"랜덤 선택: {random.choice(items)}")
print(f"랜덤 샘플: {random.sample(items, 2)}")

# 4. os 모듈
print("\n=== os 모듈 예제 ===")
import os

# 현재 작업 디렉토리
print(f"현재 작업 디렉토리: {os.getcwd()}")

# 디렉토리 생성
os.makedirs("test_dir", exist_ok=True)

# 파일 경로 조작
path = os.path.join("test_dir", "test.txt")
print(f"생성된 경로: {path}")

# 5. sys 모듈
print("\n=== sys 모듈 예제 ===")
import sys

print(f"파이썬 버전: {sys.version}")
print(f"플랫폼: {sys.platform}")
print(f"모듈 검색 경로: {sys.path}")

# 6. collections 모듈
print("\n=== collections 모듈 예제 ===")
from collections import Counter, defaultdict, deque

# Counter
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = Counter(words)
print(f"단어 빈도: {word_count}")

# defaultdict
word_lengths = defaultdict(list)
for word in words:
    word_lengths[len(word)].append(word)
print(f"단어 길이별 그룹: {dict(word_lengths)}")

# deque
queue = deque(["첫번째", "두번째", "세번째"])
queue.append("네번째")
queue.appendleft("시작")
print(f"큐: {list(queue)}")

# 7. re 모듈 (정규표현식)
print("\n=== re 모듈 예제 ===")
import re

text = "이메일: user@example.com, 전화번호: 010-1234-5678"

# 이메일 찾기
email_pattern = r'[\w\.-]+@[\w\.-]+'
email = re.search(email_pattern, text)
print(f"찾은 이메일: {email.group()}")

# 전화번호 찾기
phone_pattern = r'\d{3}-\d{4}-\d{4}'
phone = re.search(phone_pattern, text)
print(f"찾은 전화번호: {phone.group()}")

# 8. logging 모듈
print("\n=== logging 모듈 예제 ===")
import logging

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 로그 메시지
logging.debug("디버그 메시지")
logging.info("정보 메시지")
logging.warning("경고 메시지")
logging.error("에러 메시지")
logging.critical("치명적 에러 메시지")

# 9. threading 모듈
print("\n=== threading 모듈 예제 ===")
import threading
import time

def worker(name, delay):
    print(f"{name} 시작")
    time.sleep(delay)
    print(f"{name} 완료")

# 스레드 생성 및 실행
thread1 = threading.Thread(target=worker, args=("스레드1", 1))
thread2 = threading.Thread(target=worker, args=("스레드2", 2))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

# 10. unittest 모듈
print("\n=== unittest 모듈 예제 ===")
import unittest

class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(3, 5), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 1), 0)

# 테스트 실행
if __name__ == '__main__':
    unittest.main() 