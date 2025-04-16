"""
고급 비동기 프로그래밍
이 파일은 고급 비동기 프로그래밍 개념과 패턴을 다룹니다.
"""

import asyncio
from typing import Any, List, Dict, Optional
import time
import random
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import functools

class AdvancedAsyncExamples:
    """고급 비동기 프로그래밍 예제 클래스"""

    def __init__(self):
        self.thread_pool = ThreadPoolExecutor(max_workers=4)
        self.process_pool = ProcessPoolExecutor(max_workers=4)

    async def async_context_manager(self) -> None:
        """비동기 컨텍스트 매니저 예제"""
        print("\n=== Async Context Manager ===")
        
        class AsyncResource:
            def __init__(self, name: str):
                self.name = name

            async def __aenter__(self):
                print(f"Acquiring {self.name}")
                await asyncio.sleep(1)
                return self

            async def __aexit__(self, exc_type, exc_val, exc_tb):
                print(f"Releasing {self.name}")
                await asyncio.sleep(1)

        async with AsyncResource("Resource1") as resource:
            print(f"Using {resource.name}")
            await asyncio.sleep(2)

    async def async_iterator(self) -> None:
        """비동기 이터레이터 예제"""
        print("\n=== Async Iterator ===")
        
        class AsyncCounter:
            def __init__(self, limit: int):
                self.limit = limit
                self.counter = 0

            def __aiter__(self):
                return self

            async def __anext__(self):
                if self.counter < self.limit:
                    self.counter += 1
                    await asyncio.sleep(0.5)
                    return self.counter
                raise StopAsyncIteration

        async for number in AsyncCounter(5):
            print(f"Count: {number}")

    async def async_generator(self) -> None:
        """비동기 제너레이터 예제"""
        print("\n=== Async Generator ===")
        
        async def async_range(start: int, stop: int):
            for i in range(start, stop):
                await asyncio.sleep(0.5)
                yield i

        async for number in async_range(1, 6):
            print(f"Generated: {number}")

    async def thread_pool_execution(self) -> None:
        """스레드 풀 실행 예제"""
        print("\n=== Thread Pool Execution ===")
        
        def blocking_operation(n: int) -> int:
            time.sleep(1)
            return n * n

        loop = asyncio.get_running_loop()
        tasks = [
            loop.run_in_executor(self.thread_pool, blocking_operation, i)
            for i in range(5)
        ]
        results = await asyncio.gather(*tasks)
        print(f"Results: {results}")

    async def process_pool_execution(self) -> None:
        """프로세스 풀 실행 예제"""
        print("\n=== Process Pool Execution ===")
        
        def cpu_intensive(n: int) -> int:
            return sum(i * i for i in range(n))

        loop = asyncio.get_running_loop()
        tasks = [
            loop.run_in_executor(self.process_pool, cpu_intensive, i * 1000000)
            for i in range(1, 6)
        ]
        results = await asyncio.gather(*tasks)
        print(f"Results: {results}")

    async def async_timeout(self) -> None:
        """비동기 타임아웃 예제"""
        print("\n=== Async Timeout ===")
        
        async def long_running_task():
            await asyncio.sleep(2)
            return "Task completed"

        try:
            result = await asyncio.wait_for(long_running_task(), timeout=1.0)
            print(f"Result: {result}")
        except asyncio.TimeoutError:
            print("Task timed out")

    async def async_semaphore(self) -> None:
        """비동기 세마포어 예제"""
        print("\n=== Async Semaphore ===")
        
        sem = asyncio.Semaphore(2)

        async def worker(name: str):
            async with sem:
                print(f"Worker {name} acquired semaphore")
                await asyncio.sleep(1)
                print(f"Worker {name} released semaphore")

        tasks = [worker(f"Task-{i}") for i in range(5)]
        await asyncio.gather(*tasks)

    async def async_queue(self) -> None:
        """비동기 큐 예제"""
        print("\n=== Async Queue ===")
        
        queue = asyncio.Queue(maxsize=3)

        async def producer():
            for i in range(5):
                await queue.put(i)
                print(f"Produced: {i}")
                await asyncio.sleep(0.5)

        async def consumer():
            while True:
                item = await queue.get()
                print(f"Consumed: {item}")
                queue.task_done()
                if item == 4:
                    break

        await asyncio.gather(producer(), consumer())

async def main():
    """메인 함수"""
    examples = AdvancedAsyncExamples()
    
    # 고급 비동기 예제 실행
    await examples.async_context_manager()
    await examples.async_iterator()
    await examples.async_generator()
    await examples.thread_pool_execution()
    await examples.process_pool_execution()
    await examples.async_timeout()
    await examples.async_semaphore()
    await examples.async_queue()

if __name__ == "__main__":
    asyncio.run(main()) 