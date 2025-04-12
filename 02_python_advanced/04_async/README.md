# 9. Python과 PHP의 비동기 프로그래밍 비교

이 디렉토리는 Python과 PHP의 비동기 프로그래밍을 비교하는 예제를 포함합니다.

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