# 파이썬 웹 프레임워크 예제

# 1. Django 웹 프레임워크
print("=== Django 웹 프레임워크 ===")
"""
Django 설치: pip install django

# 프로젝트 생성
django-admin startproject myproject
cd myproject

# 앱 생성
python manage.py startapp blog

# settings.py에 앱 등록
INSTALLED_APPS = [
    ...
    'blog',
]

# models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

# views.py
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]

# templates/blog/post_list.html
{% extends 'base.html' %}

{% block content %}
    {% for post in posts %}
        <h2>{{ post.title }}</h2>
        <p>{{ post.content }}</p>
    {% endfor %}
{% endblock %}
"""

# 2. Flask 웹 프레임워크
print("\n=== Flask 웹 프레임워크 ===")

# Flask 설치 필요: pip install flask
try:
    from flask import Flask, render_template, request, jsonify
    
    app = Flask(__name__)
    
    # 간단한 라우팅
    @app.route('/')
    def home():
        return '안녕하세요! Flask 웹 애플리케이션입니다.'
    
    # HTML 템플릿 렌더링
    @app.route('/hello/<name>')
    def hello(name):
        return render_template('hello.html', name=name)
    
    # POST 요청 처리
    @app.route('/api/post', methods=['POST'])
    def create_post():
        data = request.get_json()
        return jsonify({'message': '게시물이 생성되었습니다.', 'data': data})
    
    # 에러 핸들링
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': '페이지를 찾을 수 없습니다.'}), 404
    
    """
    # templates/hello.html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello</title>
    </head>
    <body>
        <h1>안녕하세요, {{ name }}님!</h1>
    </body>
    </html>
    
    # 실행
    if __name__ == '__main__':
        app.run(debug=True)
    """
    
except ImportError:
    print("Flask가 설치되어 있지 않습니다. 'pip install flask' 명령으로 설치하세요.")

# 3. FastAPI 웹 프레임워크
print("\n=== FastAPI 웹 프레임워크 ===")

# FastAPI 설치 필요: pip install fastapi uvicorn
try:
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel
    from typing import List, Optional
    
    app = FastAPI()
    
    # 데이터 모델
    class Post(BaseModel):
        title: str
        content: str
        published: bool = True
        rating: Optional[int] = None
    
    # 메모리 저장소
    posts = []
    
    # GET 엔드포인트
    @app.get("/")
    async def root():
        return {"message": "안녕하세요! FastAPI 웹 애플리케이션입니다."}
    
    # POST 엔드포인트
    @app.post("/posts/")
    async def create_post(post: Post):
        posts.append(post)
        return {"message": "게시물이 생성되었습니다.", "data": post}
    
    # GET 리스트 엔드포인트
    @app.get("/posts/", response_model=List[Post])
    async def get_posts():
        return posts
    
    # GET 단일 항목 엔드포인트
    @app.get("/posts/{post_id}")
    async def get_post(post_id: int):
        if post_id < 0 or post_id >= len(posts):
            raise HTTPException(status_code=404, detail="게시물을 찾을 수 없습니다.")
        return posts[post_id]
    
    """
    # 실행
    # uvicorn main:app --reload
    
    # 자동 생성된 API 문서
    # http://localhost:8000/docs
    # http://localhost:8000/redoc
    """
    
except ImportError:
    print("FastAPI가 설치되어 있지 않습니다. 'pip install fastapi uvicorn' 명령으로 설치하세요.")

# 4. aiohttp 비동기 웹 프레임워크
print("\n=== aiohttp 비동기 웹 프레임워크 ===")

# aiohttp 설치 필요: pip install aiohttp
try:
    from aiohttp import web
    import asyncio
    
    # 라우트 핸들러
    async def handle(request):
        return web.Response(text="안녕하세요! aiohttp 웹 애플리케이션입니다.")
    
    async def handle_post(request):
        data = await request.json()
        return web.json_response({"message": "게시물이 생성되었습니다.", "data": data})
    
    # 애플리케이션 설정
    app = web.Application()
    app.router.add_get('/', handle)
    app.router.add_post('/api/post', handle_post)
    
    """
    # 실행
    if __name__ == '__main__':
        web.run_app(app)
    """
    
except ImportError:
    print("aiohttp가 설치되어 있지 않습니다. 'pip install aiohttp' 명령으로 설치하세요.")

print("\n프로그램 종료") 