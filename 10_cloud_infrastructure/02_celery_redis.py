"""
Celery와 Redis
=====================================
분산 작업 큐와 캐싱
pip install celery redis
"""

# =============================================================================
# 1. Redis 기본 사용법
# =============================================================================

"""
# pip install redis

import redis

# 연결
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# 문자열
r.set('name', 'Alice')
r.get('name')  # 'Alice'

r.set('counter', 0)
r.incr('counter')  # 1
r.incrby('counter', 5)  # 6

# 만료 시간 설정
r.setex('session', 3600, 'session_data')  # 1시간 후 만료
r.ttl('session')  # 남은 시간 (초)

# 해시 (딕셔너리)
r.hset('user:1', mapping={'name': 'Alice', 'age': 25})
r.hget('user:1', 'name')  # 'Alice'
r.hgetall('user:1')  # {'name': 'Alice', 'age': '25'}

# 리스트
r.rpush('queue', 'task1', 'task2', 'task3')
r.lpop('queue')  # 'task1'
r.lrange('queue', 0, -1)  # 전체 리스트

# 집합
r.sadd('tags', 'python', 'redis', 'celery')
r.smembers('tags')  # {'python', 'redis', 'celery'}

# 정렬된 집합 (점수 기반)
r.zadd('leaderboard', {'alice': 100, 'bob': 85, 'charlie': 92})
r.zrange('leaderboard', 0, -1, withscores=True)

# 삭제
r.delete('name')
r.flushdb()  # 현재 DB 전체 삭제
"""


# Redis 캐시 유틸리티
class RedisCache:
    """Redis 캐시 유틸리티"""

    def __init__(self, host='localhost', port=6379, db=0):
        import redis
        import json
        self.redis = redis.Redis(host=host, port=port, db=db, decode_responses=True)
        self.json = json

    def get(self, key: str):
        """캐시 조회"""
        value = self.redis.get(key)
        if value:
            try:
                return self.json.loads(value)
            except:
                return value
        return None

    def set(self, key: str, value, expire: int = None):
        """캐시 설정"""
        if isinstance(value, (dict, list)):
            value = self.json.dumps(value)
        if expire:
            self.redis.setex(key, expire, value)
        else:
            self.redis.set(key, value)

    def delete(self, key: str):
        """캐시 삭제"""
        self.redis.delete(key)

    def exists(self, key: str) -> bool:
        """키 존재 확인"""
        return self.redis.exists(key) > 0


# 캐시 데코레이터
def redis_cache(expire: int = 300):
    """Redis 캐시 데코레이터"""
    import functools
    import json
    import redis
    import hashlib

    r = redis.Redis(decode_responses=True)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 캐시 키 생성
            key_data = f"{func.__name__}:{args}:{kwargs}"
            cache_key = hashlib.md5(key_data.encode()).hexdigest()

            # 캐시 확인
            cached = r.get(cache_key)
            if cached:
                return json.loads(cached)

            # 함수 실행 및 캐시 저장
            result = func(*args, **kwargs)
            r.setex(cache_key, expire, json.dumps(result))
            return result

        return wrapper
    return decorator


# =============================================================================
# 2. Celery 기본 설정
# =============================================================================

"""
# celery_app.py

from celery import Celery

app = Celery(
    'tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/1'
)

# 설정
app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='Asia/Seoul',
    enable_utc=True,
    task_track_started=True,
    task_time_limit=3600,  # 1시간 제한
)

# 태스크 정의
@app.task(bind=True)
def add(self, x, y):
    return x + y

@app.task(bind=True)
def long_task(self, duration):
    import time
    for i in range(duration):
        time.sleep(1)
        # 진행 상황 업데이트
        self.update_state(
            state='PROGRESS',
            meta={'current': i + 1, 'total': duration}
        )
    return {'status': 'completed', 'result': duration}
"""


# =============================================================================
# 3. Celery 태스크 예제
# =============================================================================

"""
# tasks.py

from celery import Celery, shared_task
from celery.exceptions import MaxRetriesExceededError

app = Celery('tasks')
app.config_from_object('celeryconfig')


# 기본 태스크
@app.task
def send_email(to: str, subject: str, body: str):
    '''이메일 발송 태스크'''
    import smtplib
    # 이메일 발송 로직
    print(f"Sending email to {to}: {subject}")
    return True


# 재시도 태스크
@app.task(bind=True, max_retries=3, default_retry_delay=60)
def process_payment(self, order_id: int):
    '''결제 처리 (재시도 지원)'''
    try:
        # 결제 처리 로직
        result = external_payment_api(order_id)
        return result
    except Exception as e:
        try:
            self.retry(exc=e)
        except MaxRetriesExceededError:
            # 최대 재시도 초과
            notify_admin(f"Payment failed: {order_id}")
            raise


# 체인 태스크
@app.task
def step1(data):
    return data + 1

@app.task
def step2(data):
    return data * 2

@app.task
def step3(data):
    return data ** 2


# 그룹 태스크
@app.task
def process_item(item_id):
    # 개별 아이템 처리
    return f"Processed {item_id}"
"""


# =============================================================================
# 4. Celery 태스크 호출
# =============================================================================

"""
# 동기 호출 (블로킹)
result = add.apply(args=[4, 4])
print(result.get())  # 8

# 비동기 호출 (논블로킹)
result = add.delay(4, 4)  # 또는 add.apply_async(args=[4, 4])
print(result.id)  # 태스크 ID
print(result.ready())  # 완료 여부
print(result.get(timeout=10))  # 결과 대기

# 태스크 체인
from celery import chain
result = chain(step1.s(10), step2.s(), step3.s())()
print(result.get())  # ((10 + 1) * 2) ** 2 = 484

# 태스크 그룹 (병렬 실행)
from celery import group
result = group(process_item.s(i) for i in range(10))()
print(result.get())  # 모든 결과 리스트

# 태스크 코드
from celery import chord
callback = final_task.s()
result = chord(
    group(process_item.s(i) for i in range(10)),
    callback
)()

# 예약 실행
from datetime import datetime, timedelta
eta = datetime.utcnow() + timedelta(hours=1)
add.apply_async(args=[4, 4], eta=eta)

# 카운트다운 (초 단위 지연)
add.apply_async(args=[4, 4], countdown=60)
"""


# =============================================================================
# 5. Celery Beat (스케줄러)
# =============================================================================

"""
# celeryconfig.py

from celery.schedules import crontab

beat_schedule = {
    # 매분 실행
    'add-every-minute': {
        'task': 'tasks.add',
        'schedule': 60.0,  # 초
        'args': (16, 16),
    },
    # 매일 자정 실행
    'cleanup-every-midnight': {
        'task': 'tasks.cleanup',
        'schedule': crontab(hour=0, minute=0),
    },
    # 매주 월요일 9시
    'weekly-report': {
        'task': 'tasks.generate_report',
        'schedule': crontab(hour=9, minute=0, day_of_week=1),
    },
    # 매월 1일
    'monthly-billing': {
        'task': 'tasks.process_billing',
        'schedule': crontab(hour=0, minute=0, day_of_month=1),
    },
}

# Celery Beat 실행
# celery -A tasks beat --loglevel=info
"""


# =============================================================================
# 6. FastAPI + Celery 통합
# =============================================================================

"""
# main.py

from fastapi import FastAPI, BackgroundTasks
from celery.result import AsyncResult
from tasks import long_task, send_email

app = FastAPI()


@app.post("/tasks/")
async def create_task(duration: int):
    '''태스크 생성'''
    task = long_task.delay(duration)
    return {"task_id": task.id}


@app.get("/tasks/{task_id}")
async def get_task_status(task_id: str):
    '''태스크 상태 조회'''
    result = AsyncResult(task_id)

    return {
        "task_id": task_id,
        "status": result.status,
        "result": result.result if result.ready() else None
    }


@app.post("/email/")
async def send_email_task(to: str, subject: str, body: str):
    '''이메일 발송 태스크'''
    task = send_email.delay(to, subject, body)
    return {"task_id": task.id, "message": "Email queued"}
"""


# =============================================================================
# 7. Celery 모니터링 (Flower)
# =============================================================================

"""
# Flower 설치 및 실행
pip install flower

# 실행
celery -A tasks flower --port=5555

# 웹 UI: http://localhost:5555

# 기능:
# - 실시간 태스크 모니터링
# - 워커 상태 확인
# - 태스크 통계
# - 태스크 취소/재시도
"""


# =============================================================================
# 8. 실전 예제: 이미지 처리 파이프라인
# =============================================================================

"""
# tasks.py

from celery import Celery, chain
from PIL import Image
import boto3

app = Celery('image_tasks')


@app.task
def download_image(url: str) -> str:
    '''이미지 다운로드'''
    import requests
    response = requests.get(url)
    local_path = f'/tmp/{uuid.uuid4()}.jpg'
    with open(local_path, 'wb') as f:
        f.write(response.content)
    return local_path


@app.task
def resize_image(local_path: str, size: tuple = (800, 600)) -> str:
    '''이미지 리사이즈'''
    img = Image.open(local_path)
    img.thumbnail(size)
    resized_path = local_path.replace('.jpg', '_resized.jpg')
    img.save(resized_path)
    return resized_path


@app.task
def upload_to_s3(local_path: str, bucket: str) -> str:
    '''S3에 업로드'''
    s3 = boto3.client('s3')
    key = f'images/{os.path.basename(local_path)}'
    s3.upload_file(local_path, bucket, key)
    return f's3://{bucket}/{key}'


@app.task
def cleanup(paths: list):
    '''임시 파일 정리'''
    for path in paths:
        if os.path.exists(path):
            os.remove(path)


# 파이프라인 실행
def process_image_pipeline(url: str):
    pipeline = chain(
        download_image.s(url),
        resize_image.s(),
        upload_to_s3.s('my-bucket'),
    )
    return pipeline()
"""


# =============================================================================
# 정리: Celery + Redis
# =============================================================================

"""
Redis 용도:
1. 캐싱 (TTL 지원)
2. 세션 저장
3. 실시간 데이터 (Pub/Sub)
4. 작업 큐 (브로커)
5. 리더보드/카운터

Celery 구성요소:
1. Broker (Redis/RabbitMQ): 태스크 큐
2. Worker: 태스크 실행
3. Backend (Redis): 결과 저장
4. Beat: 스케줄러

Celery 명령어:
# 워커 실행
celery -A tasks worker --loglevel=info

# 스케줄러 실행
celery -A tasks beat --loglevel=info

# 모니터링
celery -A tasks flower

PHP 비교:
- Laravel Queue/Horizon과 유사
- Redis 드라이버 사용 시 거의 동일
- Celery가 더 다양한 기능 제공
"""
