# GUI 프로그래밍과 네트워크 프로그래밍

# 1. tkinter GUI 예제
print("=== tkinter GUI 예제 ===")
"""
import tkinter as tk
from tkinter import messagebox

class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("간단한 GUI 앱")
        
        # 레이블
        self.label = tk.Label(root, text="이름을 입력하세요:")
        self.label.pack(pady=10)
        
        # 입력 필드
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)
        
        # 버튼
        self.button = tk.Button(root, text="환영!", command=self.show_message)
        self.button.pack(pady=10)
    
    def show_message(self):
        name = self.entry.get()
        if name:
            messagebox.showinfo("환영", f"안녕하세요, {name}님!")
        else:
            messagebox.showwarning("경고", "이름을 입력해주세요!")

# 앱 실행
root = tk.Tk()
app = SimpleApp(root)
root.mainloop()
"""

# 2. PyQt GUI 예제
print("\n=== PyQt GUI 예제 ===")
"""
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt 앱")
        self.setGeometry(100, 100, 400, 300)
        
        # 중앙 위젯 설정
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # 레이블
        label = QLabel("PyQt5로 만든 앱입니다!")
        layout.addWidget(label)
        
        # 버튼
        button = QPushButton("클릭하세요!")
        button.clicked.connect(self.button_clicked)
        layout.addWidget(button)
    
    def button_clicked(self):
        self.statusBar().showMessage("버튼이 클릭되었습니다!")

# 앱 실행
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
"""

# 3. 소켓 프로그래밍 (서버)
print("\n=== 소켓 프로그래밍 예제 ===")
"""
import socket
import threading

def handle_client(client_socket, addr):
    print(f"클라이언트 {addr} 연결됨")
    
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            
            # 에코 서버
            client_socket.send(data)
            print(f"클라이언트로부터 받은 메시지: {data.decode()}")
            
        except:
            break
    
    client_socket.close()
    print(f"클라이언트 {addr} 연결 종료")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5000))
    server.listen(5)
    print("서버 시작...")
    
    while True:
        client_socket, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_thread.start()

# 서버 시작
# server_thread = threading.Thread(target=start_server)
# server_thread.start()
"""

# 4. 소켓 프로그래밍 (클라이언트)
print("\n=== 소켓 클라이언트 예제 ===")
"""
import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5000))
    
    while True:
        message = input("메시지를 입력하세요 (종료: q): ")
        if message.lower() == 'q':
            break
        
        client.send(message.encode())
        response = client.recv(1024)
        print(f"서버로부터 받은 응답: {response.decode()}")
    
    client.close()

# 클라이언트 시작
# start_client()
"""

# 5. HTTP 서버
print("\n=== HTTP 서버 예제 ===")
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {
            'message': '안녕하세요!',
            'path': self.path
        }
        
        self.wfile.write(json.dumps(response).encode())
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {
            'message': '데이터를 받았습니다!',
            'received_data': post_data.decode()
        }
        
        self.wfile.write(json.dumps(response).encode())

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHandler)
    print('서버 시작...')
    httpd.serve_forever()

# 서버 시작
# run_server()
"""

# 6. 비동기 네트워크 프로그래밍
print("\n=== 비동기 네트워크 프로그래밍 예제 ===")
"""
import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        urls = [
            'https://example.com',
            'https://python.org',
            'https://github.com'
        ]
        
        tasks = [fetch_url(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)
        
        for url, response in zip(urls, responses):
            print(f"{url}: {len(response)} bytes")

# 비동기 함수 실행
# asyncio.run(main())
"""

# 7. 웹소켓 클라이언트
print("\n=== 웹소켓 클라이언트 예제 ===")
"""
import websockets
import asyncio

async def connect_to_websocket():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            message = input("메시지를 입력하세요 (종료: q): ")
            if message.lower() == 'q':
                break
            
            await websocket.send(message)
            response = await websocket.recv()
            print(f"서버로부터 받은 응답: {response}")

# 웹소켓 클라이언트 실행
# asyncio.run(connect_to_websocket())
"""

# 8. REST API 클라이언트
print("\n=== REST API 클라이언트 예제 ===")
"""
import requests

def make_api_request():
    # GET 요청
    response = requests.get('https://api.example.com/data')
    print("GET 응답:", response.json())
    
    # POST 요청
    data = {'name': '홍길동', 'age': 25}
    response = requests.post('https://api.example.com/users', json=data)
    print("POST 응답:", response.json())
    
    # PUT 요청
    data = {'age': 26}
    response = requests.put('https://api.example.com/users/1', json=data)
    print("PUT 응답:", response.json())
    
    # DELETE 요청
    response = requests.delete('https://api.example.com/users/1')
    print("DELETE 응답:", response.status_code)

# API 요청 실행
# make_api_request()
""" 