"""
파이썬 동시성 프로그래밍: 스레딩
이 파일은 스레딩의 기본 개념을 설명합니다.
"""

import threading
import time
import random

# 1. 기본 스레드 생성
print("=== 기본 스레드 생성 ===")

def worker(name):
    print(f"작업자 {name} 시작")
    time.sleep(random.randint(1, 3))
    print(f"작업자 {name} 종료")

# 스레드 생성 및 실행
threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

# 모든 스레드가 종료될 때까지 대기
for t in threads:
    t.join()

print("모든 스레드가 종료되었습니다.")

# 2. 스레드 동기화
print("\n=== 스레드 동기화 ===")

class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()
    
    def increment(self):
        with self.lock:
            self.value += 1

def increment_counter(counter, times):
    for _ in range(times):
        counter.increment()

# 공유 자원 생성
counter = Counter()
threads = []

# 여러 스레드에서 동시에 카운터 증가
for _ in range(5):
    t = threading.Thread(target=increment_counter, args=(counter, 100000))
    threads.append(t)
    t.start()

# 모든 스레드가 종료될 때까지 대기
for t in threads:
    t.join()

print(f"최종 카운터 값: {counter.value}")

# 3. 데몬 스레드
print("\n=== 데몬 스레드 ===")

def daemon_worker():
    while True:
        print("데몬 스레드 실행 중...")
        time.sleep(1)

# 데몬 스레드 생성
daemon = threading.Thread(target=daemon_worker)
daemon.daemon = True
daemon.start()

# 메인 스레드에서 3초간 대기
time.sleep(3)
print("메인 스레드 종료")

# 4. 스레드 풀
print("\n=== 스레드 풀 ===")

from concurrent.futures import ThreadPoolExecutor

def task(name):
    print(f"작업 {name} 시작")
    time.sleep(random.randint(1, 3))
    return f"작업 {name} 완료"

# 스레드 풀 생성 및 작업 실행
with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(task, f"Task-{i}") for i in range(5)]
    
    # 결과 수집
    for future in futures:
        print(future.result())

print("모든 작업이 완료되었습니다.")

# 5. 스레드 로컬 데이터
print("\n=== 스레드 로컬 데이터 ===")

thread_local = threading.local()

def show_thread_data():
    try:
        value = thread_local.value
    except AttributeError:
        print(f"스레드 {threading.current_thread().name}에 데이터가 없습니다.")
    else:
        print(f"스레드 {threading.current_thread().name}의 값: {value}")

def worker_with_data(value):
    thread_local.value = value
    show_thread_data()

# 여러 스레드에서 스레드 로컬 데이터 사용
threads = []
for i in range(3):
    t = threading.Thread(target=worker_with_data, args=(i,))
    threads.append(t)
    t.start()

# 모든 스레드가 종료될 때까지 대기
for t in threads:
    t.join()

print("\n프로그램 종료") 