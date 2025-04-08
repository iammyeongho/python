# 파이썬 비동기 프로그래밍

# 1. 기본 asyncio 사용법
print("=== 기본 asyncio 사용법 ===")

import asyncio
import time

async def say_hello(name, delay):
    """비동기 함수 예제"""
    await asyncio.sleep(delay)
    print(f"안녕하세요, {name}!")
    return f"{name}의 인사"

async def main():
    """메인 비동기 함수"""
    # 동시에 여러 작업 실행
    task1 = asyncio.create_task(say_hello("홍길동", 1))
    task2 = asyncio.create_task(say_hello("김철수", 2))
    task3 = asyncio.create_task(say_hello("이영희", 3))
    
    # 모든 작업 완료 대기
    results = await asyncio.gather(task1, task2, task3)
    print(f"모든 작업 완료: {results}")

# 비동기 함수 실행
asyncio.run(main())

# 2. 비동기 컨텍스트 관리자
print("\n=== 비동기 컨텍스트 관리자 ===")

class AsyncResource:
    """비동기 리소스 클래스"""
    def __init__(self, name):
        self.name = name
    
    async def __aenter__(self):
        print(f"{self.name} 리소스 획득 중...")
        await asyncio.sleep(1)
        print(f"{self.name} 리소스 획득 완료")
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"{self.name} 리소스 해제 중...")
        await asyncio.sleep(1)
        print(f"{self.name} 리소스 해제 완료")

async def use_async_resource():
    """비동기 리소스 사용 예제"""
    async with AsyncResource("데이터베이스") as db:
        print("리소스 사용 중...")
        await asyncio.sleep(1)
        print("리소스 사용 완료")

asyncio.run(use_async_resource())

# 3. 비동기 이벤트 루프
print("\n=== 비동기 이벤트 루프 ===")

async def event_loop_example():
    """이벤트 루프 예제"""
    loop = asyncio.get_running_loop()
    
    # 이벤트 루프 정보 출력
    print(f"이벤트 루프: {loop}")
    print(f"기본 실행기: {loop.get_default_executor()}")
    
    # 이벤트 루프에서 작업 실행
    future = loop.create_future()
    loop.call_soon_threadsafe(future.set_result, "작업 완료")
    
    result = await future
    print(f"결과: {result}")

asyncio.run(event_loop_example())

# 4. 비동기 제너레이터
print("\n=== 비동기 제너레이터 ===")

async def async_range(start, stop):
    """비동기 범위 제너레이터"""
    for i in range(start, stop):
        await asyncio.sleep(0.1)
        yield i

async def use_async_generator():
    """비동기 제너레이터 사용 예제"""
    async for i in async_range(1, 6):
        print(f"숫자: {i}")

asyncio.run(use_async_generator())

# 5. 비동기 큐
print("\n=== 비동기 큐 ===")

async def producer(queue):
    """생산자 함수"""
    for i in range(5):
        await queue.put(f"항목 {i}")
        print(f"생산: 항목 {i}")
        await asyncio.sleep(0.5)

async def consumer(queue):
    """소비자 함수"""
    while True:
        item = await queue.get()
        print(f"소비: {item}")
        queue.task_done()
        await asyncio.sleep(1)

async def queue_example():
    """큐 사용 예제"""
    queue = asyncio.Queue()
    
    # 생산자와 소비자 태스크 생성
    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))
    
    # 생산자 완료 대기
    await producer_task
    
    # 큐가 비어있을 때까지 대기
    await queue.join()
    
    # 소비자 태스크 취소
    consumer_task.cancel()
    try:
        await consumer_task
    except asyncio.CancelledError:
        print("소비자 태스크 취소됨")

asyncio.run(queue_example())

# 6. 비동기 웹 스크래핑
print("\n=== 비동기 웹 스크래핑 ===")

# aiohttp 설치 필요: pip install aiohttp
try:
    import aiohttp
    from bs4 import BeautifulSoup
    
    async def fetch_url(session, url):
        """URL 가져오기"""
        async with session.get(url) as response:
            return await response.text()
    
    async def scrape_urls(urls):
        """여러 URL 스크래핑"""
        async with aiohttp.ClientSession() as session:
            tasks = [fetch_url(session, url) for url in urls]
            responses = await asyncio.gather(*tasks)
            
            for url, html in zip(urls, responses):
                soup = BeautifulSoup(html, 'html.parser')
                title = soup.title.string if soup.title else "제목 없음"
                print(f"URL: {url}")
                print(f"제목: {title}\n")
    
    # 예제 URL 목록
    urls = [
        'https://www.python.org',
        'https://www.github.com',
        'https://www.wikipedia.org'
    ]
    
    asyncio.run(scrape_urls(urls))
    
except ImportError:
    print("aiohttp가 설치되어 있지 않습니다. 'pip install aiohttp' 명령으로 설치하세요.")

# 7. 비동기 데이터베이스 작업
print("\n=== 비동기 데이터베이스 작업 ===")

# aiomysql 설치 필요: pip install aiomysql
try:
    import aiomysql
    
    async def db_example():
        """비동기 데이터베이스 작업 예제"""
        # 데이터베이스 연결
        conn = await aiomysql.connect(
            host='localhost',
            user='root',
            password='password',
            db='example_db'
        )
        
        async with conn.cursor() as cursor:
            # 테이블 생성
            await cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                age INT
            )
            """)
            
            # 데이터 삽입
            await cursor.execute(
                "INSERT INTO users (name, age) VALUES (%s, %s)",
                ("홍길동", 25)
            )
            
            # 데이터 조회
            await cursor.execute("SELECT * FROM users")
            result = await cursor.fetchall()
            print("사용자 목록:")
            for row in result:
                print(row)
        
        # 연결 종료
        conn.close()
        await conn.wait_closed()
    
    asyncio.run(db_example())
    
except ImportError:
    print("aiomysql이 설치되어 있지 않습니다. 'pip install aiomysql' 명령으로 설치하세요.")

print("\n프로그램 종료") 