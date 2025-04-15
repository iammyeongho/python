# 파이썬 데이터베이스 연동

# 1. SQLite 데이터베이스
print("=== SQLite 데이터베이스 ===")

import sqlite3
import os

# 데이터베이스 파일 경로
db_path = "example.db"

# 데이터베이스 연결
def connect_db():
    """데이터베이스 연결 함수"""
    return sqlite3.connect(db_path)

# 테이블 생성
def create_tables(conn):
    """테이블 생성 함수"""
    cursor = conn.cursor()
    
    # 사용자 테이블 생성
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        age INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    # 게시물 테이블 생성
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        content TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """)
    
    conn.commit()
    print("테이블이 생성되었습니다.")

# 데이터 삽입
def insert_data(conn):
    """데이터 삽입 함수"""
    cursor = conn.cursor()
    
    # 사용자 데이터 삽입
    users = [
        ("홍길동", "hong@example.com", 25),
        ("김철수", "kim@example.com", 30),
        ("이영희", "lee@example.com", 28)
    ]
    
    cursor.executemany(
        "INSERT OR REPLACE INTO users (username, email, age) VALUES (?, ?, ?)",
        users
    )
    
    # 게시물 데이터 삽입
    posts = [
        (1, "첫 번째 게시물", "안녕하세요! 첫 번째 게시물입니다."),
        (1, "두 번째 게시물", "안녕하세요! 두 번째 게시물입니다."),
        (2, "김철수의 게시물", "김철수의 첫 번째 게시물입니다."),
        (3, "이영희의 게시물", "이영희의 첫 번째 게시물입니다.")
    ]
    
    cursor.executemany(
        "INSERT OR REPLACE INTO posts (user_id, title, content) VALUES (?, ?, ?)",
        posts
    )
    
    conn.commit()
    print("데이터가 삽입되었습니다.")

# 데이터 조회
def query_data(conn):
    """데이터 조회 함수"""
    cursor = conn.cursor()
    
    # 모든 사용자 조회
    print("\n모든 사용자:")
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print(row)
    
    # 모든 게시물 조회
    print("\n모든 게시물:")
    cursor.execute("SELECT * FROM posts")
    for row in cursor.fetchall():
        print(row)
    
    # 사용자와 게시물 조인 조회
    print("\n사용자와 게시물 조인:")
    cursor.execute("""
    SELECT users.username, posts.title, posts.content
    FROM users
    JOIN posts ON users.id = posts.user_id
    """)
    for row in cursor.fetchall():
        print(row)
    
    # 조건부 조회
    print("\n25세 이상 사용자:")
    cursor.execute("SELECT * FROM users WHERE age >= ?", (25,))
    for row in cursor.fetchall():
        print(row)
    
    # 집계 함수 사용
    print("\n사용자 통계:")
    cursor.execute("SELECT COUNT(*) FROM users")
    print(f"총 사용자 수: {cursor.fetchone()[0]}")
    
    cursor.execute("SELECT AVG(age) FROM users")
    print(f"평균 나이: {cursor.fetchone()[0]:.1f}")

# 데이터 업데이트
def update_data(conn):
    """데이터 업데이트 함수"""
    cursor = conn.cursor()
    
    # 사용자 나이 업데이트
    cursor.execute("UPDATE users SET age = ? WHERE username = ?", (26, "홍길동"))
    
    # 게시물 내용 업데이트
    cursor.execute("UPDATE posts SET content = ? WHERE title = ?", 
                  ("수정된 내용입니다.", "첫 번째 게시물"))
    
    conn.commit()
    print("데이터가 업데이트되었습니다.")

# 데이터 삭제
def delete_data(conn):
    """데이터 삭제 함수"""
    cursor = conn.cursor()
    
    # 특정 게시물 삭제
    cursor.execute("DELETE FROM posts WHERE title = ?", ("두 번째 게시물",))
    
    # 특정 사용자 삭제
    cursor.execute("DELETE FROM users WHERE username = ?", ("이영희",))
    
    conn.commit()
    print("데이터가 삭제되었습니다.")

# 트랜잭션 처리
def transaction_example(conn):
    """트랜잭션 처리 예제"""
    try:
        cursor = conn.cursor()
        
        # 트랜잭션 시작
        cursor.execute("BEGIN TRANSACTION")
        
        # 여러 작업 수행
        cursor.execute("INSERT INTO users (username, email, age) VALUES (?, ?, ?)",
                      ("박지성", "park@example.com", 35))
        
        cursor.execute("INSERT INTO posts (user_id, title, content) VALUES (?, ?, ?)",
                      (4, "박지성의 게시물", "박지성의 첫 번째 게시물입니다."))
        
        # 트랜잭션 커밋
        conn.commit()
        print("트랜잭션이 성공적으로 완료되었습니다.")
        
    except sqlite3.Error as e:
        # 오류 발생 시 롤백
        conn.rollback()
        print(f"트랜잭션 오류: {e}")

# 데이터베이스 연결 및 테이블 생성
conn = connect_db()
create_tables(conn)

# 데이터 삽입
insert_data(conn)

# 데이터 조회
query_data(conn)

# 데이터 업데이트
update_data(conn)

# 업데이트 후 데이터 조회
print("\n업데이트 후 데이터:")
query_data(conn)

# 트랜잭션 예제
transaction_example(conn)

# 데이터 삭제
delete_data(conn)

# 삭제 후 데이터 조회
print("\n삭제 후 데이터:")
query_data(conn)

# 데이터베이스 연결 종료
conn.close()

# 2. MySQL 데이터베이스 (PyMySQL 사용)
print("\n=== MySQL 데이터베이스 (PyMySQL) ===")

# PyMySQL 설치 필요: pip install pymysql

try:
    import pymysql
    
    # 데이터베이스 연결 설정
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'password',
        'db': 'example_db',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor
    }
    
    # 데이터베이스 연결
    def connect_mysql():
        """MySQL 데이터베이스 연결 함수"""
        return pymysql.connect(**db_config)
    
    # 테이블 생성
    def create_mysql_tables(conn):
        """MySQL 테이블 생성 함수"""
        with conn.cursor() as cursor:
            # 사용자 테이블 생성
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) NOT NULL UNIQUE,
                email VARCHAR(100) NOT NULL UNIQUE,
                age INT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)
            
            # 게시물 테이블 생성
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                title VARCHAR(100) NOT NULL,
                content TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
            """)
        
        conn.commit()
        print("MySQL 테이블이 생성되었습니다.")
    
    # 데이터 삽입
    def insert_mysql_data(conn):
        """MySQL 데이터 삽입 함수"""
        with conn.cursor() as cursor:
            # 사용자 데이터 삽입
            users = [
                ("홍길동", "hong@example.com", 25),
                ("김철수", "kim@example.com", 30),
                ("이영희", "lee@example.com", 28)
            ]
            
            cursor.executemany(
                "INSERT INTO users (username, email, age) VALUES (%s, %s, %s)",
                users
            )
            
            # 게시물 데이터 삽입
            posts = [
                (1, "첫 번째 게시물", "안녕하세요! 첫 번째 게시물입니다."),
                (1, "두 번째 게시물", "안녕하세요! 두 번째 게시물입니다."),
                (2, "김철수의 게시물", "김철수의 첫 번째 게시물입니다."),
                (3, "이영희의 게시물", "이영희의 첫 번째 게시물입니다.")
            ]
            
            cursor.executemany(
                "INSERT INTO posts (user_id, title, content) VALUES (%s, %s, %s)",
                posts
            )
        
        conn.commit()
        print("MySQL 데이터가 삽입되었습니다.")
    
    # 데이터 조회
    def query_mysql_data(conn):
        """MySQL 데이터 조회 함수"""
        with conn.cursor() as cursor:
            # 모든 사용자 조회
            print("\n모든 사용자:")
            cursor.execute("SELECT * FROM users")
            for row in cursor.fetchall():
                print(row)
            
            # 모든 게시물 조회
            print("\n모든 게시물:")
            cursor.execute("SELECT * FROM posts")
            for row in cursor.fetchall():
                print(row)
            
            # 사용자와 게시물 조인 조회
            print("\n사용자와 게시물 조인:")
            cursor.execute("""
            SELECT users.username, posts.title, posts.content
            FROM users
            JOIN posts ON users.id = posts.user_id
            """)
            for row in cursor.fetchall():
                print(row)
    
    # MySQL 연결 시도
    mysql_conn = connect_mysql()
    create_mysql_tables(mysql_conn)
    insert_mysql_data(mysql_conn)
    query_mysql_data(mysql_conn)
    mysql_conn.close()
    
except ImportError:
    print("PyMySQL이 설치되어 있지 않습니다. 'pip install pymysql' 명령으로 설치하세요.")

# 3. PostgreSQL 데이터베이스 (psycopg2 사용)
print("\n=== PostgreSQL 데이터베이스 (psycopg2) ===")

# psycopg2 설치 필요: pip install psycopg2

try:
    import psycopg2
    from psycopg2.extras import DictCursor
    
    # 데이터베이스 연결 설정
    pg_config = {
        'host': 'localhost',
        'user': 'postgres',
        'password': 'password',
        'dbname': 'example_db',
        'port': '5432'
    }
    
    # 데이터베이스 연결
    def connect_postgresql():
        """PostgreSQL 데이터베이스 연결 함수"""
        return psycopg2.connect(**pg_config)
    
    # 테이블 생성
    def create_postgresql_tables(conn):
        """PostgreSQL 테이블 생성 함수"""
        with conn.cursor() as cursor:
            # 사용자 테이블 생성
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) NOT NULL UNIQUE,
                email VARCHAR(100) NOT NULL UNIQUE,
                age INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)
            
            # 게시물 테이블 생성
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL,
                title VARCHAR(100) NOT NULL,
                content TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
            """)
        
        conn.commit()
        print("PostgreSQL 테이블이 생성되었습니다.")
    
    # 데이터 삽입
    def insert_postgresql_data(conn):
        """PostgreSQL 데이터 삽입 함수"""
        with conn.cursor() as cursor:
            # 사용자 데이터 삽입
            users = [
                ("홍길동", "hong@example.com", 25),
                ("김철수", "kim@example.com", 30),
                ("이영희", "lee@example.com", 28)
            ]
            
            cursor.executemany(
                "INSERT INTO users (username, email, age) VALUES (%s, %s, %s)",
                users
            )
            
            # 게시물 데이터 삽입
            posts = [
                (1, "첫 번째 게시물", "안녕하세요! 첫 번째 게시물입니다."),
                (1, "두 번째 게시물", "안녕하세요! 두 번째 게시물입니다."),
                (2, "김철수의 게시물", "김철수의 첫 번째 게시물입니다."),
                (3, "이영희의 게시물", "이영희의 첫 번째 게시물입니다.")
            ]
            
            cursor.executemany(
                "INSERT INTO posts (user_id, title, content) VALUES (%s, %s, %s)",
                posts
            )
        
        conn.commit()
        print("PostgreSQL 데이터가 삽입되었습니다.")
    
    # 데이터 조회
    def query_postgresql_data(conn):
        """PostgreSQL 데이터 조회 함수"""
        with conn.cursor(cursor_factory=DictCursor) as cursor:
            # 모든 사용자 조회
            print("\n모든 사용자:")
            cursor.execute("SELECT * FROM users")
            for row in cursor.fetchall():
                print(dict(row))
            
            # 모든 게시물 조회
            print("\n모든 게시물:")
            cursor.execute("SELECT * FROM posts")
            for row in cursor.fetchall():
                print(dict(row))
            
            # 사용자와 게시물 조인 조회
            print("\n사용자와 게시물 조인:")
            cursor.execute("""
            SELECT users.username, posts.title, posts.content
            FROM users
            JOIN posts ON users.id = posts.user_id
            """)
            for row in cursor.fetchall():
                print(dict(row))
    
    # PostgreSQL 연결 시도
    pg_conn = connect_postgresql()
    create_postgresql_tables(pg_conn)
    insert_postgresql_data(pg_conn)
    query_postgresql_data(pg_conn)
    pg_conn.close()
    
except ImportError:
    print("psycopg2가 설치되어 있지 않습니다. 'pip install psycopg2' 명령으로 설치하세요.")

# 4. SQLAlchemy ORM
print("\n=== SQLAlchemy ORM ===")

# SQLAlchemy 설치 필요: pip install sqlalchemy

try:
    from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, DateTime, func
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker, relationship
    
    # 데이터베이스 연결 설정
    DATABASE_URL = "sqlite:///sqlalchemy_example.db"
    
    # 엔진 생성
    engine = create_engine(DATABASE_URL)
    
    # 세션 팩토리 생성
    Session = sessionmaker(bind=engine)
    
    # 기본 클래스 생성
    Base = declarative_base()
    
    # 모델 정의
    class User(Base):
        """사용자 모델"""
        __tablename__ = 'users'
        
        id = Column(Integer, primary_key=True)
        username = Column(String(50), unique=True, nullable=False)
        email = Column(String(100), unique=True, nullable=False)
        age = Column(Integer)
        created_at = Column(DateTime, default=func.now())
        
        # 관계 정의
        posts = relationship("Post", back_populates="user")
        
        def __repr__(self):
            return f"<User(username='{self.username}', email='{self.email}', age={self.age})>"
    
    class Post(Base):
        """게시물 모델"""
        __tablename__ = 'posts'
        
        id = Column(Integer, primary_key=True)
        user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
        title = Column(String(100), nullable=False)
        content = Column(Text)
        created_at = Column(DateTime, default=func.now())
        
        # 관계 정의
        user = relationship("User", back_populates="posts")
        
        def __repr__(self):
            return f"<Post(title='{self.title}', user_id={self.user_id})>"
    
    # 테이블 생성
    Base.metadata.create_all(engine)
    print("SQLAlchemy 테이블이 생성되었습니다.")
    
    # 세션 생성
    session = Session()
    
    # 데이터 삽입
    def insert_orm_data():
        """ORM 데이터 삽입 함수"""
        # 사용자 생성
        user1 = User(username="홍길동", email="hong@example.com", age=25)
        user2 = User(username="김철수", email="kim@example.com", age=30)
        user3 = User(username="이영희", email="lee@example.com", age=28)
        
        # 세션에 추가
        session.add_all([user1, user2, user3])
        session.commit()
        
        # 게시물 생성
        post1 = Post(title="첫 번째 게시물", content="안녕하세요! 첫 번째 게시물입니다.", user=user1)
        post2 = Post(title="두 번째 게시물", content="안녕하세요! 두 번째 게시물입니다.", user=user1)
        post3 = Post(title="김철수의 게시물", content="김철수의 첫 번째 게시물입니다.", user=user2)
        post4 = Post(title="이영희의 게시물", content="이영희의 첫 번째 게시물입니다.", user=user3)
        
        # 세션에 추가
        session.add_all([post1, post2, post3, post4])
        session.commit()
        
        print("ORM 데이터가 삽입되었습니다.")
    
    # 데이터 조회
    def query_orm_data():
        """ORM 데이터 조회 함수"""
        # 모든 사용자 조회
        print("\n모든 사용자:")
        users = session.query(User).all()
        for user in users:
            print(user)
        
        # 모든 게시물 조회
        print("\n모든 게시물:")
        posts = session.query(Post).all()
        for post in posts:
            print(post)
        
        # 관계를 통한 조회
        print("\n사용자와 게시물 관계:")
        users = session.query(User).all()
        for user in users:
            print(f"{user.username}의 게시물:")
            for post in user.posts:
                print(f"  - {post.title}: {post.content}")
        
        # 필터링 조회
        print("\n25세 이상 사용자:")
        users = session.query(User).filter(User.age >= 25).all()
        for user in users:
            print(user)
        
        # 조인 조회
        print("\n사용자와 게시물 조인:")
        results = session.query(User.username, Post.title, Post.content).join(Post).all()
        for username, title, content in results:
            print(f"{username}: {title} - {content}")
    
    # 데이터 업데이트
    def update_orm_data():
        """ORM 데이터 업데이트 함수"""
        # 사용자 업데이트
        user = session.query(User).filter_by(username="홍길동").first()
        if user:
            user.age = 26
            session.commit()
        
        # 게시물 업데이트
        post = session.query(Post).filter_by(title="첫 번째 게시물").first()
        if post:
            post.content = "수정된 내용입니다."
            session.commit()
        
        print("ORM 데이터가 업데이트되었습니다.")
    
    # 데이터 삭제
    def delete_orm_data():
        """ORM 데이터 삭제 함수"""
        # 게시물 삭제
        post = session.query(Post).filter_by(title="두 번째 게시물").first()
        if post:
            session.delete(post)
            session.commit()
        
        # 사용자 삭제
        user = session.query(User).filter_by(username="이영희").first()
        if user:
            session.delete(user)
            session.commit()
        
        print("ORM 데이터가 삭제되었습니다.")
    
    # 데이터 삽입
    insert_orm_data()
    
    # 데이터 조회
    query_orm_data()
    
    # 데이터 업데이트
    update_orm_data()
    
    # 업데이트 후 데이터 조회
    print("\n업데이트 후 데이터:")
    query_orm_data()
    
    # 데이터 삭제
    delete_orm_data()
    
    # 삭제 후 데이터 조회
    print("\n삭제 후 데이터:")
    query_orm_data()
    
    # 세션 종료
    session.close()
    
except ImportError:
    print("SQLAlchemy가 설치되어 있지 않습니다. 'pip install sqlalchemy' 명령으로 설치하세요.")

# 5. MongoDB (pymongo 사용)
print("\n=== MongoDB (pymongo) ===")

# pymongo 설치 필요: pip install pymongo

try:
    from pymongo import MongoClient
    from bson import ObjectId
    
    # MongoDB 연결
    def connect_mongodb():
        """MongoDB 연결 함수"""
        return MongoClient('mongodb://localhost:27017/')
    
    # 데이터베이스 및 컬렉션 생성
    def setup_mongodb(client):
        """MongoDB 데이터베이스 및 컬렉션 설정"""
        db = client['example_db']
        users = db['users']
        posts = db['posts']
        
        # 인덱스 생성
        users.create_index([('username', 1)], unique=True)
        users.create_index([('email', 1)], unique=True)
        posts.create_index([('user_id', 1)])
        
        return db, users, posts
    
    # 데이터 삽입
    def insert_mongodb_data(users, posts):
        """MongoDB 데이터 삽입 함수"""
        # 사용자 데이터 삽입
        user_data = [
            {"username": "홍길동", "email": "hong@example.com", "age": 25},
            {"username": "김철수", "email": "kim@example.com", "age": 30},
            {"username": "이영희", "email": "lee@example.com", "age": 28}
        ]
        
        user_ids = []
        for user in user_data:
            result = users.insert_one(user)
            user_ids.append(result.inserted_id)
        
        # 게시물 데이터 삽입
        post_data = [
            {"user_id": user_ids[0], "title": "첫 번째 게시물", "content": "안녕하세요! 첫 번째 게시물입니다."},
            {"user_id": user_ids[0], "title": "두 번째 게시물", "content": "안녕하세요! 두 번째 게시물입니다."},
            {"user_id": user_ids[1], "title": "김철수의 게시물", "content": "김철수의 첫 번째 게시물입니다."},
            {"user_id": user_ids[2], "title": "이영희의 게시물", "content": "이영희의 첫 번째 게시물입니다."}
        ]
        
        for post in post_data:
            posts.insert_one(post)
        
        print("MongoDB 데이터가 삽입되었습니다.")
        return user_ids
    
    # 데이터 조회
    def query_mongodb_data(users, posts, user_ids):
        """MongoDB 데이터 조회 함수"""
        # 모든 사용자 조회
        print("\n모든 사용자:")
        for user in users.find():
            print(user)
        
        # 모든 게시물 조회
        print("\n모든 게시물:")
        for post in posts.find():
            print(post)
        
        # 관계 조회 (사용자 ID로 게시물 조회)
        print("\n사용자와 게시물 관계:")
        for user_id in user_ids:
            user = users.find_one({"_id": user_id})
            if user:
                print(f"{user['username']}의 게시물:")
                for post in posts.find({"user_id": user_id}):
                    print(f"  - {post['title']}: {post['content']}")
        
        # 필터링 조회
        print("\n25세 이상 사용자:")
        for user in users.find({"age": {"$gte": 25}}):
            print(user)
    
    # 데이터 업데이트
    def update_mongodb_data(users, posts):
        """MongoDB 데이터 업데이트 함수"""
        # 사용자 업데이트
        users.update_one(
            {"username": "홍길동"},
            {"$set": {"age": 26}}
        )
        
        # 게시물 업데이트
        posts.update_one(
            {"title": "첫 번째 게시물"},
            {"$set": {"content": "수정된 내용입니다."}}
        )
        
        print("MongoDB 데이터가 업데이트되었습니다.")
    
    # 데이터 삭제
    def delete_mongodb_data(users, posts):
        """MongoDB 데이터 삭제 함수"""
        # 게시물 삭제
        posts.delete_one({"title": "두 번째 게시물"})
        
        # 사용자 삭제
        user = users.find_one({"username": "이영희"})
        if user:
            # 사용자의 게시물도 삭제
            posts.delete_many({"user_id": user["_id"]})
            users.delete_one({"_id": user["_id"]})
        
        print("MongoDB 데이터가 삭제되었습니다.")
    
    # MongoDB 연결 시도
    client = connect_mongodb()
    db, users, posts = setup_mongodb(client)
    user_ids = insert_mongodb_data(users, posts)
    query_mongodb_data(users, posts, user_ids)
    update_mongodb_data(users, posts)
    print("\n업데이트 후 데이터:")
    query_mongodb_data(users, posts, user_ids)
    delete_mongodb_data(users, posts)
    print("\n삭제 후 데이터:")
    query_mongodb_data(users, posts, user_ids)
    client.close()
    
except ImportError:
    print("pymongo가 설치되어 있지 않습니다. 'pip install pymongo' 명령으로 설치하세요.")

# 6. Redis (redis-py 사용)
print("\n=== Redis (redis-py) ===")

# redis-py 설치 필요: pip install redis

try:
    import redis
    import json
    
    # Redis 연결
    def connect_redis():
        """Redis 연결 함수"""
        return redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    
    # 데이터 저장
    def store_redis_data(r):
        """Redis 데이터 저장 함수"""
        # 문자열 저장
        r.set('name', '홍길동')
        r.set('age', 25)
        
        # 리스트 저장
        r.lpush('fruits', '사과', '바나나', '오렌지')
        
        # 집합 저장
        r.sadd('tags', '파이썬', '데이터베이스', 'Redis')
        
        # 해시 저장
        r.hset('user:1', mapping={
            'username': '홍길동',
            'email': 'hong@example.com',
            'age': 25
        })
        
        # 정렬된 집합 저장
        r.zadd('scores', {'홍길동': 100, '김철수': 85, '이영희': 95})
        
        # JSON 데이터 저장
        user_data = {
            'username': '김철수',
            'email': 'kim@example.com',
            'age': 30,
            'interests': ['독서', '운동', '음악']
        }
        r.set('user:2', json.dumps(user_data))
        
        print("Redis 데이터가 저장되었습니다.")
    
    # 데이터 조회
    def query_redis_data(r):
        """Redis 데이터 조회 함수"""
        # 문자열 조회
        print(f"이름: {r.get('name')}")
        print(f"나이: {r.get('age')}")
        
        # 리스트 조회
        print(f"과일 목록: {r.lrange('fruits', 0, -1)}")
        
        # 집합 조회
        print(f"태그 목록: {r.smembers('tags')}")
        
        # 해시 조회
        print(f"사용자 1 정보: {r.hgetall('user:1')}")
        
        # 정렬된 집합 조회
        print(f"점수 목록: {r.zrange('scores', 0, -1, withscores=True)}")
        
        # JSON 데이터 조회
        user_json = r.get('user:2')
        if user_json:
            user_data = json.loads(user_json)
            print(f"사용자 2 정보: {user_data}")
    
    # 데이터 업데이트
    def update_redis_data(r):
        """Redis 데이터 업데이트 함수"""
        # 문자열 업데이트
        r.set('name', '김홍길')
        
        # 리스트 업데이트
        r.lpush('fruits', '포도')
        
        # 해시 업데이트
        r.hset('user:1', 'age', 26)
        
        # JSON 데이터 업데이트
        user_json = r.get('user:2')
        if user_json:
            user_data = json.loads(user_json)
            user_data['age'] = 31
            r.set('user:2', json.dumps(user_data))
        
        print("Redis 데이터가 업데이트되었습니다.")
    
    # 데이터 삭제
    def delete_redis_data(r):
        """Redis 데이터 삭제 함수"""
        # 키 삭제
        r.delete('name', 'age')
        
        # 리스트에서 항목 삭제
        r.lrem('fruits', 0, '바나나')
        
        # 해시 필드 삭제
        r.hdel('user:1', 'email')
        
        print("Redis 데이터가 삭제되었습니다.")
    
    # Redis 연결 시도
    r = connect_redis()
    store_redis_data(r)
    query_redis_data(r)
    update_redis_data(r)
    print("\n업데이트 후 데이터:")
    query_redis_data(r)
    delete_redis_data(r)
    print("\n삭제 후 데이터:")
    query_redis_data(r)
    
except ImportError:
    print("redis-py가 설치되어 있지 않습니다. 'pip install redis' 명령으로 설치하세요.")

print("\n프로그램 종료") 