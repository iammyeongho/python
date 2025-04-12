# FastAPI 의존성 주입 예제
# 작성일: 2024-04-09
# 목적: FastAPI의 의존성 주입 기능을 설명하는 예제 코드

from fastapi import FastAPI, Depends, HTTPException, status, Header, Request
from typing import List, Optional, Callable
from pydantic import BaseModel
import uvicorn
import time
import random

# FastAPI 애플리케이션 생성
app = FastAPI(
    title="FastAPI 의존성 주입 예제",
    description="FastAPI의 의존성 주입 기능을 보여주는 예제",
    version="1.0.0"
)

# 1. 기본 의존성
# 간단한 의존성 함수
def get_db():
    """
    데이터베이스 연결을 제공하는 의존성 함수
    """
    db = "데이터베이스 연결"
    try:
        yield db
    finally:
        print("데이터베이스 연결 종료")

@app.get("/items/")
def read_items(db: str = Depends(get_db)):
    """
    기본 의존성을 사용하는 엔드포인트
    """
    return {"db": db, "items": ["item1", "item2", "item3"]}

# 2. 중첩 의존성
# 의존성 함수가 다른 의존성에 의존하는 경우
def get_query_parameter(q: Optional[str] = None):
    """
    쿼리 매개변수를 제공하는 의존성 함수
    """
    return q

def get_filtered_items(q: str = Depends(get_query_parameter)):
    """
    필터링된 아이템을 제공하는 의존성 함수
    """
    if q:
        return [f"filtered_{q}_item1", f"filtered_{q}_item2"]
    return ["item1", "item2"]

@app.get("/filtered-items/")
def read_filtered_items(items: List[str] = Depends(get_filtered_items)):
    """
    중첩 의존성을 사용하는 엔드포인트
    """
    return {"items": items}

# 3. 클래스 기반 의존성
class ItemRepository:
    """
    아이템 저장소 클래스
    """
    def __init__(self):
        self.items = ["item1", "item2", "item3"]
    
    def get_all(self):
        return self.items
    
    def get_by_id(self, item_id: int):
        if 0 <= item_id < len(self.items):
            return self.items[item_id]
        return None

# 의존성으로 사용할 클래스 인스턴스
item_repository = ItemRepository()

@app.get("/repository-items/")
def read_repository_items(repo: ItemRepository = Depends(lambda: item_repository)):
    """
    클래스 기반 의존성을 사용하는 엔드포인트
    """
    return {"items": repo.get_all()}

@app.get("/repository-items/{item_id}")
def read_repository_item(item_id: int, repo: ItemRepository = Depends(lambda: item_repository)):
    """
    클래스 기반 의존성을 사용하는 엔드포인트
    """
    item = repo.get_by_id(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="아이템을 찾을 수 없습니다")
    return {"item": item}

# 4. 의존성 캐싱
# 의존성 결과를 캐싱하는 예제
def get_cached_data():
    """
    캐시된 데이터를 제공하는 의존성 함수
    """
    # 실제로는 데이터베이스 쿼리나 외부 API 호출 등이 있을 수 있습니다
    time.sleep(1)  # 시간이 걸리는 작업 시뮬레이션
    return {"data": "캐시된 데이터", "timestamp": time.time()}

@app.get("/cached-data/")
def read_cached_data(data: dict = Depends(get_cached_data)):
    """
    캐시된 의존성을 사용하는 엔드포인트
    """
    return data

# 5. 조건부 의존성
# 조건에 따라 다른 의존성을 제공하는 예제
def get_production_db():
    """
    프로덕션 데이터베이스 연결을 제공하는 의존성 함수
    """
    return "프로덕션 데이터베이스 연결"

def get_test_db():
    """
    테스트 데이터베이스 연결을 제공하는 의존성 함수
    """
    return "테스트 데이터베이스 연결"

# 환경에 따라 다른 데이터베이스 연결을 제공하는 의존성 함수
def get_db_connection(environment: str = Header("X-Environment", "production")):
    """
    환경에 따라 다른 데이터베이스 연결을 제공하는 의존성 함수
    """
    if environment == "test":
        return get_test_db()
    return get_production_db()

@app.get("/environment-db/")
def read_environment_db(db: str = Depends(get_db_connection)):
    """
    조건부 의존성을 사용하는 엔드포인트
    """
    return {"db": db}

# 6. 의존성 오버라이드
# 테스트를 위해 의존성을 오버라이드하는 예제
def get_random_number():
    """
    랜덤 숫자를 제공하는 의존성 함수
    """
    return random.randint(1, 100)

@app.get("/random-number/")
def read_random_number(number: int = Depends(get_random_number)):
    """
    랜덤 숫자를 반환하는 엔드포인트
    """
    return {"number": number}

# 테스트용 의존성 오버라이드
def get_fixed_number():
    """
    고정된 숫자를 제공하는 의존성 함수 (테스트용)
    """
    return 42

# 의존성 오버라이드 예제 (실제로는 테스트 코드에서 사용)
app.dependency_overrides[get_random_number] = get_fixed_number

# 7. 의존성 검증
# 의존성 결과를 검증하는 예제
class User(BaseModel):
    username: str
    is_active: bool = True

def get_current_user(username: str = Header("X-Username", "anonymous")):
    """
    현재 사용자를 제공하는 의존성 함수
    """
    return User(username=username)

def get_active_user(user: User = Depends(get_current_user)):
    """
    활성 사용자를 제공하는 의존성 함수
    """
    if not user.is_active:
        raise HTTPException(status_code=400, detail="비활성 사용자입니다")
    return user

@app.get("/active-user/")
def read_active_user(user: User = Depends(get_active_user)):
    """
    활성 사용자 정보를 반환하는 엔드포인트
    """
    return {"user": user}

# 8. 의존성 공유
# 여러 엔드포인트에서 공유하는 의존성 예제
class SharedService:
    """
    공유 서비스 클래스
    """
    def __init__(self):
        self.counter = 0
    
    def increment(self):
        self.counter += 1
        return self.counter
    
    def get_count(self):
        return self.counter

# 공유 서비스 인스턴스
shared_service = SharedService()

@app.get("/shared-service/increment/")
def increment_counter(service: SharedService = Depends(lambda: shared_service)):
    """
    카운터를 증가시키는 엔드포인트
    """
    count = service.increment()
    return {"count": count}

@app.get("/shared-service/count/")
def get_counter(service: SharedService = Depends(lambda: shared_service)):
    """
    현재 카운터 값을 반환하는 엔드포인트
    """
    return {"count": service.get_count()}

# 9. 비동기 의존성
# 비동기 의존성 함수 예제
async def get_async_data():
    """
    비동기 데이터를 제공하는 의존성 함수
    """
    # 비동기 작업 시뮬레이션
    await asyncio.sleep(1)
    return {"data": "비동기 데이터"}

@app.get("/async-data/")
async def read_async_data(data: dict = Depends(get_async_data)):
    """
    비동기 의존성을 사용하는 엔드포인트
    """
    return data

# 10. 의존성 주입 테스트
# 의존성 주입을 테스트하는 예제
class TestService:
    """
    테스트 서비스 클래스
    """
    def __init__(self, test_mode: bool = False):
        self.test_mode = test_mode
    
    def get_data(self):
        if self.test_mode:
            return {"data": "테스트 데이터"}
        return {"data": "실제 데이터"}

# 테스트 모드 설정
test_mode = True
test_service = TestService(test_mode=test_mode)

@app.get("/test-service/")
def read_test_service(service: TestService = Depends(lambda: test_service)):
    """
    테스트 서비스를 사용하는 엔드포인트
    """
    return service.get_data()

# 서버 실행
if __name__ == "__main__":
    uvicorn.run("04_dependencies:app", host="0.0.0.0", port=8000, reload=True) 