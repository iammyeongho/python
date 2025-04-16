"""
코루틴과 async/await
이 파일은 코루틴과 async/await의 개념과 사용법을 다룹니다.
"""

import asyncio
from typing import Generator, Any

class CoroutineExamples:
    """코루틴 예제 클래스"""

    def __init__(self):
        pass

    async def basic_coroutine(self) -> None:
        """기본 코루틴 예제"""
        print("\n=== Basic Coroutine ===")
        
        async def greet(name: str) -> str:
            await asyncio.sleep(1)
            return f"Hello, {name}!"

        result = await greet("Python")
        print(result)

    async def coroutine_chain(self) -> None:
        """코루틴 체이닝 예제"""
        print("\n=== Coroutine Chain ===")
        
        async def step1() -> int:
            await asyncio.sleep(1)
            return 1

        async def step2(value: int) -> int:
            await asyncio.sleep(1)
            return value + 1

        async def step3(value: int) -> int:
            await asyncio.sleep(1)
            return value * 2

        # 코루틴 체이닝
        result1 = await step1()
        result2 = await step2(result1)
        final_result = await step3(result2)
        print(f"Final result: {final_result}")

    async def coroutine_generator(self) -> None:
        """코루틴 제너레이터 예제"""
        print("\n=== Coroutine Generator ===")
        
        async def async_range(n: int) -> Generator[int, None, None]:
            for i in range(n):
                await asyncio.sleep(0.5)
                yield i

        # 비동기 제너레이터 사용
        async for number in async_range(5):
            print(f"Generated: {number}")

    async def coroutine_context(self) -> None:
        """코루틴 컨텍스트 매니저 예제"""
        print("\n=== Coroutine Context Manager ===")
        
        class AsyncResource:
            async def __aenter__(self):
                print("Acquiring resource...")
                await asyncio.sleep(1)
                return self

            async def __aexit__(self, exc_type, exc_val, exc_tb):
                print("Releasing resource...")
                await asyncio.sleep(1)

            async def use(self):
                print("Using resource...")
                await asyncio.sleep(1)

        # 비동기 컨텍스트 매니저 사용
        async with AsyncResource() as resource:
            await resource.use()

    async def coroutine_events(self) -> None:
        """코루틴 이벤트 예제"""
        print("\n=== Coroutine Events ===")
        
        async def waiter(event: asyncio.Event):
            print("Waiting for event...")
            await event.wait()
            print("Event received!")

        async def setter(event: asyncio.Event):
            print("Setting event...")
            await asyncio.sleep(2)
            event.set()

        # 이벤트 생성 및 사용
        event = asyncio.Event()
        await asyncio.gather(waiter(event), setter(event))

async def main():
    """메인 함수"""
    examples = CoroutineExamples()
    
    # 코루틴 예제 실행
    await examples.basic_coroutine()
    await examples.coroutine_chain()
    await examples.coroutine_generator()
    await examples.coroutine_context()
    await examples.coroutine_events()

if __name__ == "__main__":
    asyncio.run(main()) 