"""
Future 객체와 콜백
이 파일은 Future 객체와 콜백의 개념과 사용법을 다룹니다.
"""

import asyncio
from typing import Callable, Any
import time

class FutureExamples:
    """Future 예제 클래스"""

    def __init__(self):
        pass

    async def basic_future(self) -> None:
        """기본 Future 예제"""
        print("\n=== Basic Future ===")
        
        # Future 객체 생성
        future = asyncio.Future()
        
        # Future 완료 설정
        future.set_result("Future completed!")
        
        # Future 결과 가져오기
        result = await future
        print("Future result:", result)

    async def future_callback(self) -> None:
        """Future 콜백 예제"""
        print("\n=== Future Callback ===")
        
        def callback(fut: asyncio.Future):
            print("Callback called with result:", fut.result())

        # Future 객체 생성
        future = asyncio.Future()
        
        # 콜백 추가
        future.add_done_callback(callback)
        
        # Future 완료 설정
        future.set_result("Callback result")

    async def future_exception(self) -> None:
        """Future 예외 처리 예제"""
        print("\n=== Future Exception ===")
        
        # Future 객체 생성
        future = asyncio.Future()
        
        # 예외 설정
        future.set_exception(ValueError("Something went wrong"))
        
        try:
            # Future 결과 가져오기 (예외 발생)
            result = await future
        except ValueError as e:
            print("Caught exception:", e)

    async def future_cancellation(self) -> None:
        """Future 취소 예제"""
        print("\n=== Future Cancellation ===")
        
        # Future 객체 생성
        future = asyncio.Future()
        
        # Future 취소
        future.cancel()
        
        try:
            # Future 결과 가져오기 (취소됨)
            result = await future
        except asyncio.CancelledError:
            print("Future was cancelled")

    async def future_timeout(self) -> None:
        """Future 타임아웃 예제"""
        print("\n=== Future Timeout ===")
        
        async def slow_operation():
            await asyncio.sleep(3)
            return "Operation completed"

        # Future 생성 및 타임아웃 설정
        try:
            result = await asyncio.wait_for(slow_operation(), timeout=2)
            print("Result:", result)
        except asyncio.TimeoutError:
            print("Operation timed out")

    async def future_gather(self) -> None:
        """Future gather 예제"""
        print("\n=== Future Gather ===")
        
        async def task(name: str, delay: int):
            print(f"Task {name} started")
            await asyncio.sleep(delay)
            print(f"Task {name} completed")
            return f"Result from {name}"

        # 여러 Future 생성
        futures = [
            asyncio.create_task(task("A", 2)),
            asyncio.create_task(task("B", 1)),
            asyncio.create_task(task("C", 3))
        ]
        
        # 모든 Future 완료 대기
        results = await asyncio.gather(*futures)
        print("All results:", results)

async def main():
    """메인 함수"""
    examples = FutureExamples()
    
    # Future 예제 실행
    await examples.basic_future()
    await examples.future_callback()
    await examples.future_exception()
    await examples.future_cancellation()
    await examples.future_timeout()
    await examples.future_gather()

if __name__ == "__main__":
    asyncio.run(main()) 