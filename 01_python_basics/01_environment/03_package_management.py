"""
3. Python 패키지 관리 가이드
이 파일은 PHP 개발자가 Python의 패키지 관리를 이해하는 데 도움을 주기 위한 예제입니다.
"""

import os
import sys
import subprocess
from typing import List, Dict, Any
from pathlib import Path

class PackageManager:
    """패키지 관리 클래스"""

    def __init__(self):
        self.current_dir = Path(__file__).parent
        self.setup_py = self.current_dir / "setup.py"
        self.requirements_txt = self.current_dir / "requirements.txt"
        self.pipfile = self.current_dir / "Pipfile"
        self.poetry_toml = self.current_dir / "pyproject.toml"

    def create_setup_py(self) -> None:
        """
        setup.py 파일 생성
        PHP의 composer.json과 유사한 역할
        """
        content = """from setuptools import setup, find_packages

setup(
    name="my_python_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "flask>=2.3.3",
        "sqlalchemy>=2.0.20",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "black>=23.7.0",
            "flake8>=6.1.0",
        ],
    },
    python_requires=">=3.8",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python package example",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_python_package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
"""
        self.setup_py.write_text(content)
        print(f"Created {self.setup_py}")

    def create_requirements_txt(self) -> None:
        """
        requirements.txt 파일 생성
        """
        content = """# 기본 의존성
requests==2.31.0
flask==2.3.3
sqlalchemy==2.0.20

# 개발 의존성
pytest==7.4.0
black==23.7.0
flake8==6.1.0
"""
        self.requirements_txt.write_text(content)
        print(f"Created {self.requirements_txt}")

    def create_pipfile(self) -> None:
        """
        Pipfile 생성 (pipenv 사용)
        """
        content = """[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
requests = "==2.31.0"
flask = "==2.3.3"
sqlalchemy = "==2.0.20"

[dev-packages]
pytest = "==7.4.0"
black = "==23.7.0"
flake8 = "==6.1.0"

[requires]
python_version = "3.8"
"""
        self.pipfile.write_text(content)
        print(f"Created {self.pipfile}")

    def create_poetry_toml(self) -> None:
        """
        pyproject.toml 생성 (poetry 사용)
        """
        content = """[tool.poetry]
name = "my_python_package"
version = "0.1.0"
description = "A Python package example"
authors = ["Your Name <your.email@example.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.8"
requests = "2.31.0"
flask = "2.3.3"
sqlalchemy = "2.0.20"

[tool.poetry.group.dev.dependencies]
pytest = "7.4.0"
black = "23.7.0"
flake8 = "6.1.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
"""
        self.poetry_toml.write_text(content)
        print(f"Created {self.poetry_toml}")

    def install_package(self, method: str = "pip") -> None:
        """
        패키지 설치
        """
        print(f"\nInstalling package using {method}...")
        
        if method == "pip":
            cmd = [sys.executable, "-m", "pip", "install", "-e", "."]
        elif method == "pipenv":
            cmd = ["pipenv", "install", "-e", "."]
        elif method == "poetry":
            cmd = ["poetry", "install"]
        else:
            print(f"Unknown method: {method}")
            return

        try:
            subprocess.run(cmd, check=True)
            print(f"Package installed successfully using {method}")
        except subprocess.CalledProcessError as e:
            print(f"Error installing package: {e}")

    def show_installed_packages(self) -> None:
        """
        설치된 패키지 목록 표시
        """
        print("\nInstalled packages:")
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "list"],
                capture_output=True,
                text=True
            )
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error listing packages: {e}")

def main():
    """메인 함수"""
    manager = PackageManager()
    
    print("=== Python Package Management Guide ===")
    print("This guide will help you understand Python package management")
    print("similar to PHP's Composer.\n")
    
    # 패키지 관리 파일 생성
    manager.create_setup_py()
    manager.create_requirements_txt()
    manager.create_pipfile()
    manager.create_poetry_toml()
    
    # 패키지 설치 (기본적으로 pip 사용)
    manager.install_package("pip")
    
    # 설치된 패키지 목록 표시
    manager.show_installed_packages()
    
    print("\nPackage management setup completed!")
    print("\nAvailable package management methods:")
    print("1. pip (기본)")
    print("2. pipenv (Composer와 유사)")
    print("3. poetry (Composer와 유사)")
    print("\nTo use a different method, run:")
    print("python package_management.py --method pipenv")
    print("or")
    print("python package_management.py --method poetry")

if __name__ == "__main__":
    # 명령줄 인수 처리
    method = "pip"
    if len(sys.argv) > 1 and sys.argv[1] == "--method":
        method = sys.argv[2]
    
    main() 