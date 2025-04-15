"""
파이썬 환경 설정 가이드
이 파일은 파이썬 개발 환경을 설정하는 방법을 설명합니다.
"""

# 1. 파이썬 설치
"""
1. 파이썬 공식 웹사이트(https://www.python.org/downloads/)에서 최신 버전 다운로드
2. 설치 시 'Add Python to PATH' 옵션 체크
3. 설치 완료 후 터미널에서 다음 명령어로 확인:
   python --version
   pip --version
"""

# 2. 환경 변수 설정
"""
Windows:
1. 시스템 속성 > 고급 > 환경 변수
2. 시스템 변수에서 Path 편집
3. Python 설치 경로와 Scripts 폴더 경로 추가
   예: C:\Python39\; C:\Python39\Scripts\

Linux/Mac:
~/.bashrc 또는 ~/.zshrc 파일에 다음 내용 추가:
export PATH="$PATH:/usr/local/bin/python3"
"""

# 3. 기본 개발 도구 설치
"""
1. 텍스트 에디터 또는 IDE 설치
   - VS Code: https://code.visualstudio.com/
   - PyCharm: https://www.jetbrains.com/pycharm/
   
2. VS Code 확장 프로그램 설치
   - Python
   - Pylance
   - Python Test Explorer
"""

# 4. 기본 설정 확인
import sys
import platform

print(f"Python 버전: {sys.version}")
print(f"운영체제: {platform.system()} {platform.release()}")
print(f"파이썬 경로: {sys.executable}")

# 5. 기본 패키지 설치
"""
다음 명령어로 기본 개발 도구 설치:
pip install black pylint pytest
"""

print("\n환경 설정 가이드가 완료되었습니다.") 