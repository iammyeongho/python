"""
CI/CD 파이프라인
=====================================
GitHub Actions, GitLab CI 등을 사용한 자동화 배포
"""

# =============================================================================
# 1. GitHub Actions - 기본 테스트
# =============================================================================

"""
# .github/workflows/test.yml

name: Tests

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        python-version: ['3.10', '3.11', '3.12']

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - name: Cache pip
        uses: actions/cache@v3
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip-

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install pytest pytest-cov

      - name: Run tests
        run: |
          pytest --cov=app --cov-report=xml

      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml
"""


# =============================================================================
# 2. GitHub Actions - 린트 및 타입 체크
# =============================================================================

"""
# .github/workflows/lint.yml

name: Lint & Type Check

on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install ruff mypy black isort

      - name: Run Black (formatting check)
        run: black --check .

      - name: Run isort (import sort check)
        run: isort --check-only .

      - name: Run Ruff (linting)
        run: ruff check .

      - name: Run mypy (type check)
        run: mypy src/
"""


# =============================================================================
# 3. GitHub Actions - Docker 빌드 및 푸시
# =============================================================================

"""
# .github/workflows/docker.yml

name: Docker Build & Push

on:
  push:
    branches: [main]
    tags: ['v*']

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write

    steps:
      - uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Log in to Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=ref,event=branch
            type=ref,event=pr
            type=semver,pattern={{version}}
            type=sha

      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
"""


# =============================================================================
# 4. GitHub Actions - 전체 CI/CD 파이프라인
# =============================================================================

"""
# .github/workflows/main.yml

name: CI/CD Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  # 1. 테스트
  test:
    runs-on: ubuntu-latest

    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: test_db
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432

      redis:
        image: redis:7
        ports:
          - 6379:6379

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov

      - name: Run tests
        env:
          DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test_db
          REDIS_URL: redis://localhost:6379
        run: pytest --cov=app

  # 2. 빌드
  build:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'

    steps:
      - uses: actions/checkout@v4

      - name: Build Docker image
        run: docker build -t myapp:${{ github.sha }} .

      - name: Save Docker image
        run: docker save myapp:${{ github.sha }} | gzip > myapp.tar.gz

      - name: Upload artifact
        uses: actions/upload-artifact@v3
        with:
          name: docker-image
          path: myapp.tar.gz

  # 3. 배포 (스테이징)
  deploy-staging:
    needs: build
    runs-on: ubuntu-latest
    environment: staging

    steps:
      - name: Download artifact
        uses: actions/download-artifact@v3
        with:
          name: docker-image

      - name: Deploy to staging
        run: |
          echo "Deploying to staging..."
          # SSH로 서버 접속 후 배포
          # 또는 Kubernetes, AWS ECS 등에 배포

  # 4. 배포 (프로덕션)
  deploy-production:
    needs: deploy-staging
    runs-on: ubuntu-latest
    environment: production

    steps:
      - name: Deploy to production
        run: |
          echo "Deploying to production..."
"""


# =============================================================================
# 5. GitLab CI
# =============================================================================

"""
# .gitlab-ci.yml

stages:
  - test
  - build
  - deploy

variables:
  DOCKER_IMAGE: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

# 테스트
test:
  stage: test
  image: python:3.11
  services:
    - postgres:15
    - redis:7
  variables:
    POSTGRES_PASSWORD: postgres
    DATABASE_URL: postgresql://postgres:postgres@postgres:5432/test
    REDIS_URL: redis://redis:6379
  before_script:
    - pip install -r requirements.txt
    - pip install pytest pytest-cov
  script:
    - pytest --cov=app --cov-report=xml
  coverage: '/TOTAL.*\s+(\d+%)$/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage.xml

# Docker 빌드
build:
  stage: build
  image: docker:24
  services:
    - docker:24-dind
  before_script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
  script:
    - docker build -t $DOCKER_IMAGE .
    - docker push $DOCKER_IMAGE
  only:
    - main

# 스테이징 배포
deploy-staging:
  stage: deploy
  image: alpine
  script:
    - echo "Deploying to staging..."
  environment:
    name: staging
    url: https://staging.example.com
  only:
    - main

# 프로덕션 배포
deploy-production:
  stage: deploy
  image: alpine
  script:
    - echo "Deploying to production..."
  environment:
    name: production
    url: https://example.com
  when: manual
  only:
    - main
"""


# =============================================================================
# 6. AWS 배포 (ECS)
# =============================================================================

"""
# .github/workflows/aws-ecs.yml

name: Deploy to AWS ECS

on:
  push:
    branches: [main]

env:
  AWS_REGION: ap-northeast-2
  ECR_REPOSITORY: myapp
  ECS_SERVICE: myapp-service
  ECS_CLUSTER: myapp-cluster
  CONTAINER_NAME: myapp

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ env.AWS_REGION }}

      - name: Login to Amazon ECR
        id: login-ecr
        uses: aws-actions/amazon-ecr-login@v2

      - name: Build, tag, and push image to Amazon ECR
        id: build-image
        env:
          ECR_REGISTRY: ${{ steps.login-ecr.outputs.registry }}
          IMAGE_TAG: ${{ github.sha }}
        run: |
          docker build -t $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG .
          docker push $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG
          echo "image=$ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG" >> $GITHUB_OUTPUT

      - name: Deploy to Amazon ECS
        uses: aws-actions/amazon-ecs-deploy-task-definition@v1
        with:
          task-definition: task-definition.json
          service: ${{ env.ECS_SERVICE }}
          cluster: ${{ env.ECS_CLUSTER }}
          wait-for-service-stability: true
"""


# =============================================================================
# 7. Kubernetes 배포
# =============================================================================

"""
# .github/workflows/kubernetes.yml

name: Deploy to Kubernetes

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up kubectl
        uses: azure/setup-kubectl@v3

      - name: Configure kubectl
        run: |
          echo "${{ secrets.KUBE_CONFIG }}" | base64 -d > kubeconfig
          export KUBECONFIG=kubeconfig

      - name: Build and push to registry
        run: |
          docker build -t myregistry/myapp:${{ github.sha }} .
          docker push myregistry/myapp:${{ github.sha }}

      - name: Deploy to Kubernetes
        run: |
          kubectl set image deployment/myapp \\
            myapp=myregistry/myapp:${{ github.sha }}
          kubectl rollout status deployment/myapp


# k8s/deployment.yaml 예제:

# apiVersion: apps/v1
# kind: Deployment
# metadata:
#   name: myapp
# spec:
#   replicas: 3
#   selector:
#     matchLabels:
#       app: myapp
#   template:
#     metadata:
#       labels:
#         app: myapp
#     spec:
#       containers:
#       - name: myapp
#         image: myregistry/myapp:latest
#         ports:
#         - containerPort: 8000
#         env:
#         - name: DATABASE_URL
#           valueFrom:
#             secretKeyRef:
#               name: myapp-secrets
#               key: database-url
"""


# =============================================================================
# 8. pre-commit 설정
# =============================================================================

"""
# .pre-commit-config.yaml

repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files

  - repo: https://github.com/psf/black
    rev: 24.1.0
    hooks:
      - id: black

  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.14
    hooks:
      - id: ruff
        args: [--fix, --exit-non-zero-on-fix]

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        additional_dependencies: [types-requests]

# 설치 및 사용:
# pip install pre-commit
# pre-commit install
# pre-commit run --all-files
"""


# =============================================================================
# 정리: CI/CD 베스트 프랙티스
# =============================================================================

"""
CI/CD 체크리스트:

1. 테스트 단계
   □ 단위 테스트
   □ 통합 테스트
   □ 코드 커버리지

2. 품질 검사
   □ 린팅 (ruff, flake8)
   □ 포매팅 (black, isort)
   □ 타입 체크 (mypy)
   □ 보안 스캔 (bandit, safety)

3. 빌드
   □ Docker 이미지 빌드
   □ 이미지 태깅 (SHA, 버전)
   □ 캐싱 활용

4. 배포
   □ 스테이징 환경 배포
   □ 프로덕션 수동 승인
   □ 롤백 전략

5. 모니터링
   □ 배포 알림 (Slack 등)
   □ 헬스 체크
   □ 에러 추적

파이프라인 단계:
test → lint → build → deploy-staging → deploy-production

PHP 비교:
- Laravel Forge, Envoyer와 유사한 워크플로우
- GitHub Actions는 PHP 프로젝트에서도 동일하게 사용
"""
