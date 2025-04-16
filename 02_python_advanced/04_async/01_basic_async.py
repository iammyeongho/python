"""
비동기 프로그래밍의 기본 개념
이 파일은 비동기 프로그래밍의 기본 개념을 다룹니다.
"""

import asyncio
import time

class BasicAsync:
    """비동기 프로그래밍 기본 예제 클래스"""

    def __init__(self):
        pass

    async def say_hello(self, name: str, delay: int) -> str:
        """비동기 인사말 함수"""
        await asyncio.sleep(delay)
        return f"Hello, {name}!"

    async def fetch_data(self, data_id: int, delay: int) -> dict:
        """비동기 데이터 가져오기"""
        print(f"Fetching data {data_id}...")
        await asyncio.sleep(delay)
        return {"id": data_id, "data": f"Sample data {data_id}"}

    async def process_data(self, data: dict) -> dict:
        """비동기 데이터 처리"""
        print(f"Processing data {data['id']}...")
        await asyncio.sleep(1)
        return {**data, "processed": True}

    async def run_examples(self) -> None:
        """기본 비동기 예제 실행"""
        print("\n=== Basic Async Examples ===")
        
        # 기본 비동기 함수 실행
        result = await self.say_hello("Python", 1)
        print(result)

        # 여러 비동기 작업 동시 실행
        tasks = [
            self.fetch_data(1, 2),
            self.fetch_data(2, 1),
            self.fetch_data(3, 3)
        ]
        results = await asyncio.gather(*tasks)
        print("Fetched data:", results)

        # 비동기 데이터 처리 파이프라인
        processed_data = await self.process_data(results[0])
        print("Processed data:", processed_data)

def main():
    """메인 함수"""
    examples = BasicAsync()
    asyncio.run(examples.run_examples())

if __name__ == "__main__":
    main() 