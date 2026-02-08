"""
Dockerfile 기초
=====================================
Python 애플리케이션을 위한 Dockerfile 작성법
"""

# =============================================================================
# 1. 기본 Dockerfile
# =============================================================================

"""
# Dockerfile

# 베이스 이미지 선택
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사 (캐시 활용)
COPY requirements.txt .

# 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY . .

# 포트 노출
EXPOSE 8000

# 실행 명령
CMD ["python", "main.py"]
"""


# =============================================================================
# 2. 최적화된 Dockerfile
# =============================================================================

"""
# Dockerfile.optimized

# 멀티 스테이지 빌드
FROM python:3.11-slim as builder

WORKDIR /app

# 가상환경 생성
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# 최종 이미지
FROM python:3.11-slim

WORKDIR /app

# 가상환경 복사
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# 비루트 사용자 생성
RUN useradd --create-home appuser
USER appuser

# 소스 코드 복사
COPY --chown=appuser:appuser . .

EXPOSE 8000

# 헬스체크
HEALTHCHECK --interval=30s --timeout=3s \\
    CMD curl -f http://localhost:8000/health || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
"""


# =============================================================================
# 3. FastAPI 전용 Dockerfile
# =============================================================================

"""
# Dockerfile.fastapi

FROM python:3.11-slim

WORKDIR /app

# 시스템 의존성
RUN apt-get update && apt-get install -y --no-install-recommends \\
    gcc \\
    && rm -rf /var/lib/apt/lists/*

# Poetry 사용 시
# RUN pip install poetry
# COPY pyproject.toml poetry.lock ./
# RUN poetry config virtualenvs.create false && poetry install --no-dev

# pip 사용 시
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 환경 변수
ENV PYTHONDONTWRITEBYTECODE=1 \\
    PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
"""


# =============================================================================
# 4. Django 전용 Dockerfile
# =============================================================================

"""
# Dockerfile.django

FROM python:3.11-slim

WORKDIR /app

# 시스템 의존성 (PostgreSQL 클라이언트 포함)
RUN apt-get update && apt-get install -y --no-install-recommends \\
    libpq-dev \\
    gcc \\
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 정적 파일 수집
RUN python manage.py collectstatic --noinput

ENV PYTHONDONTWRITEBYTECODE=1 \\
    PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
"""


# =============================================================================
# 5. .dockerignore 파일
# =============================================================================

"""
# .dockerignore

# Git
.git
.gitignore

# Python
__pycache__
*.py[cod]
*$py.class
*.so
.Python
build/
dist/
*.egg-info/
.eggs/

# 가상환경
venv/
.venv/
env/

# IDE
.idea/
.vscode/
*.swp
*.swo

# 테스트
.pytest_cache/
.coverage
htmlcov/
.tox/

# 환경 파일
.env
.env.local
*.env

# 문서
docs/
*.md
!README.md

# Docker
Dockerfile*
docker-compose*.yml
.docker/

# 기타
*.log
*.tmp
.DS_Store
"""


# =============================================================================
# 6. requirements.txt 생성
# =============================================================================

"""
# 기본 의존성 내보내기
pip freeze > requirements.txt

# 프로덕션용 (불필요한 패키지 제외)
pip freeze | grep -v "^-e" > requirements.txt

# pip-tools 사용 (권장)
pip install pip-tools

# requirements.in 작성
# requirements.in:
# fastapi
# uvicorn[standard]
# sqlalchemy
# pydantic

# 잠금 파일 생성
pip-compile requirements.in

# 설치
pip-sync requirements.txt
"""


# =============================================================================
# 7. Docker 명령어
# =============================================================================

"""
# 이미지 빌드
docker build -t myapp:latest .
docker build -f Dockerfile.prod -t myapp:prod .

# 컨테이너 실행
docker run -d -p 8000:8000 --name myapp myapp:latest

# 환경 변수 전달
docker run -d -p 8000:8000 \\
    -e DATABASE_URL=postgresql://... \\
    -e SECRET_KEY=mysecret \\
    myapp:latest

# 볼륨 마운트 (개발용)
docker run -d -p 8000:8000 \\
    -v $(pwd):/app \\
    myapp:latest

# 로그 확인
docker logs -f myapp

# 컨테이너 접속
docker exec -it myapp bash
docker exec -it myapp python manage.py shell

# 이미지 정리
docker system prune -a
docker image prune -a
"""


# =============================================================================
# 8. Dockerfile 베스트 프랙티스
# =============================================================================

"""
1. 가벼운 베이스 이미지 사용
   - python:3.11-slim (Debian slim)
   - python:3.11-alpine (더 작지만 호환성 이슈 가능)

2. 레이어 캐싱 활용
   - 변경이 적은 것 먼저 (requirements.txt)
   - 자주 변경되는 것 나중에 (소스 코드)

3. 멀티 스테이지 빌드
   - 빌드 의존성과 런타임 분리
   - 최종 이미지 크기 감소

4. 비루트 사용자 사용
   - 보안 강화
   - 파일 권한 주의

5. 불필요한 파일 제외
   - .dockerignore 활용
   - 캐시, 로그, 테스트 파일 제외

6. 헬스체크 추가
   - 컨테이너 상태 모니터링
   - 오케스트레이션 도구 연동

7. 환경 변수 활용
   - 설정 외부화
   - 12-Factor App 원칙
"""


# =============================================================================
# 9. 예제: Flask 앱 Dockerfile
# =============================================================================

"""
# 프로젝트 구조:
# myapp/
# ├── Dockerfile
# ├── docker-compose.yml
# ├── requirements.txt
# ├── app/
# │   ├── __init__.py
# │   ├── main.py
# │   └── config.py
# └── .dockerignore

# Dockerfile
FROM python:3.11-slim as base

ENV PYTHONDONTWRITEBYTECODE=1 \\
    PYTHONUNBUFFERED=1 \\
    PIP_NO_CACHE_DIR=1 \\
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app


FROM base as builder

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt


FROM base as production

COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN useradd --create-home --shell /bin/bash appuser
USER appuser

COPY --chown=appuser:appuser app/ ./app/

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app.main:app"]
"""


# =============================================================================
# 정리: Dockerfile 체크리스트
# =============================================================================

"""
Dockerfile 작성 체크리스트:

□ slim 또는 alpine 베이스 이미지 사용
□ .dockerignore 파일 작성
□ 의존성 먼저 복사 (캐싱 활용)
□ 불필요한 빌드 의존성 제거
□ 비루트 사용자 사용
□ PYTHONDONTWRITEBYTECODE=1 설정
□ PYTHONUNBUFFERED=1 설정
□ 헬스체크 추가
□ 적절한 EXPOSE 포트 설정
□ 프로덕션용 서버 사용 (gunicorn, uvicorn)

이미지 크기 비교:
- python:3.11         ~900MB
- python:3.11-slim    ~150MB
- python:3.11-alpine  ~50MB

PHP 비교:
- PHP Docker 이미지와 유사한 구조
- Composer -> pip/Poetry
- php-fpm -> gunicorn/uvicorn
"""
