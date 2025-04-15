# 파이썬 비동기 프로그래밍 예제
# 작성일: 2024-04-08
# 목적: 파이썬의 비동기 프로그래밍과 관련된 다양한 기능을 설명하는 예제 코드

# 1. 기본 asyncio 사용
# asyncio의 기본적인 사용 방법을 보여줍니다.
print("=== 1. 기본 asyncio 사용 ===")

import asyncio

# 비동기 함수 정의
async def say_hello(name, delay):
    # delay 초 동안 대기
    await asyncio.sleep(delay)
    print(f"안녕하세요, {name}님! ({delay}초 후)")

# 메인 함수
async def main():
    # 여러 비동기 작업을 동시에 실행
    await asyncio.gather(
        say_hello("홍길동", 1),
        say_hello("김철수", 2),
        say_hello("이영희", 3)
    )

# 이벤트 루프 실행
asyncio.run(main())

# 2. 비동기 컨텍스트 매니저
# 비동기 컨텍스트 매니저를 사용하는 방법을 보여줍니다.
print("\n=== 2. 비동기 컨텍스트 매니저 ===")

class AsyncResource:
    def __init__(self, name):
        self.name = name
    
    async def __aenter__(self):
        print(f"{self.name} 리소스를 획득합니다.")
        await asyncio.sleep(1)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"{self.name} 리소스를 해제합니다.")
        await asyncio.sleep(1)

async def use_resource():
    async with AsyncResource("데이터베이스") as resource:
        print(f"{resource.name} 리소스를 사용 중입니다.")
        await asyncio.sleep(2)

asyncio.run(use_resource())

# 3. 비동기 이벤트 루프
# 비동기 이벤트 루프를 사용하는 방법을 보여줍니다.
print("\n=== 3. 비동기 이벤트 루프 ===")

async def event_loop_example():
    # 현재 이벤트 루프 가져오기
    loop = asyncio.get_event_loop()
    
    # 이벤트 루프에서 작업 실행
    await loop.run_in_executor(None, lambda: print("이벤트 루프에서 실행된 작업"))
    
    # 이벤트 루프 정보 출력
    print(f"이벤트 루프: {loop}")
    print(f"이벤트 루프가 실행 중인가요? {loop.is_running()}")
    print(f"이벤트 루프가 종료되었나요? {loop.is_closed()}")

asyncio.run(event_loop_example())

# 4. 비동기 제너레이터
# 비동기 제너레이터를 사용하는 방법을 보여줍니다.
print("\n=== 4. 비동기 제너레이터 ===")

async def async_range(start, stop, step=1):
    for i in range(start, stop, step):
        await asyncio.sleep(0.1)
        yield i

async def use_async_generator():
    async for i in async_range(1, 6):
        print(f"비동기 제너레이터 값: {i}")

asyncio.run(use_async_generator())

# 5. 비동기 큐
# 비동기 큐를 사용하는 방법을 보여줍니다.
print("\n=== 5. 비동기 큐 ===")

async def producer(queue):
    for i in range(5):
        await asyncio.sleep(0.5)
        await queue.put(f"항목 {i}")
        print(f"생산자: 항목 {i}을(를) 큐에 추가했습니다.")

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        await asyncio.sleep(1)
        print(f"소비자: {item}을(를) 처리했습니다.")
        queue.task_done()

async def queue_example():
    queue = asyncio.Queue()
    
    # 생산자와 소비자 작업 생성
    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))
    
    # 생산자 작업 완료 대기
    await producer_task
    
    # 큐에 None 추가하여 소비자에게 종료 신호 전송
    await queue.put(None)
    
    # 소비자 작업 완료 대기
    await consumer_task

asyncio.run(queue_example())

# 6. 비동기 웹 스크래핑
# 비동기 웹 스크래핑을 사용하는 방법을 보여줍니다.
print("\n=== 6. 비동기 웹 스크래핑 ===")

import aiohttp
from bs4 import BeautifulSoup

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def scrape_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        pages = await asyncio.gather(*tasks)
        
        for url, page in zip(urls, pages):
            soup = BeautifulSoup(page, 'html.parser')
            title = soup.title.string if soup.title else "제목 없음"
            print(f"URL: {url}")
            print(f"제목: {title}")
            print("-" * 50)

# 웹 스크래핑 예제 (실제로 실행하려면 인터넷 연결 필요)
# urls = [
#     "https://www.python.org",
#     "https://www.github.com",
#     "https://www.wikipedia.org"
# ]
# asyncio.run(scrape_urls(urls))

# 7. 비동기 데이터베이스 작업
# 비동기 데이터베이스 작업을 사용하는 방법을 보여줍니다.
print("\n=== 7. 비동기 데이터베이스 작업 ===")

import aiomysql

async def db_example():
    # 데이터베이스 연결
    conn = await aiomysql.connect(
        host='localhost',
        user='user',
        password='password',
        db='test_db'
    )
    
    async with conn.cursor() as cur:
        # 테이블 생성
        await cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                email VARCHAR(255)
            )
        """)
        
        # 데이터 삽입
        await cur.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s)",
            ("홍길동", "hong@example.com")
        )
        
        # 변경사항 저장
        await conn.commit()
        
        # 데이터 조회
        await cur.execute("SELECT * FROM users")
        users = await cur.fetchall()
        
        for user in users:
            print(f"사용자: {user}")
    
    # 연결 종료
    conn.close()
    await conn.wait_closed()

# 데이터베이스 예제 (실제로 실행하려면 MySQL 서버 필요)
# asyncio.run(db_example())

# 8. 비동기 예외 처리
# 비동기 코드에서 예외를 처리하는 방법을 보여줍니다.
print("\n=== 8. 비동기 예외 처리 ===")

async def error_task():
    await asyncio.sleep(1)
    raise ValueError("비동기 작업에서 오류 발생!")

async def handle_errors():
    try:
        await error_task()
    except ValueError as e:
        print(f"오류 처리: {e}")
    finally:
        print("오류 처리 완료")

asyncio.run(handle_errors())

# 9. 비동기 타임아웃
# 비동기 작업에 타임아웃을 설정하는 방법을 보여줍니다.
print("\n=== 9. 비동기 타임아웃 ===")

async def long_task():
    await asyncio.sleep(5)
    return "작업 완료!"

async def timeout_example():
    try:
        # 3초 타임아웃 설정
        result = await asyncio.wait_for(long_task(), timeout=3)
        print(result)
    except asyncio.TimeoutError:
        print("작업 시간 초과!")

asyncio.run(timeout_example())

print("\n프로그램 종료") 