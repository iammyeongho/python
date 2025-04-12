"""
Python과 PHP의 패키지 관리 비교 예제
이 파일은 PHP 개발자가 Python의 패키지 관리 방식을 이해하는 데 도움을 주기 위한 예제입니다.
"""

import sys
import subprocess
from pathlib import Path
from typing import List, Dict, Optional
import json
import pkg_resources

class PackageManager:
    """패키지 관리 유틸리티 클래스"""
    
    @staticmethod
    def create_venv(venv_path: str) -> None:
        """
        가상 환경 생성
        PHP의 .env 파일과 유사한 개념
        """
        try:
            subprocess.run([sys.executable, "-m", "venv", venv_path], check=True)
            print(f"Created virtual environment at {venv_path}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to create virtual environment: {e}")
            raise
    
    @staticmethod
    def install_packages(packages: List[str]) -> None:
        """
        패키지 설치
        PHP의 composer require와 유사
        """
        try:
            subprocess.run([sys.executable, "-m", "pip", "install"] + packages, check=True)
            print(f"Installed packages: {packages}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install packages: {e}")
            raise
    
    @staticmethod
    def freeze_requirements(output_file: str = "requirements.txt") -> None:
        """
        현재 설치된 패키지 목록을 requirements.txt로 저장
        PHP의 composer.json과 유사
        """
        try:
            with open(output_file, "w") as f:
                subprocess.run([sys.executable, "-m", "pip", "freeze"], stdout=f, check=True)
            print(f"Saved requirements to {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to freeze requirements: {e}")
            raise
    
    @staticmethod
    def load_requirements(requirements_file: str = "requirements.txt") -> List[str]:
        """
        requirements.txt 파일에서 패키지 목록 로드
        """
        try:
            with open(requirements_file, "r") as f:
                return [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"Requirements file {requirements_file} not found")
            return []
    
    @staticmethod
    def create_pyproject_toml(project_name: str, version: str, dependencies: List[str]) -> None:
        """
        pyproject.toml 파일 생성
        PHP의 composer.json과 유사한 설정 파일
        """
        config = {
            "build-system": {
                "requires": ["setuptools>=42", "wheel"],
                "build-backend": "setuptools.build_meta"
            },
            "project": {
                "name": project_name,
                "version": version,
                "dependencies": dependencies
            }
        }
        
        try:
            with open("pyproject.toml", "w") as f:
                f.write("[build-system]\n")
                f.write("requires = [\"setuptools>=42\", \"wheel\"]\n")
                f.write("build-backend = \"setuptools.build_meta\"\n\n")
                f.write(f"[project]\n")
                f.write(f"name = \"{project_name}\"\n")
                f.write(f"version = \"{version}\"\n")
                f.write("dependencies = [\n")
                for dep in dependencies:
                    f.write(f"    \"{dep}\",\n")
                f.write("]\n")
            print("Created pyproject.toml")
        except Exception as e:
            print(f"Failed to create pyproject.toml: {e}")
            raise
    
    @staticmethod
    def get_installed_packages() -> Dict[str, str]:
        """
        설치된 패키지 목록 조회
        PHP의 composer show와 유사
        """
        return {pkg.key: pkg.version for pkg in pkg_resources.working_set}
    
    @staticmethod
    def check_package_version(package_name: str) -> Optional[str]:
        """
        특정 패키지 버전 확인
        """
        try:
            return pkg_resources.get_distribution(package_name).version
        except pkg_resources.DistributionNotFound:
            return None

def main():
    """메인 실행 함수"""
    # 가상 환경 생성 예제
    venv_path = "venv"
    PackageManager.create_venv(venv_path)
    
    # 패키지 설치 예제
    packages = ["requests", "flask", "sqlalchemy"]
    PackageManager.install_packages(packages)
    
    # requirements.txt 생성 예제
    PackageManager.freeze_requirements()
    
    # pyproject.toml 생성 예제
    project_name = "my_project"
    version = "0.1.0"
    dependencies = ["requests>=2.25.0", "flask>=2.0.0", "sqlalchemy>=1.4.0"]
    PackageManager.create_pyproject_toml(project_name, version, dependencies)
    
    # 설치된 패키지 확인 예제
    installed_packages = PackageManager.get_installed_packages()
    print("\nInstalled packages:")
    for name, version in installed_packages.items():
        print(f"{name}=={version}")
    
    # 특정 패키지 버전 확인 예제
    package_name = "requests"
    version = PackageManager.check_package_version(package_name)
    if version:
        print(f"\n{package_name} version: {version}")
    else:
        print(f"\n{package_name} is not installed")

if __name__ == "__main__":
    main() 