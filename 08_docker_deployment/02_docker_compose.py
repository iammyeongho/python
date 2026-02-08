"""
Docker Compose
=====================================
여러 컨테이너를 함께 관리하는 Docker Compose 사용법
"""

# =============================================================================
# 1. 기본 docker-compose.yml
# =============================================================================

"""
# docker-compose.yml

version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DEBUG=1
    volumes:
      - .:/app
"""


# =============================================================================
# 2. FastAPI + PostgreSQL + Redis
# =============================================================================

"""
# docker-compose.yml

version: '3.8'

services:
  # FastAPI 애플리케이션
  web:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/mydb
      - REDIS_URL=redis://redis:6379
      - SECRET_KEY=${SECRET_KEY:-development_secret}
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    volumes:
      - .:/app
    command: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    restart: unless-stopped

  # PostgreSQL 데이터베이스
  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped

  # Redis 캐시
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    command: redis-server --appendonly yes
    restart: unless-stopped

volumes:
  postgres_data:
  redis_data:
"""


# =============================================================================
# 3. Django + Celery + RabbitMQ
# =============================================================================

"""
# docker-compose.yml

version: '3.8'

services:
  # Django 웹
  web:
    build: .
    command: gunicorn config.wsgi:application --bind 0.0.0.0:8000
    ports:
      - "8000:8000"
    environment:
      - DEBUG=0
      - DATABASE_URL=postgresql://postgres:password@db:5432/django_db
      - CELERY_BROKER_URL=amqp://guest:guest@rabbitmq:5672//
    depends_on:
      - db
      - rabbitmq
    restart: unless-stopped

  # Celery Worker
  celery:
    build: .
    command: celery -A config worker --loglevel=info
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/django_db
      - CELERY_BROKER_URL=amqp://guest:guest@rabbitmq:5672//
    depends_on:
      - db
      - rabbitmq
    restart: unless-stopped

  # Celery Beat (스케줄러)
  celery-beat:
    build: .
    command: celery -A config beat --loglevel=info
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/django_db
      - CELERY_BROKER_URL=amqp://guest:guest@rabbitmq:5672//
    depends_on:
      - db
      - rabbitmq
    restart: unless-stopped

  # PostgreSQL
  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=django_db
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped

  # RabbitMQ
  rabbitmq:
    image: rabbitmq:3-management-alpine
    ports:
      - "5672:5672"
      - "15672:15672"  # Management UI
    restart: unless-stopped

volumes:
  postgres_data:
"""


# =============================================================================
# 4. 개발 vs 프로덕션 설정
# =============================================================================

"""
# docker-compose.yml (기본/공통)

version: '3.8'

services:
  web:
    build: .
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/mydb

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=mydb

volumes:
  postgres_data:


# docker-compose.override.yml (개발 - 자동 로드)

version: '3.8'

services:
  web:
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    command: uvicorn main:app --host 0.0.0.0 --reload
    environment:
      - DEBUG=1

  db:
    ports:
      - "5432:5432"


# docker-compose.prod.yml (프로덕션)

version: '3.8'

services:
  web:
    command: gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
    environment:
      - DEBUG=0
    deploy:
      replicas: 3
      resources:
        limits:
          cpus: '0.5'
          memory: 512M

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./static:/static
    depends_on:
      - web
"""


# =============================================================================
# 5. Nginx 설정
# =============================================================================

"""
# nginx.conf

upstream web {
    server web:8000;
}

server {
    listen 80;
    server_name localhost;

    # 정적 파일
    location /static/ {
        alias /static/;
    }

    # 미디어 파일
    location /media/ {
        alias /media/;
    }

    # API 및 동적 요청
    location / {
        proxy_pass http://web;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
"""


# =============================================================================
# 6. Docker Compose 명령어
# =============================================================================

"""
# 기본 명령어
docker compose up                    # 시작
docker compose up -d                 # 백그라운드 실행
docker compose up --build            # 빌드 후 시작
docker compose down                  # 중지 및 제거
docker compose down -v               # 볼륨까지 제거

# 프로덕션 설정으로 실행
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d

# 로그
docker compose logs                  # 모든 로그
docker compose logs -f web           # 웹 서비스 로그 (follow)

# 실행 중인 컨테이너 관리
docker compose ps                    # 상태 확인
docker compose exec web bash         # 컨테이너 접속
docker compose exec web python manage.py migrate  # 명령 실행

# 스케일링
docker compose up -d --scale web=3   # 웹 서비스 3개로

# 재시작
docker compose restart               # 전체 재시작
docker compose restart web           # 웹만 재시작

# 이미지 관리
docker compose build                 # 이미지 빌드
docker compose pull                  # 이미지 풀
docker compose push                  # 이미지 푸시
"""


# =============================================================================
# 7. 환경 변수 관리
# =============================================================================

"""
# .env 파일

# Database
POSTGRES_USER=myapp
POSTGRES_PASSWORD=supersecret
POSTGRES_DB=myapp_db
DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db:5432/${POSTGRES_DB}

# App
SECRET_KEY=your-super-secret-key
DEBUG=0
ALLOWED_HOSTS=example.com,www.example.com

# Redis
REDIS_URL=redis://redis:6379/0

# docker-compose.yml에서 사용
services:
  web:
    environment:
      - DATABASE_URL
      - SECRET_KEY
      - DEBUG
    env_file:
      - .env
"""


# =============================================================================
# 8. 헬스체크와 depends_on
# =============================================================================

"""
services:
  web:
    depends_on:
      db:
        condition: service_healthy  # DB가 healthy 상태일 때만 시작
      redis:
        condition: service_started  # Redis 시작 후

  db:
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s      # 검사 간격
      timeout: 5s        # 타임아웃
      retries: 5         # 재시도 횟수
      start_period: 30s  # 시작 대기 시간

  redis:
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
"""


# =============================================================================
# 9. 볼륨과 네트워크
# =============================================================================

"""
services:
  web:
    volumes:
      - .:/app                       # 바인드 마운트 (개발용)
      - static_volume:/app/static    # 네임드 볼륨
      - /etc/localtime:/etc/localtime:ro  # 읽기 전용
    networks:
      - frontend
      - backend

  db:
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - backend

  nginx:
    volumes:
      - static_volume:/static:ro
    networks:
      - frontend

volumes:
  postgres_data:
    driver: local
  static_volume:

networks:
  frontend:
  backend:
    internal: true  # 외부 접근 불가
"""


# =============================================================================
# 10. 완전한 프로덕션 예제
# =============================================================================

"""
# docker-compose.prod.yml

version: '3.8'

services:
  web:
    build:
      context: .
      dockerfile: Dockerfile.prod
    expose:
      - "8000"
    environment:
      - DATABASE_URL
      - SECRET_KEY
      - REDIS_URL
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
    deploy:
      replicas: 2
      restart_policy:
        condition: on-failure
        delay: 5s
        max_attempts: 3
    networks:
      - backend
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
      - static_volume:/static:ro
    depends_on:
      - web
    networks:
      - frontend
      - backend

  db:
    image: postgres:15-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./backup:/backup
    environment:
      - POSTGRES_PASSWORD_FILE=/run/secrets/db_password
    secrets:
      - db_password
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - backend

  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data
    command: redis-server --appendonly yes
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - backend

volumes:
  postgres_data:
  redis_data:
  static_volume:

networks:
  frontend:
  backend:
    internal: true

secrets:
  db_password:
    file: ./secrets/db_password.txt
"""


# =============================================================================
# 정리: Docker Compose 베스트 프랙티스
# =============================================================================

"""
Docker Compose 체크리스트:

1. 구성 분리
   □ docker-compose.yml (기본)
   □ docker-compose.override.yml (개발)
   □ docker-compose.prod.yml (프로덕션)

2. 보안
   □ 프로덕션에서 ports 대신 expose 사용
   □ 민감한 정보는 secrets 사용
   □ 내부 네트워크 분리

3. 안정성
   □ 헬스체크 설정
   □ depends_on 조건 설정
   □ restart 정책 설정

4. 로깅
   □ 로그 드라이버 설정
   □ 로그 크기 제한

5. 리소스
   □ 메모리/CPU 제한 설정
   □ 볼륨 영속성 확인

PHP (Laravel Sail 등)와 비교:
- 구조가 거의 동일
- Laravel Sail도 Docker Compose 기반
- Python 생태계에서도 유사한 패턴 사용
"""
