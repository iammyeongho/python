"""
파이썬 동시성 프로그래밍: concurrent.futures
이 파일은 concurrent.futures를 사용한 고수준 동시성 프로그래밍의 기본 개념을 설명합니다.
"""

import concurrent.futures
import time
import random
import math

# 1. ThreadPoolExecutor
print("=== ThreadPoolExecutor ===")

def task(name):
    print(f"작업 {name} 시작")
    time.sleep(random.randint(1, 3))
    return f"작업 {name} 완료"

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # 작업 제출
    futures = [executor.submit(task, i) for i in range(1, 4)]
    
    # 결과 처리
    for future in concurrent.futures.as_completed(futures):
        print(future.result())

# 2. ProcessPoolExecutor
print("\n=== ProcessPoolExecutor ===")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(start, end):
    primes = []
    for i in range(start, end):
        if is_prime(i):
            primes.append(i)
    return primes

# 프로세스 풀 생성
with concurrent.futures.ProcessPoolExecutor() as executor:
    # 작업 분할
    ranges = [(1, 1000), (1000, 2000), (2000, 3000)]
    futures = [executor.submit(find_primes, start, end) 
              for start, end in ranges]
    
    # 결과 수집
    all_primes = []
    for future in concurrent.futures.as_completed(futures):
        primes = future.result()
        all_primes.extend(primes)
        print(f"찾은 소수 개수: {len(primes)}")

    print(f"총 소수 개수: {len(all_primes)}")

# 3. map 메서드 사용
print("\n=== map 메서드 사용 ===")

def square(x):
    return x * x

with concurrent.futures.ThreadPoolExecutor() as executor:
    # map을 사용한 병렬 처리
    results = executor.map(square, range(1, 6))
    for result in results:
        print(f"제곱 결과: {result}")

# 4. 타임아웃 설정
print("\n=== 타임아웃 설정 ===")

def long_running_task(seconds):
    time.sleep(seconds)
    return f"{seconds}초 작업 완료"

with concurrent.futures.ThreadPoolExecutor() as executor:
    future = executor.submit(long_running_task, 5)
    try:
        result = future.result(timeout=3)  # 3초 타임아웃
        print(result)
    except concurrent.futures.TimeoutError:
        print("작업이 타임아웃되었습니다.")

# 5. 콜백 함수
print("\n=== 콜백 함수 ===")

def callback(future):
    print(f"콜백: {future.result()}")

with concurrent.futures.ThreadPoolExecutor() as executor:
    future = executor.submit(task, "콜백 테스트")
    future.add_done_callback(callback)

print("\n프로그램 종료") 