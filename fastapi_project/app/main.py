"""
FastAPI 메인 애플리케이션
=========================
앱의 진입점

이 파일에서 하는 일:
1. FastAPI 앱 인스턴스 생성
2. 미들웨어 설정 (CORS, 로깅 등)
3. 라우터 등록
4. 이벤트 핸들러 (시작/종료)

실행:
    uvicorn app.main:app --reload
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import init_db, close_db
from app.routers import auth, users


# ============================================================================
# 앱 수명 주기 관리 (Lifespan)
# ============================================================================

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    앱 시작/종료 시 실행되는 코드

    시작 시: DB 연결, 초기화
    종료 시: DB 연결 해제, 정리
    """
    # 시작 시 (Startup)
    print("🚀 서버 시작 중...")
    await init_db()  # DB 테이블 생성
    print("✅ 데이터베이스 초기화 완료")

    yield  # 앱 실행

    # 종료 시 (Shutdown)
    print("🛑 서버 종료 중...")
    await close_db()
    print("✅ 데이터베이스 연결 종료")


# ============================================================================
# FastAPI 앱 생성
# ============================================================================

app = FastAPI(
    title=settings.app_name,
    description="""
## FastAPI 실무 프로젝트

### 기능
- 🔐 JWT 인증 (로그인, 회원가입)
- 👤 사용자 CRUD
- 📚 Swagger UI 자동 문서화

### 인증
1. `/api/v1/auth/login`으로 로그인
2. 받은 `access_token`을 Authorization 헤더에 추가
3. `Bearer <token>` 형식으로 요청
    """,
    version="1.0.0",
    docs_url="/docs",       # Swagger UI
    redoc_url="/redoc",     # ReDoc
    lifespan=lifespan,
)


# ============================================================================
# 미들웨어 설정
# ============================================================================

# CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,  # 허용할 도메인
    allow_credentials=True,               # 쿠키 허용
    allow_methods=["*"],                  # 모든 HTTP 메서드 허용
    allow_headers=["*"],                  # 모든 헤더 허용
)


# 커스텀 미들웨어 예시 (로깅)
# @app.middleware("http")
# async def log_requests(request: Request, call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     print(f"{request.method} {request.url.path} - {process_time:.3f}s")
#     return response


# ============================================================================
# 라우터 등록
# ============================================================================

# API 버전 접두사와 함께 라우터 등록
app.include_router(auth.router, prefix=settings.api_v1_prefix)
app.include_router(users.router, prefix=settings.api_v1_prefix)


# ============================================================================
# 루트 엔드포인트
# ============================================================================

@app.get("/", tags=["기본"])
async def root():
    """
    API 루트

    서버 상태 확인용
    """
    return {
        "message": "FastAPI 서버가 실행 중입니다!",
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health", tags=["기본"])
async def health_check():
    """
    헬스 체크

    로드밸런서, Kubernetes 등에서 사용
    """
    return {"status": "healthy"}


# ============================================================================
# 에러 핸들러 (선택)
# ============================================================================

# from fastapi import Request
# from fastapi.responses import JSONResponse
#
# @app.exception_handler(Exception)
# async def global_exception_handler(request: Request, exc: Exception):
#     return JSONResponse(
#         status_code=500,
#         content={"message": "서버 오류가 발생했습니다."}
#     )
