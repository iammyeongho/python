"""
2. Python 가상환경 설정 가이드
PHP 개발자를 위한 Python 가상 환경 가이드
이 파일은 PHP 개발자가 Python의 가상 환경을 이해하는 데 도움을 주기 위한 예제입니다.
"""

import os
import sys
import subprocess
from typing import List, Dict, Any

class VirtualEnvGuide:
    """가상 환경 가이드 클래스"""

    def __init__(self):
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.venv_dir = os.path.join(self.current_dir, "venv")
        self.requirements_file = os.path.join(self.current_dir, "requirements.txt")

    def create_venv(self) -> None:
        """
        가상 환경 생성
        PHP의 composer와 유사한 역할
        """
        print("Creating virtual environment...")
        try:
            # Python 3의 venv 모듈을 사용하여 가상 환경 생성
            subprocess.run([sys.executable, "-m", "venv", self.venv_dir], check=True)
            print(f"Virtual environment created at: {self.venv_dir}")
        except subprocess.CalledProcessError as e:
            print(f"Error creating virtual environment: {e}")
            sys.exit(1)

    def activate_venv(self) -> None:
        """
        가상 환경 활성화
        """
        if sys.platform == "win32":
            activate_script = os.path.join(self.venv_dir, "Scripts", "activate")
        else:
            activate_script = os.path.join(self.venv_dir, "bin", "activate")

        print(f"\nTo activate the virtual environment, run:")
        print(f"source {activate_script}  # On Unix/MacOS")
        print(f"{activate_script}  # On Windows")

    def install_requirements(self) -> None:
        """
        requirements.txt에서 패키지 설치
        PHP의 composer.json과 유사한 역할
        """
        if not os.path.exists(self.requirements_file):
            print(f"Creating {self.requirements_file}...")
            with open(self.requirements_file, "w") as f:
                f.write("# Python 패키지 의존성\n")
                f.write("requests==2.31.0\n")
                f.write("flask==2.3.3\n")
                f.write("sqlalchemy==2.0.20\n")
                f.write("pytest==7.4.0\n")

        print("\nInstalling requirements...")
        try:
            pip_path = os.path.join(self.venv_dir, "bin", "pip")
            if sys.platform == "win32":
                pip_path = os.path.join(self.venv_dir, "Scripts", "pip.exe")

            subprocess.run([pip_path, "install", "-r", self.requirements_file], check=True)
            print("Requirements installed successfully")
        except subprocess.CalledProcessError as e:
            print(f"Error installing requirements: {e}")
            sys.exit(1)

    def show_installed_packages(self) -> None:
        """
        설치된 패키지 목록 표시
        PHP의 composer show와 유사
        """
        print("\nInstalled packages:")
        try:
            pip_path = os.path.join(self.venv_dir, "bin", "pip")
            if sys.platform == "win32":
                pip_path = os.path.join(self.venv_dir, "Scripts", "pip.exe")

            result = subprocess.run([pip_path, "list"], capture_output=True, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error listing packages: {e}")

    def create_project_structure(self) -> None:
        """
        기본 프로젝트 구조 생성
        """
        print("\nCreating project structure...")
        directories = [
            "src",
            "tests",
            "docs",
            "config"
        ]

        for directory in directories:
            dir_path = os.path.join(self.current_dir, directory)
            os.makedirs(dir_path, exist_ok=True)
            print(f"Created directory: {directory}")

        # 기본 파일 생성
        files = {
            "src/__init__.py": "",
            "tests/__init__.py": "",
            "README.md": "# Python Project\n\nThis is a Python project created with virtualenv guide.",
            ".gitignore": "venv/\n__pycache__/\n*.pyc\n.env\n"
        }

        for file_path, content in files.items():
            full_path = os.path.join(self.current_dir, file_path)
            with open(full_path, "w") as f:
                f.write(content)
            print(f"Created file: {file_path}")

def main():
    """메인 함수"""
    guide = VirtualEnvGuide()
    
    print("=== Python Virtual Environment Guide ===")
    print("This guide will help you set up a Python virtual environment")
    print("similar to PHP's Composer environment.\n")
    
    # 가상 환경 생성
    guide.create_venv()
    
    # 가상 환경 활성화 방법 표시
    guide.activate_venv()
    
    # requirements.txt 생성 및 패키지 설치
    guide.install_requirements()
    
    # 설치된 패키지 목록 표시
    guide.show_installed_packages()
    
    # 프로젝트 구조 생성
    guide.create_project_structure()
    
    print("\nSetup completed successfully!")
    print("\nNext steps:")
    print("1. Activate the virtual environment")
    print("2. Start coding in the src directory")
    print("3. Run tests in the tests directory")
    print("4. Add new packages to requirements.txt")

if __name__ == "__main__":
    main() 