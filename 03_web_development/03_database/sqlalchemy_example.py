"""
Python과 PHP의 데이터베이스 접근 비교 예제 (SQLAlchemy)
이 파일은 PHP 개발자가 Python의 SQLAlchemy ORM을 이해하는 데 도움을 주기 위한 예제입니다.
"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
from typing import List, Optional
from contextlib import contextmanager

# 데이터베이스 연결 설정
engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

# 컨텍스트 매니저 (PHP의 트랜잭션과 유사)
@contextmanager
def session_scope():
    """세션 스코프 컨텍스트 매니저"""
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

# 모델 정의 (PHP의 엔티티와 유사)
class User(Base):
    """사용자 모델"""
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # 관계 정의 (PHP의 관계와 유사)
    posts = relationship('Post', back_populates='author')
    
    def __repr__(self):
        return f'<User {self.username}>'

class Post(Base):
    """게시글 모델"""
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # 관계 정의
    author = relationship('User', back_populates='posts')
    
    def __repr__(self):
        return f'<Post {self.title}>'

# 데이터베이스 초기화
def init_db():
    Base.metadata.create_all(engine)

# CRUD 작업 (PHP의 Repository와 유사)
class UserRepository:
    """사용자 저장소"""
    
    @staticmethod
    def create(username: str, email: str) -> User:
        """사용자 생성"""
        with session_scope() as session:
            user = User(username=username, email=email)
            session.add(user)
            return user
    
    @staticmethod
    def get(user_id: int) -> Optional[User]:
        """사용자 조회"""
        with session_scope() as session:
            return session.query(User).get(user_id)
    
    @staticmethod
    def get_by_username(username: str) -> Optional[User]:
        """사용자명으로 조회"""
        with session_scope() as session:
            return session.query(User).filter_by(username=username).first()
    
    @staticmethod
    def update(user_id: int, username: Optional[str] = None, email: Optional[str] = None) -> Optional[User]:
        """사용자 정보 업데이트"""
        with session_scope() as session:
            user = session.query(User).get(user_id)
            if user:
                if username is not None:
                    user.username = username
                if email is not None:
                    user.email = email
            return user
    
    @staticmethod
    def delete(user_id: int) -> bool:
        """사용자 삭제"""
        with session_scope() as session:
            user = session.query(User).get(user_id)
            if user:
                session.delete(user)
                return True
            return False

class PostRepository:
    """게시글 저장소"""
    
    @staticmethod
    def create(title: str, content: str, author_id: int) -> Post:
        """게시글 생성"""
        with session_scope() as session:
            post = Post(title=title, content=content, author_id=author_id)
            session.add(post)
            return post
    
    @staticmethod
    def get(post_id: int) -> Optional[Post]:
        """게시글 조회"""
        with session_scope() as session:
            return session.query(Post).get(post_id)
    
    @staticmethod
    def get_by_author(author_id: int) -> List[Post]:
        """작성자별 게시글 조회"""
        with session_scope() as session:
            return session.query(Post).filter_by(author_id=author_id).all()
    
    @staticmethod
    def update(post_id: int, title: Optional[str] = None, content: Optional[str] = None) -> Optional[Post]:
        """게시글 업데이트"""
        with session_scope() as session:
            post = session.query(Post).get(post_id)
            if post:
                if title is not None:
                    post.title = title
                if content is not None:
                    post.content = content
            return post
    
    @staticmethod
    def delete(post_id: int) -> bool:
        """게시글 삭제"""
        with session_scope() as session:
            post = session.query(Post).get(post_id)
            if post:
                session.delete(post)
                return True
            return False

def main():
    """메인 실행 함수"""
    # 데이터베이스 초기화
    init_db()
    
    # 사용자 생성 예제
    user = UserRepository.create("john_doe", "john@example.com")
    print(f"Created user: {user}")
    
    # 게시글 생성 예제
    post = PostRepository.create("Hello World", "This is my first post", user.id)
    print(f"Created post: {post}")
    
    # 사용자 조회 예제
    found_user = UserRepository.get(user.id)
    print(f"Found user: {found_user}")
    
    # 게시글 조회 예제
    found_post = PostRepository.get(post.id)
    print(f"Found post: {found_post}")
    
    # 작성자별 게시글 조회 예제
    user_posts = PostRepository.get_by_author(user.id)
    print(f"User's posts: {user_posts}")
    
    # 게시글 업데이트 예제
    updated_post = PostRepository.update(post.id, title="Updated Title")
    print(f"Updated post: {updated_post}")
    
    # 사용자 업데이트 예제
    updated_user = UserRepository.update(user.id, email="john.updated@example.com")
    print(f"Updated user: {updated_user}")
    
    # 게시글 삭제 예제
    PostRepository.delete(post.id)
    print("Deleted post")
    
    # 사용자 삭제 예제
    UserRepository.delete(user.id)
    print("Deleted user")

if __name__ == "__main__":
    main() 