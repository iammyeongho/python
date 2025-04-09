# FastAPI 기본 예제
# 작성일: 2024-04-09
# 목적: FastAPI의 기본적인 사용법을 설명하는 예제 코드

from fastapi import FastAPI, HTTPException, Path, Query, Body
from pydantic import BaseModel, Field
from typing import List, Optional
import uvicorn

# FastAPI 애플리케이션 생성
app = FastAPI(
    title="FastAPI 기본 예제",
    description="FastAPI의 기본적인 기능을 보여주는 예제 API",
    version="1.0.0"
)

# 1. 기본 라우트
@app.get("/")
async def root():
    """
    루트 경로에 대한 기본 응답을 반환합니다.
    """
    return {"message": "FastAPI 기본 예제에 오신 것을 환영합니다!"}

# 2. 경로 매개변수
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """
    경로 매개변수를 사용하여 특정 아이템을 조회합니다.
    
    - item_id: 조회할 아이템의 ID
    """
    return {"item_id": item_id}

# 3. 쿼리 매개변수
@app.get("/search/")
async def search_items(
    q: Optional[str] = Query(None, min_length=3, max_length=50, description="검색어"),
    skip: int = Query(0, ge=0, description="건너뛸 항목 수"),
    limit: int = Query(10, ge=1, le=100, description="반환할 항목 수")
):
    """
    쿼리 매개변수를 사용하여 아이템을 검색합니다.
    
    - q: 검색어 (선택적)
    - skip: 건너뛸 항목 수
    - limit: 반환할 항목 수
    """
    return {
        "q": q,
        "skip": skip,
        "limit": limit,
        "items": [{"item_id": i} for i in range(skip, skip + limit)]
    }

# 4. 요청 본문 (Request Body)
class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=50, description="아이템 이름")
    description: Optional[str] = Field(None, max_length=200, description="아이템 설명")
    price: float = Field(..., gt=0, description="아이템 가격")
    tax: Optional[float] = Field(None, ge=0, description="세금")

@app.post("/items/")
async def create_item(item: Item):
    """
    요청 본문을 사용하여 새 아이템을 생성합니다.
    
    - item: 생성할 아이템 정보
    """
    return item

# 5. 응답 모델
class ItemResponse(BaseModel):
    id: int
    name: str
    price: float
    is_available: bool = True

@app.get("/items/{item_id}/response", response_model=ItemResponse)
async def read_item_with_response(item_id: int):
    """
    응답 모델을 사용하여 아이템 정보를 반환합니다.
    
    - item_id: 조회할 아이템의 ID
    """
    # 실제로는 데이터베이스에서 조회하는 코드가 있을 것입니다
    return {
        "id": item_id,
        "name": f"아이템 {item_id}",
        "price": 100.0 * item_id,
        "is_available": item_id % 2 == 0
    }

# 6. 예외 처리
@app.get("/items/{item_id}/error")
async def read_item_with_error(item_id: int):
    """
    예외 처리를 보여주는 예제입니다.
    
    - item_id: 조회할 아이템의 ID
    """
    if item_id < 0:
        raise HTTPException(status_code=400, detail="아이템 ID는 0 이상이어야 합니다")
    if item_id > 100:
        raise HTTPException(status_code=404, detail="아이템을 찾을 수 없습니다")
    return {"item_id": item_id}

# 7. 중첩 모델
class Address(BaseModel):
    street: str
    city: str
    country: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    address: Address

@app.post("/users/")
async def create_user(user: User):
    """
    중첩 모델을 사용하여 사용자 정보를 생성합니다.
    
    - user: 생성할 사용자 정보
    """
    return user

# 8. 리스트 응답
@app.get("/items/", response_model=List[ItemResponse])
async def read_items(skip: int = 0, limit: int = 10):
    """
    리스트 응답을 반환하는 예제입니다.
    
    - skip: 건너뛸 항목 수
    - limit: 반환할 항목 수
    """
    items = []
    for i in range(skip, skip + limit):
        items.append({
            "id": i,
            "name": f"아이템 {i}",
            "price": 100.0 * i,
            "is_available": i % 2 == 0
        })
    return items

# 9. 경로 매개변수 검증
@app.get("/items/{item_id}/validate")
async def read_item_with_validation(
    item_id: int = Path(..., ge=1, le=100, description="아이템 ID")
):
    """
    경로 매개변수 검증을 보여주는 예제입니다.
    
    - item_id: 조회할 아이템의 ID (1 이상 100 이하)
    """
    return {"item_id": item_id}

# 10. 요청 본문 검증
@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item = Body(..., description="업데이트할 아이템 정보")
):
    """
    요청 본문 검증을 보여주는 예제입니다.
    
    - item_id: 업데이트할 아이템의 ID
    - item: 업데이트할 아이템 정보
    """
    return {"item_id": item_id, **item.dict()}

# 서버 실행
if __name__ == "__main__":
    uvicorn.run("01_basic_api:app", host="0.0.0.0", port=8000, reload=True) 