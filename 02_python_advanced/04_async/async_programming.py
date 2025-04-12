"""
PHP와 Python의 비동기 프로그래밍 비교
이 파일은 PHP 개발자가 Python의 비동기 프로그래밍을 이해하는 데 도움을 주기 위한 예제입니다.
"""

import asyncio
import aiohttp
from typing import List, Dict, Any
from datetime import datetime

async def fetch_data(url: str) -> Dict[str, Any]:
    """비동기 HTTP 요청 (PHP의 Guzzle 비동기 요청과 유사)"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def process_user_data(user_id: int) -> Dict[str, Any]:
    """비동기 사용자 데이터 처리 (PHP의 Promise와 유사)"""
    # 사용자 정보 가져오기
    user_url = f"https://api.example.com/users/{user_id}"
    user_data = await fetch_data(user_url)
    
    # 사용자의 게시물 가져오기
    posts_url = f"https://api.example.com/users/{user_id}/posts"
    posts_data = await fetch_data(posts_url)
    
    return {
        "user": user_data,
        "posts": posts_data
    }

async def batch_process_users(user_ids: List[int]) -> List[Dict[str, Any]]:
    """여러 사용자 데이터를 병렬로 처리 (PHP의 Promise::all과 유사)"""
    tasks = [process_user_data(user_id) for user_id in user_ids]
    return await asyncio.gather(*tasks)

class AsyncQueue:
    """비동기 큐 예제 (PHP의 Swoole 채널과 유사)"""
    
    def __init__(self):
        self.queue = asyncio.Queue()
    
    async def producer(self, items: List[Any]) -> None:
        """생산자 코루틴"""
        for item in items:
            await self.queue.put(item)
            print(f"Produced: {item}")
            await asyncio.sleep(0.1)
    
    async def consumer(self) -> None:
        """소비자 코루틴"""
        while True:
            item = await self.queue.get()
            print(f"Consumed: {item}")
            self.queue.task_done()
            await asyncio.sleep(0.2)

async def main():
    """메인 함수"""
    
    # 비동기 HTTP 요청 예제
    print("Fetching data from API...")
    data = await fetch_data("https://api.example.com/data")
    print(f"Received data: {data}")
    
    # 여러 사용자 데이터 처리 예제
    print("\nProcessing multiple users...")
    user_ids = [1, 2, 3, 4, 5]
    results = await batch_process_users(user_ids)
    for result in results:
        print(f"Processed user: {result['user']['name']}")
    
    # 비동기 큐 예제
    print("\nRunning producer-consumer example...")
    queue = AsyncQueue()
    
    # 생산자와 소비자 태스크 생성
    producer_task = asyncio.create_task(queue.producer([1, 2, 3, 4, 5]))
    consumer_task = asyncio.create_task(queue.consumer())
    
    # 생산자 완료 대기
    await producer_task
    
    # 큐가 비워질 때까지 대기
    await queue.queue.join()
    
    # 소비자 태스크 취소
    consumer_task.cancel()
    
    try:
        await consumer_task
    except asyncio.CancelledError:
        pass

if __name__ == "__main__":
    # 이벤트 루프 실행 (PHP의 ReactPHP 이벤트 루프와 유사)
    asyncio.run(main()) 