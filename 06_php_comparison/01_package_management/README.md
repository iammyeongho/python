# 1. Python과 PHP의 패키지 관리 비교

이 디렉토리는 Python과 PHP의 패키지 관리 시스템을 비교하는 예제를 포함합니다.

## 주요 내용

- 패키지 매니저 비교 (pip vs Composer)
- 가상 환경 설정
- 의존성 관리
- 패키지 배포
- 버전 관리

## 예제 파일

- `package_management.py`: Python의 패키지 관리 예제

## 주요 차이점

1. **패키지 매니저**
   - Python: `pip` 사용
   - PHP: `Composer` 사용

2. **의존성 파일**
   - Python: `requirements.txt` 또는 `pyproject.toml`
   - PHP: `composer.json`

3. **가상 환경**
   - Python: `venv`, `virtualenv`, `pipenv`
   - PHP: `.env` 파일 또는 환경 변수

4. **패키지 배포**
   - Python: PyPI 사용
   - PHP: Packagist 사용

## 실행 방법

```bash
# 가상 환경 생성
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 또는
.\venv\Scripts\activate  # Windows

# 의존성 설치
pip install -r requirements.txt

# 예제 실행
python package_management.py
```

## 필요한 패키지

- pip (Python 기본 패키지 매니저)
- setuptools (Python 기본 패키지)
- wheel (Python 기본 패키지) 