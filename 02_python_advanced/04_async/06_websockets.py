"""
WebSocket 클라이언트/서버
이 파일은 WebSocket 클라이언트와 서버의 개념과 사용법을 다룹니다.
"""

import asyncio
import websockets
from typing import Any
import json
import time

class WebSocketExamples:
    """WebSocket 예제 클래스"""

    def __init__(self):
        self.server = None
        self.clients = set()

    async def websocket_server(self) -> None:
        """WebSocket 서버 예제"""
        print("\n=== WebSocket Server ===")
        
        async def handle_client(websocket, path):
            self.clients.add(websocket)
            try:
                async for message in websocket:
                    print(f"Received: {message}")
                    # 모든 클라이언트에게 메시지 브로드캐스트
                    for client in self.clients:
                        if client != websocket:
                            await client.send(f"Echo: {message}")
            finally:
                self.clients.remove(websocket)

        # 서버 시작
        self.server = await websockets.serve(handle_client, "localhost", 8765)
        print("WebSocket server started on ws://localhost:8765")

    async def websocket_client(self) -> None:
        """WebSocket 클라이언트 예제"""
        print("\n=== WebSocket Client ===")
        
        async def client():
            async with websockets.connect("ws://localhost:8765") as websocket:
                # 메시지 전송
                await websocket.send("Hello, WebSocket!")
                
                # 응답 수신
                response = await websocket.recv()
                print(f"Received: {response}")

        # 클라이언트 실행
        await client()

    async def websocket_chat(self) -> None:
        """WebSocket 채팅 예제"""
        print("\n=== WebSocket Chat ===")
        
        async def chat_server(websocket, path):
            self.clients.add(websocket)
            try:
                async for message in websocket:
                    # 모든 클라이언트에게 메시지 브로드캐스트
                    for client in self.clients:
                        await client.send(f"Chat: {message}")
            finally:
                self.clients.remove(websocket)

        # 채팅 서버 시작
        self.server = await websockets.serve(chat_server, "localhost", 8766)
        print("Chat server started on ws://localhost:8766")

    async def websocket_binary(self) -> None:
        """WebSocket 바이너리 데이터 예제"""
        print("\n=== WebSocket Binary Data ===")
        
        async def binary_server(websocket, path):
            async for message in websocket:
                if isinstance(message, bytes):
                    print(f"Received binary data: {len(message)} bytes")
                    # 바이너리 데이터 에코
                    await websocket.send(message)

        # 바이너리 서버 시작
        self.server = await websockets.serve(binary_server, "localhost", 8767)
        print("Binary server started on ws://localhost:8767")

    async def websocket_json(self) -> None:
        """WebSocket JSON 데이터 예제"""
        print("\n=== WebSocket JSON Data ===")
        
        async def json_server(websocket, path):
            async for message in websocket:
                try:
                    data = json.loads(message)
                    print(f"Received JSON: {data}")
                    # JSON 응답
                    response = {"status": "success", "data": data}
                    await websocket.send(json.dumps(response))
                except json.JSONDecodeError:
                    print("Invalid JSON received")

        # JSON 서버 시작
        self.server = await websockets.serve(json_server, "localhost", 8768)
        print("JSON server started on ws://localhost:8768")

async def main():
    """메인 함수"""
    examples = WebSocketExamples()
    
    # WebSocket 예제 실행
    await examples.websocket_server()
    await examples.websocket_client()
    await examples.websocket_chat()
    await examples.websocket_binary()
    await examples.websocket_json()

if __name__ == "__main__":
    asyncio.run(main()) 