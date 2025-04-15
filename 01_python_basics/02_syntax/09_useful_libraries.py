# 유용한 파이썬 라이브러리 예제

# 1. NumPy (수치 계산)
print("=== NumPy ===")

# NumPy 설치 필요: pip install numpy
try:
    import numpy as np
    
    # 배열 생성
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.zeros((3, 3))
    arr3 = np.ones((2, 4))
    arr4 = np.random.rand(2, 2)
    
    print("NumPy 배열:")
    print(f"1차원 배열: {arr1}")
    print(f"영행렬:\n{arr2}")
    print(f"1행렬:\n{arr3}")
    print(f"랜덤 행렬:\n{arr4}")
    
    # 배열 연산
    print("\n배열 연산:")
    print(f"합: {arr1 + 2}")
    print(f"곱: {arr1 * 2}")
    print(f"제곱: {arr1 ** 2}")
    
    # 통계 함수
    print("\n통계:")
    print(f"평균: {np.mean(arr1)}")
    print(f"표준편차: {np.std(arr1)}")
    print(f"최대값: {np.max(arr1)}")
    print(f"최소값: {np.min(arr1)}")
    
except ImportError:
    print("NumPy가 설치되어 있지 않습니다. 'pip install numpy' 명령으로 설치하세요.")

# 2. Pandas (데이터 분석)
print("\n=== Pandas ===")

# Pandas 설치 필요: pip install pandas
try:
    import pandas as pd
    
    # DataFrame 생성
    data = {
        '이름': ['홍길동', '김철수', '이영희'],
        '나이': [25, 30, 28],
        '직업': ['개발자', '디자이너', '마케터']
    }
    df = pd.DataFrame(data)
    
    print("DataFrame:")
    print(df)
    
    # 데이터 분석
    print("\n기본 통계:")
    print(df.describe())
    
    # 데이터 필터링
    print("\n나이가 28 이상인 사람:")
    print(df[df['나이'] >= 28])
    
    # 그룹화
    print("\n직업별 평균 나이:")
    print(df.groupby('직업')['나이'].mean())
    
except ImportError:
    print("Pandas가 설치되어 있지 않습니다. 'pip install pandas' 명령으로 설치하세요.")

# 3. Matplotlib (데이터 시각화)
print("\n=== Matplotlib ===")

# Matplotlib 설치 필요: pip install matplotlib
try:
    import matplotlib.pyplot as plt
    
    # 선 그래프
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label='sin(x)')
    plt.title('사인 함수')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    # plt.show()
    
    # 막대 그래프
    data = {'A': 10, 'B': 15, 'C': 7, 'D': 12}
    plt.figure(figsize=(8, 6))
    plt.bar(data.keys(), data.values())
    plt.title('막대 그래프')
    # plt.show()
    
except ImportError:
    print("Matplotlib이 설치되어 있지 않습니다. 'pip install matplotlib' 명령으로 설치하세요.")

# 4. Requests (HTTP 클라이언트)
print("\n=== Requests ===")

# Requests 설치 필요: pip install requests
try:
    import requests
    
    # GET 요청
    response = requests.get('https://api.github.com')
    print(f"상태 코드: {response.status_code}")
    print(f"헤더: {dict(response.headers)}")
    
    # POST 요청
    data = {'key': 'value'}
    response = requests.post('https://httpbin.org/post', json=data)
    print(f"\nPOST 응답: {response.json()}")
    
except ImportError:
    print("Requests가 설치되어 있지 않습니다. 'pip install requests' 명령으로 설치하세요.")

# 5. Beautiful Soup (웹 스크래핑)
print("\n=== Beautiful Soup ===")

# Beautiful Soup 설치 필요: pip install beautifulsoup4
try:
    from bs4 import BeautifulSoup
    
    # HTML 파싱
    html = """
    <html>
        <body>
            <h1>제목</h1>
            <p class="content">첫 번째 문단</p>
            <p class="content">두 번째 문단</p>
            <ul>
                <li>항목 1</li>
                <li>항목 2</li>
            </ul>
        </body>
    </html>
    """
    
    soup = BeautifulSoup(html, 'html.parser')
    
    print("HTML 파싱 결과:")
    print(f"제목: {soup.h1.text}")
    print("문단:")
    for p in soup.find_all('p', class_='content'):
        print(f"- {p.text}")
    print("리스트 항목:")
    for li in soup.find_all('li'):
        print(f"- {li.text}")
    
except ImportError:
    print("Beautiful Soup이 설치되어 있지 않습니다. 'pip install beautifulsoup4' 명령으로 설치하세요.")

# 6. Pillow (이미지 처리)
print("\n=== Pillow ===")

# Pillow 설치 필요: pip install Pillow
try:
    from PIL import Image, ImageDraw, ImageFilter
    
    # 새 이미지 생성
    img = Image.new('RGB', (200, 200), color='white')
    draw = ImageDraw.Draw(img)
    
    # 도형 그리기
    draw.rectangle([50, 50, 150, 150], fill='blue')
    draw.ellipse([75, 75, 125, 125], fill='red')
    
    # 이미지 필터 적용
    filtered = img.filter(ImageFilter.BLUR)
    
    # 이미지 저장
    # img.save('original.png')
    # filtered.save('filtered.png')
    
except ImportError:
    print("Pillow가 설치되어 있지 않습니다. 'pip install Pillow' 명령으로 설치하세요.")

# 7. PyQt (GUI 애플리케이션)
print("\n=== PyQt ===")

# PyQt5 설치 필요: pip install PyQt5
try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
    import sys
    
    """
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("PyQt 예제")
            self.setGeometry(100, 100, 300, 200)
            
            self.label = QLabel("안녕하세요!", self)
            self.label.move(110, 50)
            
            self.button = QPushButton("클릭", self)
            self.button.move(110, 80)
            self.button.clicked.connect(self.button_clicked)
        
        def button_clicked(self):
            self.label.setText("버튼이 클릭되었습니다!")
    
    # 애플리케이션 실행
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    """
    
except ImportError:
    print("PyQt5가 설치되어 있지 않습니다. 'pip install PyQt5' 명령으로 설치하세요.")

# 8. OpenCV (컴퓨터 비전)
print("\n=== OpenCV ===")

# OpenCV 설치 필요: pip install opencv-python
try:
    import cv2
    import numpy as np
    
    """
    # 이미지 생성
    img = np.zeros((300, 300, 3), dtype=np.uint8)
    
    # 도형 그리기
    cv2.line(img, (0, 0), (300, 300), (255, 0, 0), 3)
    cv2.rectangle(img, (50, 50), (250, 250), (0, 255, 0), 2)
    cv2.circle(img, (150, 150), 100, (0, 0, 255), -1)
    
    # 이미지 표시
    cv2.imshow('OpenCV 예제', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    """
    
except ImportError:
    print("OpenCV가 설치되어 있지 않습니다. 'pip install opencv-python' 명령으로 설치하세요.")

print("\n프로그램 종료") 