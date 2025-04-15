"""
파이썬 동시성 프로그래밍: 멀티프로세싱
이 파일은 멀티프로세싱의 기본 개념을 설명합니다.
"""

import multiprocessing
import time
import random
import os

# 1. 기본 프로세스 생성
print("=== 기본 프로세스 생성 ===")

def worker(name):
    print(f"프로세스 {name} (PID: {os.getpid()}) 시작")
    time.sleep(random.randint(1, 3))
    print(f"프로세스 {name} (PID: {os.getpid()}) 종료")

# 프로세스 생성 및 실행
processes = []
for i in range(3):
    p = multiprocessing.Process(target=worker, args=(f"Process-{i}",))
    processes.append(p)
    p.start()

# 모든 프로세스가 종료될 때까지 대기
for p in processes:
    p.join()

print("모든 프로세스가 종료되었습니다.")

# 2. 프로세스 간 통신
print("\n=== 프로세스 간 통신 ===")

def sender(conn):
    messages = ["안녕하세요", "반갑습니다", "잘 부탁드립니다"]
    for msg in messages:
        print(f"송신: {msg}")
        conn.send(msg)
        time.sleep(1)
    conn.close()

def receiver(conn):
    while True:
        try:
            msg = conn.recv()
            print(f"수신: {msg}")
        except EOFError:
            break

# 파이프 생성
parent_conn, child_conn = multiprocessing.Pipe()

# 프로세스 생성 및 실행
p1 = multiprocessing.Process(target=sender, args=(parent_conn,))
p2 = multiprocessing.Process(target=receiver, args=(child_conn,))

p1.start()
p2.start()

p1.join()
p2.join()

# 3. 공유 메모리
print("\n=== 공유 메모리 ===")

def increment_counter(counter):
    for _ in range(100000):
        counter.value += 1

# 공유 카운터 생성
counter = multiprocessing.Value('i', 0)
processes = []

# 여러 프로세스에서 동시에 카운터 증가
for _ in range(5):
    p = multiprocessing.Process(target=increment_counter, args=(counter,))
    processes.append(p)
    p.start()

# 모든 프로세스가 종료될 때까지 대기
for p in processes:
    p.join()

print(f"최종 카운터 값: {counter.value}")

# 4. 프로세스 풀
print("\n=== 프로세스 풀 ===")

def task(name):
    print(f"작업 {name} (PID: {os.getpid()}) 시작")
    time.sleep(random.randint(1, 3))
    return f"작업 {name} 완료"

# 프로세스 풀 생성 및 작업 실행
with multiprocessing.Pool(processes=3) as pool:
    results = pool.map(task, [f"Task-{i}" for i in range(5)])
    
    # 결과 출력
    for result in results:
        print(result)

print("모든 작업이 완료되었습니다.")

# 5. 프로세스 간 동기화
print("\n=== 프로세스 간 동기화 ===")

def worker_with_lock(lock, name):
    with lock:
        print(f"프로세스 {name}이(가) 임계 영역에 진입했습니다.")
        time.sleep(1)
        print(f"프로세스 {name}이(가) 임계 영역을 떠났습니다.")

# 락 생성
lock = multiprocessing.Lock()
processes = []

# 여러 프로세스에서 락 사용
for i in range(3):
    p = multiprocessing.Process(target=worker_with_lock, args=(lock, f"Process-{i}"))
    processes.append(p)
    p.start()

# 모든 프로세스가 종료될 때까지 대기
for p in processes:
    p.join()

print("\n프로그램 종료") 