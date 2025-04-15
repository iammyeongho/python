"""
Python과 PHP의 웹 프레임워크 비교 예제 (Django)
이 파일은 PHP 개발자가 Python의 Django 프레임워크를 이해하는 데 도움을 주기 위한 예제입니다.
"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ValidationError
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# 모델 정의 (PHP의 엔티티와 유사)
class User(AbstractUser):
    """사용자 모델"""
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'pk': self.pk})

class Post(models.Model):
    """게시글 모델"""
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
    
    def clean(self):
        """데이터 검증 (PHP의 validation과 유사)"""
        if len(self.title) < 5:
            raise ValidationError("Title must be at least 5 characters long")
        if len(self.content) < 10:
            raise ValidationError("Content must be at least 10 characters long")

# 뷰 정의 (PHP의 컨트롤러와 유사)
class PostListView(LoginRequiredMixin, ListView):
    """게시글 목록 뷰"""
    model = Post
    template_name = 'posts/list.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostDetailView(LoginRequiredMixin, DetailView):
    """게시글 상세 뷰"""
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    """게시글 생성 뷰"""
    model = Post
    template_name = 'posts/form.html'
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    """게시글 수정 뷰"""
    model = Post
    template_name = 'posts/form.html'
    fields = ['title', 'content']
    
    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

class PostDeleteView(LoginRequiredMixin, DeleteView):
    """게시글 삭제 뷰"""
    model = Post
    template_name = 'posts/confirm_delete.html'
    success_url = '/posts/'
    
    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

# 함수 기반 뷰 (PHP의 컨트롤러와 유사)
@login_required
def user_profile(request):
    """사용자 프로필 뷰"""
    return render(request, 'users/profile.html', {
        'user': request.user
    })

@require_http_methods(['POST'])
def user_login(request):
    """사용자 로그인 뷰"""
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        return redirect('post_list')
    else:
        return render(request, 'users/login.html', {
            'error': 'Invalid credentials'
        })

@login_required
def user_logout(request):
    """사용자 로그아웃 뷰"""
    logout(request)
    return redirect('login')

# API 뷰 (PHP의 API와 유사)
@login_required
def api_posts(request):
    """게시글 API"""
    posts = Post.objects.all()
    return JsonResponse({
        'posts': [{
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'author': post.author.username,
            'created_at': post.created_at.isoformat(),
            'updated_at': post.updated_at.isoformat()
        } for post in posts]
    })

@login_required
def api_post_detail(request, pk):
    """게시글 상세 API"""
    post = get_object_or_404(Post, pk=pk)
    return JsonResponse({
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'author': post.author.username,
        'created_at': post.created_at.isoformat(),
        'updated_at': post.updated_at.isoformat()
    })

# URL 패턴 (PHP의 라우트와 유사)
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/create/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('profile/', views.user_profile, name='user_profile'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('api/posts/', views.api_posts, name='api_posts'),
    path('api/posts/<int:pk>/', views.api_post_detail, name='api_post_detail'),
]
""" 