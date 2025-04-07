# 파이썬 패키지 개발과 배포

# 1. 기본 패키지 구조
print("=== 기본 패키지 구조 예제 ===")

"""
my_package/
    ├── my_package/
    │   ├── __init__.py
    │   ├── core.py
    │   └── utils.py
    ├── tests/
    │   ├── __init__.py
    │   └── test_core.py
    ├── setup.py
    ├── setup.cfg
    ├── pyproject.toml
    ├── README.md
    └── LICENSE
"""

# 2. setup.py 예제
print("\n=== setup.py 예제 ===")

"""
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "pandas>=1.2.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.9",
        ],
    },
    author="홍길동",
    author_email="hong@example.com",
    description="간단한 파이썬 패키지 예제",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/username/my_package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
"""

# 3. pyproject.toml 예제
print("\n=== pyproject.toml 예제 ===")

"""
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[tool.black]
line-length = 88
target-version = ['py37']
include = '\.pyi?$'

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
addopts = "-ra -q"
"""

# 4. 패키지 초기화 파일
print("\n=== __init__.py 예제 ===")

"""
# Version 정보
__version__ = "0.1.0"

# 주요 기능 임포트
from .core import main_function
from .utils import helper_function

# 공개 API 정의
__all__ = ["main_function", "helper_function"]
"""

# 5. 테스트 작성 예제
print("\n=== 테스트 작성 예제 ===")

"""
import pytest
from my_package.core import calculate_sum

def test_calculate_sum():
    assert calculate_sum(1, 2) == 3
    assert calculate_sum(-1, 1) == 0
    assert calculate_sum(0, 0) == 0

def test_calculate_sum_invalid_input():
    with pytest.raises(TypeError):
        calculate_sum("1", 2)
"""

# 6. 문서화 예제
print("\n=== 문서화 예제 ===")

"""
def process_data(data: list, threshold: float = 0.5) -> dict:
    \"\"\"데이터를 처리하고 결과를 반환합니다.

    Args:
        data (list): 처리할 데이터 리스트
        threshold (float, optional): 처리 기준값. 기본값은 0.5입니다.

    Returns:
        dict: 처리 결과를 담은 딕셔너리
            - 'count': 처리된 항목 수
            - 'average': 평균값
            - 'above_threshold': 기준값을 초과하는 항목 수

    Raises:
        ValueError: 데이터가 비어있는 경우
        TypeError: 데이터 타입이 올바르지 않은 경우

    Examples:
        >>> data = [1, 2, 3, 4, 5]
        >>> result = process_data(data, threshold=3)
        >>> print(result)
        {'count': 5, 'average': 3.0, 'above_threshold': 2}
    \"\"\"
    if not data:
        raise ValueError("데이터가 비어있습니다.")
    
    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("모든 데이터는 숫자여야 합니다.")
    
    count = len(data)
    average = sum(data) / count
    above_threshold = sum(1 for x in data if x > threshold)
    
    return {
        'count': count,
        'average': average,
        'above_threshold': above_threshold
    }
"""

# 7. 패키지 배포 예제
print("\n=== 패키지 배포 예제 ===")

"""
# 1. 패키지 빌드
# python -m pip install --upgrade build
# python -m build

# 2. PyPI에 배포
# python -m pip install --upgrade twine
# python -m twine upload dist/*

# 3. 테스트 PyPI에 배포
# python -m twine upload --repository testpypi dist/*
"""

# 8. 의존성 관리 예제
print("\n=== 의존성 관리 예제 ===")

"""
# requirements.txt 예제
requests==2.25.1
pandas>=1.2.0
numpy~=1.19.0
"""

# 9. 개발 환경 설정 예제
print("\n=== 개발 환경 설정 예제 ===")

"""
# .env 파일 예제
DEBUG=True
API_KEY=your_api_key_here
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
"""

# 10. CI/CD 파이프라인 예제
print("\n=== CI/CD 파이프라인 예제 ===")

"""
# .github/workflows/python-package.yml 예제
name: Python Package

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.7, 3.8, 3.9]

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements-dev.txt
    - name: Lint with flake8
      run: flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
    - name: Test with pytest
      run: pytest
"""

# 11. 로깅 설정 예제
print("\n=== 로깅 설정 예제 ===")

"""
import logging
import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': 'app.log',
            'mode': 'a',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default', 'file'],
            'level': 'DEBUG',
            'propagate': True
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
"""

# 12. 설정 관리 예제
print("\n=== 설정 관리 예제 ===")

"""
from dataclasses import dataclass
from typing import Optional
import os
from pathlib import Path

@dataclass
class Config:
    debug: bool = False
    api_key: Optional[str] = None
    database_url: Optional[str] = None
    
    @classmethod
    def from_env(cls):
        return cls(
            debug=os.getenv('DEBUG', 'False').lower() == 'true',
            api_key=os.getenv('API_KEY'),
            database_url=os.getenv('DATABASE_URL')
        )
    
    def validate(self):
        if not self.api_key:
            raise ValueError("API_KEY가 설정되지 않았습니다.")
        if not self.database_url:
            raise ValueError("DATABASE_URL이 설정되지 않았습니다.")
""" 