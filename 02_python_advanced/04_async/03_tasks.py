"""
태스크와 이벤트 루프
이 파일은 태스크와 이벤트 루프의 개념과 사용법을 다룹니다.
"""

import asyncio
from typing import List, Any
import time

class TaskExamples:
    """태스크 예제 클래스"""

    def __init__(self):
        pass

    async def basic_task(self) -> None:
        """기본 태스크 예제"""
        print("\n=== Basic Task ===")
        
        async def worker(name: str, delay: int) -> str:
            print(f"Worker {name} started")
            await asyncio.sleep(delay)
            print(f"Worker {name} finished")
            return f"Result from {name}"

        # 태스크 생성 및 실행
        task1 = asyncio.create_task(worker("A", 2))
        task2 = asyncio.create_task(worker("B", 1))
        
        # 태스크 결과 기다리기
        results = await asyncio.gather(task1, task2)
        print("Task results:", results)

    async def task_cancellation(self) -> None:
        """태스크 취소 예제"""
        print("\n=== Task Cancellation ===")
        
        async def long_running_task():
            try:
                print("Task started")
                await asyncio.sleep(10)
                print("Task completed")
            except asyncio.CancelledError:
                print("Task cancelled")
                raise

        # 태스크 생성 및 취소
        task = asyncio.create_task(long_running_task())
        await asyncio.sleep(1)
        task.cancel()
        
        try:
            await task
        except asyncio.CancelledError:
            print("Task was cancelled")

    async def task_timeout(self) -> None:
        """태스크 타임아웃 예제"""
        print("\n=== Task Timeout ===")
        
        async def slow_operation():
            print("Operation started")
            await asyncio.sleep(3)
            print("Operation completed")
            return "Result"

        try:
            # 타임아웃 설정
            result = await asyncio.wait_for(slow_operation(), timeout=2)
            print("Result:", result)
        except asyncio.TimeoutError:
            print("Operation timed out")

    async def task_priority(self) -> None:
        """태스크 우선순위 예제"""
        print("\n=== Task Priority ===")
        
        async def worker(name: str, priority: int):
            print(f"Worker {name} (priority {priority}) started")
            await asyncio.sleep(1)
            print(f"Worker {name} finished")
            return f"Result from {name}"

        # 우선순위에 따른 태스크 실행
        tasks = [
            asyncio.create_task(worker("High", 1)),
            asyncio.create_task(worker("Medium", 2)),
            asyncio.create_task(worker("Low", 3))
        ]
        
        # 태스크 완료 순서 확인
        for task in asyncio.as_completed(tasks):
            result = await task
            print("Completed:", result)

    async def event_loop_examples(self) -> None:
        """이벤트 루프 예제"""
        print("\n=== Event Loop Examples ===")
        
        # 현재 이벤트 루프 가져오기
        loop = asyncio.get_event_loop()
        
        # 이벤트 루프 정보 출력
        print("Event loop:", loop)
        print("Is running:", loop.is_running())
        print("Is closed:", loop.is_closed())

async def main():
    """메인 함수"""
    examples = TaskExamples()
    
    # 태스크 예제 실행
    await examples.basic_task()
    await examples.task_cancellation()
    await examples.task_timeout()
    await examples.task_priority()
    await examples.event_loop_examples()

if __name__ == "__main__":
    asyncio.run(main()) 