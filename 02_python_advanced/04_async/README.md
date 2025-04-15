# 비동기 프로그래밍

이 디렉토리는 파이썬의 비동기 프로그래밍 개념을 다룹니다.

## 파일 구조

1. `01_basic_async.py`: 비동기 프로그래밍의 기본 개념
2. `02_coroutines.py`: 코루틴과 async/await
3. `03_tasks.py`: 태스크와 이벤트 루프
4. `04_futures.py`: Future 객체와 콜백
5. `05_streams.py`: 비동기 스트림
6. `06_websockets.py`: WebSocket 클라이언트/서버
7. `07_advanced_async.py`: 고급 비동기 프로그래밍
8. `08_async_db.py`: 비동기 데이터베이스 접근

각 파일은 해당 주제에 대한 예제 코드와 설명을 포함하고 있습니다.

## 주요 내용

- Python의 `asyncio`와 PHP의 비동기 프로그래밍 비교
- 코루틴과 Promise 비교
- 비동기 HTTP 요청 처리
- 병렬 작업 처리
- 비동기 큐 패턴

## 예제 파일

- `async_programming.py`: Python의 비동기 프로그래밍 예제

## 주요 차이점

1. **구현 방식**
   - Python: `asyncio` 라이브러리를 사용한 코루틴 기반
   - PHP: Promise 기반 (ReactPHP, Amp 등)

2. **문법**
   - Python: `async/await` 키워드 사용
   - PHP: `async/await` 또는 Promise 체이닝

3. **이벤트 루프**
   - Python: `asyncio.get_event_loop()`
   - PHP: ReactPHP의 `Loop` 또는 Amp의 `Loop`

## 실행 방법

```bash
python async_programming.py
```

## 필요한 패키지

- aiohttp
- asyncio (Python 3.7+ 기본 내장) 