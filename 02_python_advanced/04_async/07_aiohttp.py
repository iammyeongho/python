"""
aiohttp 클라이언트/서버
이 파일은 aiohttp 라이브러리를 사용한 비동기 HTTP 클라이언트와 서버의 개념과 사용법을 다룹니다.
"""

import asyncio
import aiohttp
from aiohttp import web
import json
from typing import Any, Dict
import time

class AiohttpExamples:
    """aiohttp 예제 클래스"""

    def __init__(self):
        self.app = web.Application()
        self.runner = None

    async def http_client(self) -> None:
        """HTTP 클라이언트 예제"""
        print("\n=== HTTP Client ===")
        
        async with aiohttp.ClientSession() as session:
            # GET 요청
            async with session.get('https://httpbin.org/get') as response:
                print(f"GET Status: {response.status}")
                print(f"GET Response: {await response.text()}")
            
            # POST 요청
            data = {'key': 'value'}
            async with session.post('https://httpbin.org/post', json=data) as response:
                print(f"POST Status: {response.status}")
                print(f"POST Response: {await response.text()}")
            
            # 동시 요청
            urls = [
                'https://httpbin.org/get',
                'https://httpbin.org/post',
                'https://httpbin.org/put'
            ]
            tasks = [session.get(url) for url in urls]
            responses = await asyncio.gather(*tasks)
            for response in responses:
                print(f"Concurrent Status: {response.status}")

    async def http_server(self) -> None:
        """HTTP 서버 예제"""
        print("\n=== HTTP Server ===")
        
        async def handle_get(request):
            return web.Response(text="Hello, GET request!")

        async def handle_post(request):
            data = await request.json()
            return web.json_response({"received": data})

        # 라우트 설정
        self.app.router.add_get('/', handle_get)
        self.app.router.add_post('/', handle_post)

        # 서버 시작
        self.runner = web.AppRunner(self.app)
        await self.runner.setup()
        site = web.TCPSite(self.runner, 'localhost', 8080)
        await site.start()
        print("HTTP server started on http://localhost:8080")

    async def websocket_server(self) -> None:
        """WebSocket 서버 예제"""
        print("\n=== WebSocket Server ===")
        
        async def websocket_handler(request):
            ws = web.WebSocketResponse()
            await ws.prepare(request)

            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    await ws.send_str(f"Echo: {msg.data}")
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    print(f"WebSocket error: {ws.exception()}")

            return ws

        # WebSocket 라우트 설정
        self.app.router.add_get('/ws', websocket_handler)

    async def file_upload(self) -> None:
        """파일 업로드 예제"""
        print("\n=== File Upload ===")
        
        async def handle_upload(request):
            reader = await request.multipart()
            field = await reader.next()
            filename = field.name
            with open(filename, 'wb') as f:
                while True:
                    chunk = await field.read_chunk()
                    if not chunk:
                        break
                    f.write(chunk)
            return web.Response(text=f"File {filename} uploaded successfully")

        # 파일 업로드 라우트 설정
        self.app.router.add_post('/upload', handle_upload)

    async def streaming_response(self) -> None:
        """스트리밍 응답 예제"""
        print("\n=== Streaming Response ===")
        
        async def stream_handler(request):
            response = web.StreamResponse()
            await response.prepare(request)
            
            for i in range(5):
                await response.write(f"Chunk {i}\n".encode())
                await asyncio.sleep(1)
            
            await response.write_eof()
            return response

        # 스트리밍 라우트 설정
        self.app.router.add_get('/stream', stream_handler)

async def main():
    """메인 함수"""
    examples = AiohttpExamples()
    
    # aiohttp 예제 실행
    await examples.http_client()
    await examples.http_server()
    await examples.websocket_server()
    await examples.file_upload()
    await examples.streaming_response()

if __name__ == "__main__":
    asyncio.run(main()) 