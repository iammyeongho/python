"""
GraphQL with Python
=====================================
Strawberry를 사용한 GraphQL API 개발
pip install strawberry-graphql[fastapi]
"""

import strawberry
from typing import List, Optional
from dataclasses import dataclass
from datetime import datetime

# =============================================================================
# 1. 기본 타입 정의
# =============================================================================

@strawberry.type
class User:
    """사용자 타입"""
    id: int
    name: str
    email: str
    created_at: datetime


@strawberry.type
class Post:
    """게시글 타입"""
    id: int
    title: str
    content: str
    author_id: int
    created_at: datetime


# =============================================================================
# 2. 쿼리 정의
# =============================================================================

# 샘플 데이터
USERS = [
    User(id=1, name="Alice", email="alice@example.com", created_at=datetime.now()),
    User(id=2, name="Bob", email="bob@example.com", created_at=datetime.now()),
]

POSTS = [
    Post(id=1, title="Hello GraphQL", content="This is my first post",
         author_id=1, created_at=datetime.now()),
    Post(id=2, title="Python Tips", content="Some useful tips",
         author_id=2, created_at=datetime.now()),
]


@strawberry.type
class Query:
    """루트 쿼리"""

    @strawberry.field
    def users(self) -> List[User]:
        """모든 사용자 조회"""
        return USERS

    @strawberry.field
    def user(self, id: int) -> Optional[User]:
        """ID로 사용자 조회"""
        return next((u for u in USERS if u.id == id), None)

    @strawberry.field
    def posts(self) -> List[Post]:
        """모든 게시글 조회"""
        return POSTS

    @strawberry.field
    def post(self, id: int) -> Optional[Post]:
        """ID로 게시글 조회"""
        return next((p for p in POSTS if p.id == id), None)


# =============================================================================
# 3. Mutation 정의
# =============================================================================

@strawberry.input
class CreateUserInput:
    """사용자 생성 입력"""
    name: str
    email: str


@strawberry.input
class CreatePostInput:
    """게시글 생성 입력"""
    title: str
    content: str
    author_id: int


@strawberry.type
class Mutation:
    """루트 뮤테이션"""

    @strawberry.mutation
    def create_user(self, input: CreateUserInput) -> User:
        """사용자 생성"""
        new_user = User(
            id=len(USERS) + 1,
            name=input.name,
            email=input.email,
            created_at=datetime.now()
        )
        USERS.append(new_user)
        return new_user

    @strawberry.mutation
    def create_post(self, input: CreatePostInput) -> Post:
        """게시글 생성"""
        new_post = Post(
            id=len(POSTS) + 1,
            title=input.title,
            content=input.content,
            author_id=input.author_id,
            created_at=datetime.now()
        )
        POSTS.append(new_post)
        return new_post

    @strawberry.mutation
    def delete_user(self, id: int) -> bool:
        """사용자 삭제"""
        global USERS
        USERS = [u for u in USERS if u.id != id]
        return True


# =============================================================================
# 4. 관계 설정 (Resolver)
# =============================================================================

@strawberry.type
class UserWithPosts:
    """게시글을 포함한 사용자"""
    id: int
    name: str
    email: str

    @strawberry.field
    def posts(self) -> List[Post]:
        """사용자의 게시글"""
        return [p for p in POSTS if p.author_id == self.id]


@strawberry.type
class PostWithAuthor:
    """작성자를 포함한 게시글"""
    id: int
    title: str
    content: str
    author_id: int

    @strawberry.field
    def author(self) -> Optional[User]:
        """게시글 작성자"""
        return next((u for u in USERS if u.id == self.author_id), None)


# =============================================================================
# 5. Subscription (실시간)
# =============================================================================

"""
import asyncio
from typing import AsyncGenerator

@strawberry.type
class Subscription:
    @strawberry.subscription
    async def post_added(self) -> AsyncGenerator[Post, None]:
        '''새 게시글 구독'''
        while True:
            await asyncio.sleep(1)
            # 새 게시글이 있으면 yield
            if new_post := get_new_post():
                yield new_post
"""


# =============================================================================
# 6. FastAPI 통합
# =============================================================================

"""
# main.py

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

# 스키마 생성
schema = strawberry.Schema(query=Query, mutation=Mutation)

# FastAPI 앱
app = FastAPI()

# GraphQL 라우터 추가
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")


# 실행
# uvicorn main:app --reload

# GraphQL Playground: http://localhost:8000/graphql
"""


# =============================================================================
# 7. 인증 및 권한
# =============================================================================

"""
from strawberry.types import Info
from strawberry.permission import BasePermission

class IsAuthenticated(BasePermission):
    message = "User is not authenticated"

    def has_permission(self, source, info: Info, **kwargs) -> bool:
        request = info.context["request"]
        return request.headers.get("Authorization") is not None


class IsAdmin(BasePermission):
    message = "User is not admin"

    def has_permission(self, source, info: Info, **kwargs) -> bool:
        user = info.context.get("user")
        return user and user.is_admin


@strawberry.type
class Query:
    @strawberry.field(permission_classes=[IsAuthenticated])
    def protected_data(self) -> str:
        return "This is protected data"

    @strawberry.field(permission_classes=[IsAuthenticated, IsAdmin])
    def admin_only(self) -> str:
        return "Admin data"
"""


# =============================================================================
# 8. DataLoader (N+1 문제 해결)
# =============================================================================

"""
from strawberry.dataloader import DataLoader

# 배치 로딩 함수
async def load_users(user_ids: List[int]) -> List[User]:
    # DB에서 한 번에 조회
    users = await db.fetch_users(user_ids)
    user_map = {u.id: u for u in users}
    return [user_map.get(id) for id in user_ids]


# DataLoader 생성
user_loader = DataLoader(load_fn=load_users)


@strawberry.type
class Post:
    id: int
    title: str
    author_id: int

    @strawberry.field
    async def author(self, info: Info) -> User:
        # DataLoader를 통해 효율적으로 조회
        return await info.context["user_loader"].load(self.author_id)
"""


# =============================================================================
# 9. GraphQL 쿼리 예제
# =============================================================================

"""
# 사용자 목록 조회
query {
    users {
        id
        name
        email
    }
}

# 특정 사용자와 게시글 조회
query {
    user(id: 1) {
        id
        name
        posts {
            id
            title
        }
    }
}

# 사용자 생성
mutation {
    createUser(input: {name: "Charlie", email: "charlie@example.com"}) {
        id
        name
    }
}

# 게시글 생성
mutation {
    createPost(input: {title: "New Post", content: "Hello!", authorId: 1}) {
        id
        title
        author {
            name
        }
    }
}

# 변수 사용
query GetUser($userId: Int!) {
    user(id: $userId) {
        id
        name
        email
    }
}

# 프래그먼트
fragment UserFields on User {
    id
    name
    email
}

query {
    users {
        ...UserFields
    }
}
"""


# =============================================================================
# 10. 스키마 생성
# =============================================================================

# 기본 스키마
schema = strawberry.Schema(query=Query, mutation=Mutation)

# SDL 출력
print("=== GraphQL Schema ===")
print(schema.as_str())


# =============================================================================
# 정리: GraphQL vs REST
# =============================================================================

"""
GraphQL 장점:
1. 필요한 데이터만 요청 (Over-fetching 방지)
2. 단일 엔드포인트
3. 강력한 타입 시스템
4. 자기 문서화 (Introspection)
5. 실시간 구독 지원

GraphQL 단점:
1. 캐싱 복잡
2. 파일 업로드 처리 복잡
3. 학습 곡선

사용 시나리오:
- 복잡한 관계가 많은 데이터
- 다양한 클라이언트 (웹, 모바일)
- 실시간 기능 필요

Python GraphQL 라이브러리:
- Strawberry (권장): 타입 힌팅 기반
- Graphene: 성숙한 라이브러리
- Ariadne: 스키마 우선 방식

PHP 비교:
- webonyx/graphql-php
- Lighthouse (Laravel)
- Strawberry가 더 직관적인 문법
"""
