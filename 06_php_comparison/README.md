# Python과 PHP 비교

이 디렉토리는 Python과 PHP의 주요 차이점을 비교하는 자료를 포함하고 있습니다.

## 학습 내용

1. **01_syntax_comparison/** - 문법 비교
   - 변수 선언
   - 데이터 타입
   - 연산자
   - 제어 구조
   - 함수 정의

2. **02_oop_comparison/** - 객체지향 프로그래밍 비교
   - 클래스 정의
   - 상속
   - 인터페이스
   - 트레이트
   - 매직 메서드

3. **03_web_comparison/** - 웹 개발 비교
   - 프레임워크
   - 라우팅
   - 미들웨어
   - 템플릿 엔진
   - 세션 관리

4. **04_database_comparison/** - 데이터베이스 비교
   - ORM
   - 쿼리 빌더
   - 마이그레이션
   - 트랜잭션
   - 관계 정의

## 주요 차이점

1. **문법**
   - PHP: `$` 기호로 변수 선언, 세미콜론 필수
   - Python: 변수 선언 시 `$` 불필요, 들여쓰기로 블록 구분

2. **객체지향**
   - PHP: 명시적인 접근 제어자, 인터페이스와 트레이트
   - Python: 암묵적인 접근 제어, 믹스인과 추상 클래스

3. **웹 개발**
   - PHP: 내장 웹 서버, 전역 변수
   - Python: WSGI, 미들웨어 스택

4. **데이터베이스**
   - PHP: PDO, Eloquent
   - Python: SQLAlchemy, Django ORM

## 학습 순서

1. 문법 비교 (01_syntax_comparison)를 통해 기본적인 차이점을 이해
2. 객체지향 비교 (02_oop_comparison)를 통해 OOP 패러다임의 차이를 학습
3. 웹 개발 비교 (03_web_comparison)를 통해 웹 프레임워크의 차이를 이해
4. 데이터베이스 비교 (04_database_comparison)를 통해 ORM의 차이를 학습

## 예제 실행 방법

각 비교 예제는 독립적으로 실행 가능합니다:

```bash
# 문법 비교
python 01_syntax_comparison/syntax_examples.py

# 객체지향 비교
python 02_oop_comparison/oop_examples.py

# 웹 개발 비교
python 03_web_comparison/web_examples.py

# 데이터베이스 비교
python 04_database_comparison/database_examples.py
```

## PHP에서 Python으로 전환 시 주의사항

1. **문법**
   - 들여쓰기에 주의
   - 세미콜론 불필요
   - 변수 선언 시 `$` 불필요

2. **객체지향**
   - 접근 제어자가 다름
   - 매직 메서드 이름이 다름
   - 상속 방식이 다름

3. **웹 개발**
   - 프레임워크 구조가 다름
   - 미들웨어 처리 방식이 다름
   - 템플릿 엔진 문법이 다름

4. **데이터베이스**
   - ORM 문법이 다름
   - 쿼리 빌더 사용법이 다름
   - 마이그레이션 방식이 다름

## 추가 자료

1. Python 공식 문서
2. PHP 공식 문서
3. 각 프레임워크의 공식 문서
4. ORM 라이브러리 문서 