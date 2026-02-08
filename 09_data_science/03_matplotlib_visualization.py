"""
Matplotlib 시각화
=====================================
데이터 시각화를 위한 Matplotlib 라이브러리
pip install matplotlib
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 한글 폰트 설정 (macOS)
# plt.rcParams['font.family'] = 'AppleGothic'
# plt.rcParams['axes.unicode_minus'] = False

# =============================================================================
# 1. 기본 선 그래프 (Line Plot)
# =============================================================================

print("=== 선 그래프 ===")

# 데이터
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 그래프 생성
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)
plt.plot(x, np.cos(x), label='cos(x)', color='red', linestyle='--')

# 꾸미기
plt.title('Sine and Cosine Functions')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True, alpha=0.3)

# 저장 및 표시
plt.savefig('01_line_plot.png', dpi=150, bbox_inches='tight')
plt.close()
print("01_line_plot.png 저장됨")


# =============================================================================
# 2. 막대 그래프 (Bar Chart)
# =============================================================================

print("\n=== 막대 그래프 ===")

categories = ['Python', 'JavaScript', 'Java', 'C++', 'Go']
values = [30, 25, 20, 15, 10]

plt.figure(figsize=(10, 6))

# 수직 막대
plt.subplot(1, 2, 1)
bars = plt.bar(categories, values, color=['#3776AB', '#F7DF1E', '#B07219', '#00599C', '#00ADD8'])
plt.title('Programming Languages (Vertical)')
plt.ylabel('Popularity (%)')

# 값 표시
for bar, val in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             str(val), ha='center', va='bottom')

# 수평 막대
plt.subplot(1, 2, 2)
plt.barh(categories, values, color='steelblue')
plt.title('Programming Languages (Horizontal)')
plt.xlabel('Popularity (%)')

plt.tight_layout()
plt.savefig('02_bar_chart.png', dpi=150, bbox_inches='tight')
plt.close()
print("02_bar_chart.png 저장됨")


# =============================================================================
# 3. 산점도 (Scatter Plot)
# =============================================================================

print("\n=== 산점도 ===")

np.random.seed(42)
x = np.random.randn(100)
y = 2 * x + np.random.randn(100) * 0.5
colors = np.random.rand(100)
sizes = np.random.rand(100) * 500

plt.figure(figsize=(10, 6))
scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')
plt.colorbar(scatter, label='Color Value')

plt.title('Scatter Plot with Color and Size')
plt.xlabel('X')
plt.ylabel('Y')

plt.savefig('03_scatter_plot.png', dpi=150, bbox_inches='tight')
plt.close()
print("03_scatter_plot.png 저장됨")


# =============================================================================
# 4. 히스토그램 (Histogram)
# =============================================================================

print("\n=== 히스토그램 ===")

data = np.random.randn(1000)

plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.hist(data, bins=30, color='steelblue', edgecolor='white', alpha=0.7)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

# 밀도 히스토그램
plt.subplot(1, 2, 2)
plt.hist(data, bins=30, density=True, color='coral', edgecolor='white', alpha=0.7)
plt.title('Density Histogram')
plt.xlabel('Value')
plt.ylabel('Density')

plt.tight_layout()
plt.savefig('04_histogram.png', dpi=150, bbox_inches='tight')
plt.close()
print("04_histogram.png 저장됨")


# =============================================================================
# 5. 원 그래프 (Pie Chart)
# =============================================================================

print("\n=== 원 그래프 ===")

labels = ['Python', 'JavaScript', 'Java', 'C++', 'Others']
sizes = [30, 25, 20, 15, 10]
explode = (0.1, 0, 0, 0, 0)  # Python 강조
colors = ['#3776AB', '#F7DF1E', '#B07219', '#00599C', '#808080']

plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Programming Language Market Share')

# 도넛 차트
plt.subplot(1, 2, 2)
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
        pctdistance=0.85, startangle=90)
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
plt.gca().add_artist(centre_circle)
plt.title('Donut Chart')

plt.tight_layout()
plt.savefig('05_pie_chart.png', dpi=150, bbox_inches='tight')
plt.close()
print("05_pie_chart.png 저장됨")


# =============================================================================
# 6. 박스 플롯 (Box Plot)
# =============================================================================

print("\n=== 박스 플롯 ===")

data1 = np.random.normal(100, 10, 200)
data2 = np.random.normal(90, 20, 200)
data3 = np.random.normal(80, 30, 200)

plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.boxplot([data1, data2, data3], labels=['Group A', 'Group B', 'Group C'])
plt.title('Box Plot')
plt.ylabel('Value')

# 바이올린 플롯
plt.subplot(1, 2, 2)
plt.violinplot([data1, data2, data3], positions=[1, 2, 3])
plt.xticks([1, 2, 3], ['Group A', 'Group B', 'Group C'])
plt.title('Violin Plot')
plt.ylabel('Value')

plt.tight_layout()
plt.savefig('06_box_plot.png', dpi=150, bbox_inches='tight')
plt.close()
print("06_box_plot.png 저장됨")


# =============================================================================
# 7. 히트맵 (Heatmap)
# =============================================================================

print("\n=== 히트맵 ===")

# 상관관계 행렬
np.random.seed(42)
data = np.random.rand(5, 5)
labels = ['A', 'B', 'C', 'D', 'E']

plt.figure(figsize=(8, 6))
im = plt.imshow(data, cmap='coolwarm')
plt.colorbar(im)

# 레이블
plt.xticks(range(5), labels)
plt.yticks(range(5), labels)

# 값 표시
for i in range(5):
    for j in range(5):
        plt.text(j, i, f'{data[i, j]:.2f}',
                 ha='center', va='center', color='white')

plt.title('Heatmap')
plt.savefig('07_heatmap.png', dpi=150, bbox_inches='tight')
plt.close()
print("07_heatmap.png 저장됨")


# =============================================================================
# 8. 서브플롯 (Subplots)
# =============================================================================

print("\n=== 서브플롯 ===")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 첫 번째 그래프
x = np.linspace(0, 10, 100)
axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title('Sine Wave')

# 두 번째 그래프
axes[0, 1].scatter(np.random.rand(50), np.random.rand(50))
axes[0, 1].set_title('Random Scatter')

# 세 번째 그래프
axes[1, 0].bar(['A', 'B', 'C', 'D'], [3, 7, 5, 4])
axes[1, 0].set_title('Bar Chart')

# 네 번째 그래프
axes[1, 1].hist(np.random.randn(500), bins=20)
axes[1, 1].set_title('Histogram')

plt.tight_layout()
plt.savefig('08_subplots.png', dpi=150, bbox_inches='tight')
plt.close()
print("08_subplots.png 저장됨")


# =============================================================================
# 9. 스타일 설정
# =============================================================================

print("\n=== 스타일 ===")

# 사용 가능한 스타일 확인
# print(plt.style.available)

# 스타일 적용 예제
styles = ['default', 'seaborn-v0_8', 'ggplot', 'dark_background']

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

x = np.linspace(0, 10, 100)

for ax, style in zip(axes.flat, styles):
    try:
        with plt.style.context(style):
            ax.plot(x, np.sin(x), label='sin')
            ax.plot(x, np.cos(x), label='cos')
            ax.set_title(f'Style: {style}')
            ax.legend()
    except:
        ax.plot(x, np.sin(x), label='sin')
        ax.set_title(f'Style: {style} (fallback)')

plt.tight_layout()
plt.savefig('09_styles.png', dpi=150, bbox_inches='tight')
plt.close()
print("09_styles.png 저장됨")


# =============================================================================
# 10. Pandas와 함께 사용
# =============================================================================

print("\n=== Pandas 연동 ===")

# 예제 데이터
dates = pd.date_range('2024-01-01', periods=30, freq='D')
df = pd.DataFrame({
    'date': dates,
    'sales': np.random.randint(100, 500, 30),
    'visitors': np.random.randint(1000, 5000, 30),
    'category': np.random.choice(['A', 'B', 'C'], 30)
})

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 시계열 그래프
axes[0, 0].plot(df['date'], df['sales'], marker='o', markersize=3)
axes[0, 0].set_title('Daily Sales')
axes[0, 0].tick_params(axis='x', rotation=45)

# 막대 그래프
df.groupby('category')['sales'].mean().plot(kind='bar', ax=axes[0, 1], color='steelblue')
axes[0, 1].set_title('Average Sales by Category')
axes[0, 1].set_xlabel('Category')

# 산점도
axes[1, 0].scatter(df['visitors'], df['sales'], alpha=0.6)
axes[1, 0].set_title('Visitors vs Sales')
axes[1, 0].set_xlabel('Visitors')
axes[1, 0].set_ylabel('Sales')

# 히스토그램
df['sales'].plot(kind='hist', bins=15, ax=axes[1, 1], color='coral', edgecolor='white')
axes[1, 1].set_title('Sales Distribution')

plt.tight_layout()
plt.savefig('10_pandas_plot.png', dpi=150, bbox_inches='tight')
plt.close()
print("10_pandas_plot.png 저장됨")


# =============================================================================
# 11. 그래프 커스터마이징
# =============================================================================

print("\n=== 커스터마이징 ===")

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots(figsize=(12, 6))

# 선 스타일
ax.plot(x, y1, 'b-', linewidth=2, label='sin(x)')
ax.plot(x, y2, 'r--', linewidth=2, label='cos(x)')

# 영역 채우기
ax.fill_between(x, y1, alpha=0.3)

# 수직/수평선
ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
ax.axvline(x=5, color='g', linestyle=':', linewidth=1)

# 텍스트 추가
ax.annotate('Maximum', xy=(1.57, 1), xytext=(3, 1.2),
            arrowprops=dict(arrowstyle='->', color='black'),
            fontsize=10)

# 레이블과 제목
ax.set_xlabel('X Axis', fontsize=12)
ax.set_ylabel('Y Axis', fontsize=12)
ax.set_title('Customized Plot', fontsize=14, fontweight='bold')

# 범례
ax.legend(loc='upper right', frameon=True, shadow=True)

# 축 범위
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)

# 그리드
ax.grid(True, linestyle='--', alpha=0.7)

# 테두리 스타일
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.savefig('11_customized.png', dpi=150, bbox_inches='tight')
plt.close()
print("11_customized.png 저장됨")


# =============================================================================
# 정리: Matplotlib 핵심 기능
# =============================================================================

"""
Matplotlib 핵심:

1. 기본 그래프
   - plot(): 선 그래프
   - bar(), barh(): 막대 그래프
   - scatter(): 산점도
   - hist(): 히스토그램
   - pie(): 원 그래프

2. 레이아웃
   - subplots(): 여러 그래프
   - tight_layout(): 자동 레이아웃

3. 꾸미기
   - title(), xlabel(), ylabel()
   - legend(), grid()
   - savefig()

4. 스타일
   - plt.style.use()
   - colors, linewidth, alpha

5. Pandas 연동
   - df.plot()
   - df['col'].plot(kind='bar')

대안 라이브러리:
- Seaborn: 통계 시각화 (더 예쁜 기본값)
- Plotly: 인터랙티브 그래프
- Bokeh: 웹 기반 시각화

PHP에서는 Chart.js 등 JS 라이브러리 사용이 일반적
Python은 데이터 분석과 시각화가 통합된 환경 제공
"""

print("\n모든 그래프가 저장되었습니다.")
