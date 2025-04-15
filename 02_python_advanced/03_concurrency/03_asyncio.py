"""
파이썬 동시성 프로그래밍: 비동기 프로그래밍
이 파일은 asyncio를 사용한 비동기 프로그래밍의 기본 개념을 설명합니다.
"""

import asyncio
import time
import random

# 1. 기본 코루틴
print("=== 기본 코루틴 ===")

async def say_hello(name):
    print(f"안녕하세요, {name}!")
    await asyncio.sleep(1)
    print(f"{name}님, 반갑습니다!")

async def main():
    # 여러 코루틴을 동시에 실행
    await asyncio.gather(
        say_hello("철수"),
        say_hello("영희"),
        say_hello("민수")
    )

# 이벤트 루프 실행
asyncio.run(main())

# 2. 비동기 작업
print("\n=== 비동기 작업 ===")

async def fetch_data(id):
    print(f"데이터 {id} 가져오는 중...")
    await asyncio.sleep(random.randint(1, 3))
    return f"데이터 {id}"

async def process_data():
    tasks = [fetch_data(i) for i in range(1, 4)]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(f"처리된 데이터: {result}")

asyncio.run(process_data())

# 3. 비동기 제너레이터
print("\n=== 비동기 제너레이터 ===")

async def async_range(start, end):
    for i in range(start, end):
        yield i
        await asyncio.sleep(0.5)

async def print_numbers():
    async for number in async_range(1, 6):
        print(f"숫자: {number}")

asyncio.run(print_numbers())

# 4. 비동기 컨텍스트 매니저
print("\n=== 비동기 컨텍스트 매니저 ===")

class AsyncResource:
    async def __aenter__(self):
        print("리소스 획득")
        await asyncio.sleep(1)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("리소스 해제")
        await asyncio.sleep(1)
    
    async def use(self):
        print("리소스 사용 중")
        await asyncio.sleep(1)

async def use_resource():
    async with AsyncResource() as resource:
        await resource.use()

asyncio.run(use_resource())

# 5. 비동기 이벤트
print("\n=== 비동기 이벤트 ===")

async def waiter(event):
    print("이벤트 대기 중...")
    await event.wait()
    print("이벤트 발생!")

async def setter(event):
    print("이벤트 설정 중...")
    await asyncio.sleep(2)
    event.set()
    print("이벤트 설정 완료")

async def event_example():
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))

asyncio.run(event_example())

print("\n프로그램 종료") 