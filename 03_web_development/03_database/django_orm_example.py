"""
Django ORM 예제
PHP의 Eloquent와 비교하여 Django ORM의 사용법을 보여줍니다.
"""

from django.db import models
from django.db import transaction
from django.utils import timezone

class User(models.Model):
    """사용자 모델 (PHP의 User 엔티티와 유사)"""
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Post(models.Model):
    """게시글 모델 (PHP의 Post 엔티티와 유사)"""
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class UserRepository:
    """사용자 Repository (PHP의 Repository 클래스와 유사)"""
    
    @staticmethod
    def create(username, email):
        """사용자 생성 (PHP의 create()와 유사)"""
        return User.objects.create(username=username, email=email)
    
    @staticmethod
    def find_by_id(user_id):
        """ID로 사용자 조회 (PHP의 find()와 유사)"""
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
    
    @staticmethod
    def update(user_id, **kwargs):
        """사용자 정보 업데이트 (PHP의 update()와 유사)"""
        User.objects.filter(id=user_id).update(**kwargs)
    
    @staticmethod
    def delete(user_id):
        """사용자 삭제 (PHP의 delete()와 유사)"""
        User.objects.filter(id=user_id).delete()

class PostRepository:
    """게시글 Repository"""
    
    @staticmethod
    def create(title, content, author_id):
        """게시글 생성"""
        author = UserRepository.find_by_id(author_id)
        if author:
            return Post.objects.create(title=title, content=content, author=author)
        return None
    
    @staticmethod
    def find_by_id(post_id):
        """ID로 게시글 조회"""
        try:
            return Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return None
    
    @staticmethod
    def update(post_id, **kwargs):
        """게시글 업데이트"""
        Post.objects.filter(id=post_id).update(**kwargs)
    
    @staticmethod
    def delete(post_id):
        """게시글 삭제"""
        Post.objects.filter(id=post_id).delete()

def main():
    """메인 함수 - Django ORM 사용 예제"""
    
    # 트랜잭션 내에서 작업 수행 (PHP의 트랜잭션과 유사)
    with transaction.atomic():
        # 사용자 생성
        user = UserRepository.create(
            username="john_doe",
            email="john@example.com"
        )
        print(f"Created user: {user}")
        
        # 게시글 생성
        post = PostRepository.create(
            title="Hello Django",
            content="This is a test post",
            author_id=user.id
        )
        print(f"Created post: {post}")
        
        # 사용자 정보 업데이트
        UserRepository.update(user.id, email="john.doe@example.com")
        updated_user = UserRepository.find_by_id(user.id)
        print(f"Updated user email: {updated_user.email}")
        
        # 게시글 업데이트
        PostRepository.update(post.id, title="Hello Django ORM")
        updated_post = PostRepository.find_by_id(post.id)
        print(f"Updated post title: {updated_post.title}")
        
        # 관계를 통한 게시글 조회 (PHP의 관계 메서드와 유사)
        user_posts = user.posts.all()
        print(f"User's posts: {list(user_posts)}")
        
        # 게시글 삭제
        PostRepository.delete(post.id)
        print("Deleted post")
        
        # 사용자 삭제
        UserRepository.delete(user.id)
        print("Deleted user")

if __name__ == "__main__":
    main() 