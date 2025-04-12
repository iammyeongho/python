# 10. Python과 PHP의 웹 프레임워크 비교

이 디렉토리는 Python과 PHP의 웹 프레임워크를 비교하는 예제를 포함합니다.

## 주요 내용

- Flask/Django vs Laravel/Symfony
- 라우팅 시스템
- 미들웨어 처리
- 템플릿 엔진
- ORM 통합

## 예제 파일

- `flask_example.py`: Flask 예제
- `django_example.py`: Django 예제

## 주요 차이점

1. **프레임워크 구조**
   - Python: Flask(마이크로), Django(풀스택)
   - PHP: Laravel(풀스택), Symfony(모듈식)

2. **라우팅**
   - Python: 데코레이터 기반 또는 URLconf
   - PHP: 라우트 정의 파일 또는 어노테이션

3. **템플릿 엔진**
   - Python: Jinja2, Django Template
   - PHP: Blade, Twig

4. **ORM**
   - Python: SQLAlchemy, Django ORM
   - PHP: Eloquent, Doctrine

## 실행 방법

```bash
# Flask 예제 실행
python flask_example.py

# Django 예제 실행
python manage.py runserver
```

## 필요한 패키지

- Flask
- Django
- SQLAlchemy
- Jinja2 