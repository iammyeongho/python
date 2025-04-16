"""
비동기 스트림
이 파일은 비동기 스트림의 개념과 사용법을 다룹니다.
"""

import asyncio
from typing import AsyncGenerator, Any
import time

class StreamExamples:
    """스트림 예제 클래스"""

    def __init__(self):
        pass

    async def basic_stream(self) -> None:
        """기본 스트림 예제"""
        print("\n=== Basic Stream ===")
        
        async def number_stream(n: int) -> AsyncGenerator[int, None]:
            for i in range(n):
                await asyncio.sleep(0.5)
                yield i

        # 스트림 사용
        async for number in number_stream(5):
            print(f"Received: {number}")

    async def stream_pipeline(self) -> None:
        """스트림 파이프라인 예제"""
        print("\n=== Stream Pipeline ===")
        
        async def number_generator(n: int) -> AsyncGenerator[int, None]:
            for i in range(n):
                await asyncio.sleep(0.5)
                yield i

        async def square_stream(numbers: AsyncGenerator[int, None]) -> AsyncGenerator[int, None]:
            async for number in numbers:
                yield number ** 2

        async def filter_stream(numbers: AsyncGenerator[int, None]) -> AsyncGenerator[int, None]:
            async for number in numbers:
                if number % 2 == 0:
                    yield number

        # 스트림 파이프라인 구성
        numbers = number_generator(5)
        squares = square_stream(numbers)
        evens = filter_stream(squares)

        # 파이프라인 실행
        async for result in evens:
            print(f"Pipeline result: {result}")

    async def stream_reader_writer(self) -> None:
        """스트림 리더/라이터 예제"""
        print("\n=== Stream Reader/Writer ===")
        
        async def writer(stream: asyncio.StreamWriter):
            for i in range(5):
                message = f"Message {i}\n"
                stream.write(message.encode())
                await stream.drain()
                await asyncio.sleep(0.5)
            stream.close()

        async def reader(stream: asyncio.StreamReader):
            while True:
                data = await stream.readline()
                if not data:
                    break
                print(f"Received: {data.decode().strip()}")

        # 스트림 생성
        reader, writer = await asyncio.open_connection('localhost', 8888)
        
        # 리더/라이터 태스크 실행
        await asyncio.gather(
            writer(writer),
            reader(reader)
        )

    async def stream_server(self) -> None:
        """스트림 서버 예제"""
        print("\n=== Stream Server ===")
        
        async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
            addr = writer.get_extra_info('peername')
            print(f"New connection from {addr}")
            
            while True:
                data = await reader.readline()
                if not data:
                    break
                message = data.decode().strip()
                print(f"Received from {addr}: {message}")
                
                response = f"Echo: {message}\n"
                writer.write(response.encode())
                await writer.drain()
            
            print(f"Connection closed from {addr}")
            writer.close()

        # 서버 생성 및 실행
        server = await asyncio.start_server(
            handle_client, 'localhost', 8888
        )
        
        async with server:
            await server.serve_forever()

    async def stream_timeout(self) -> None:
        """스트림 타임아웃 예제"""
        print("\n=== Stream Timeout ===")
        
        async def slow_stream() -> AsyncGenerator[int, None]:
            for i in range(5):
                await asyncio.sleep(1)
                yield i

        # 타임아웃 설정
        try:
            async for number in asyncio.wait_for(slow_stream(), timeout=3):
                print(f"Received: {number}")
        except asyncio.TimeoutError:
            print("Stream timed out")

async def main():
    """메인 함수"""
    examples = StreamExamples()
    
    # 스트림 예제 실행
    await examples.basic_stream()
    await examples.stream_pipeline()
    await examples.stream_reader_writer()
    await examples.stream_server()
    await examples.stream_timeout()

if __name__ == "__main__":
    asyncio.run(main()) 