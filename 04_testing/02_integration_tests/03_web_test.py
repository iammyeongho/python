"""
웹 통합 테스트 예제
이 파일은 웹 애플리케이션의 통합 테스트를 수행하는 방법을 보여줍니다.
"""

import unittest
from flask import Flask, jsonify, request
from flask.testing import FlaskClient
from typing import Dict, Any

# 테스트용 Flask 애플리케이션
app = Flask(__name__)

# 메모리 내 데이터 저장소
users: Dict[int, Dict[str, Any]] = {}
posts: Dict[int, Dict[str, Any]] = {}

@app.route('/users', methods=['GET'])
def get_users():
    """모든 사용자 목록을 반환합니다."""
    return jsonify(list(users.values()))

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id: int):
    """특정 사용자 정보를 반환합니다."""
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(users[user_id])

@app.route('/users', methods=['POST'])
def create_user():
    """새로운 사용자를 생성합니다."""
    data = request.get_json()
    if not data or 'username' not in data or 'email' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    
    user_id = len(users) + 1
    users[user_id] = {
        'id': user_id,
        'username': data['username'],
        'email': data['email']
    }
    return jsonify(users[user_id]), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id: int):
    """사용자 정보를 업데이트합니다."""
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid data'}), 400
    
    users[user_id].update(data)
    return jsonify(users[user_id])

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int):
    """사용자를 삭제합니다."""
    if user_id not in users:
        return jsonify({'error': 'User not found'}), 404
    
    del users[user_id]
    return '', 204

@app.route('/posts', methods=['GET'])
def get_posts():
    """모든 게시글 목록을 반환합니다."""
    return jsonify(list(posts.values()))

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id: int):
    """특정 게시글 정보를 반환합니다."""
    if post_id not in posts:
        return jsonify({'error': 'Post not found'}), 404
    return jsonify(posts[post_id])

@app.route('/posts', methods=['POST'])
def create_post():
    """새로운 게시글을 생성합니다."""
    data = request.get_json()
    if not data or 'user_id' not in data or 'title' not in data or 'content' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    
    if data['user_id'] not in users:
        return jsonify({'error': 'User not found'}), 404
    
    post_id = len(posts) + 1
    posts[post_id] = {
        'id': post_id,
        'user_id': data['user_id'],
        'title': data['title'],
        'content': data['content']
    }
    return jsonify(posts[post_id]), 201

class TestWebIntegration(unittest.TestCase):
    """웹 통합 테스트"""

    def setUp(self):
        """각 테스트 메서드 실행 전에 호출됩니다."""
        app.config['TESTING'] = True
        self.client = app.test_client()
        # 데이터 초기화
        users.clear()
        posts.clear()

    def test_user_creation(self):
        """사용자 생성 테스트"""
        # 사용자 생성 요청
        response = self.client.post('/users', json={
            'username': 'testuser',
            'email': 'test@example.com'
        })
        
        # 응답 검증
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['username'], 'testuser')
        self.assertEqual(data['email'], 'test@example.com')
        self.assertIn('id', data)

    def test_user_retrieval(self):
        """사용자 조회 테스트"""
        # 테스트 데이터 생성
        users[1] = {
            'id': 1,
            'username': 'testuser',
            'email': 'test@example.com'
        }
        
        # 사용자 조회 요청
        response = self.client.get('/users/1')
        
        # 응답 검증
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data, users[1])

    def test_user_update(self):
        """사용자 정보 업데이트 테스트"""
        # 테스트 데이터 생성
        users[1] = {
            'id': 1,
            'username': 'testuser',
            'email': 'test@example.com'
        }
        
        # 사용자 정보 업데이트 요청
        response = self.client.put('/users/1', json={
            'email': 'updated@example.com'
        })
        
        # 응답 검증
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['email'], 'updated@example.com')
        self.assertEqual(users[1]['email'], 'updated@example.com')

    def test_user_deletion(self):
        """사용자 삭제 테스트"""
        # 테스트 데이터 생성
        users[1] = {
            'id': 1,
            'username': 'testuser',
            'email': 'test@example.com'
        }
        
        # 사용자 삭제 요청
        response = self.client.delete('/users/1')
        
        # 응답 검증
        self.assertEqual(response.status_code, 204)
        self.assertNotIn(1, users)

    def test_post_creation(self):
        """게시글 생성 테스트"""
        # 테스트 사용자 생성
        users[1] = {
            'id': 1,
            'username': 'testuser',
            'email': 'test@example.com'
        }
        
        # 게시글 생성 요청
        response = self.client.post('/posts', json={
            'user_id': 1,
            'title': 'Test Post',
            'content': 'This is a test post'
        })
        
        # 응답 검증
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['user_id'], 1)
        self.assertEqual(data['title'], 'Test Post')
        self.assertEqual(data['content'], 'This is a test post')
        self.assertIn('id', data)

    def test_post_retrieval(self):
        """게시글 조회 테스트"""
        # 테스트 데이터 생성
        posts[1] = {
            'id': 1,
            'user_id': 1,
            'title': 'Test Post',
            'content': 'This is a test post'
        }
        
        # 게시글 조회 요청
        response = self.client.get('/posts/1')
        
        # 응답 검증
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data, posts[1])

    def test_error_handling(self):
        """오류 처리 테스트"""
        # 존재하지 않는 사용자 조회
        response = self.client.get('/users/999')
        self.assertEqual(response.status_code, 404)
        
        # 잘못된 데이터로 사용자 생성
        response = self.client.post('/users', json={
            'username': 'testuser'
            # email 필드 누락
        })
        self.assertEqual(response.status_code, 400)
        
        # 존재하지 않는 사용자의 게시글 생성
        response = self.client.post('/posts', json={
            'user_id': 999,
            'title': 'Test Post',
            'content': 'This is a test post'
        })
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main() 