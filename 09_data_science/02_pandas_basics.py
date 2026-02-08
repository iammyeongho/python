"""
Pandas 기초
=====================================
데이터 분석을 위한 Pandas 라이브러리
pip install pandas
"""

import pandas as pd
import numpy as np

# =============================================================================
# 1. Series와 DataFrame
# =============================================================================

print("=== Series ===")

# Series: 1차원 데이터
s = pd.Series([1, 2, 3, 4, 5])
print(f"Series:\n{s}\n")

# 인덱스 지정
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(f"인덱스 있는 Series:\n{s}\n")

# 딕셔너리에서 생성
s = pd.Series({'apple': 100, 'banana': 200, 'cherry': 150})
print(f"딕셔너리 Series:\n{s}\n")


print("=== DataFrame ===")

# DataFrame: 2차원 데이터 (엑셀 스프레드시트와 유사)
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 28],
    'city': ['Seoul', 'Busan', 'Seoul', 'Incheon'],
    'salary': [50000, 60000, 70000, 55000]
})
print(f"DataFrame:\n{df}\n")


# =============================================================================
# 2. 데이터 읽기/쓰기
# =============================================================================

print("=== 데이터 I/O ===")

# CSV 파일 (가장 흔함)
# df = pd.read_csv('data.csv')
# df.to_csv('output.csv', index=False)

# Excel 파일
# df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
# df.to_excel('output.xlsx', index=False)

# JSON 파일
# df = pd.read_json('data.json')
# df.to_json('output.json', orient='records')

# SQL 데이터베이스
# from sqlalchemy import create_engine
# engine = create_engine('postgresql://user:pass@localhost/db')
# df = pd.read_sql('SELECT * FROM table', engine)
# df.to_sql('table', engine, if_exists='replace')

# 예제 데이터 생성 (CSV 읽기 시뮬레이션)
data = """name,age,city,salary
Alice,25,Seoul,50000
Bob,30,Busan,60000
Charlie,35,Seoul,70000
David,28,Incheon,55000"""

from io import StringIO
df = pd.read_csv(StringIO(data))
print(f"CSV에서 읽은 데이터:\n{df}\n")


# =============================================================================
# 3. 데이터 탐색
# =============================================================================

print("=== 데이터 탐색 ===")

# 기본 정보
print(f"형태: {df.shape}")        # (행, 열)
print(f"컬럼: {df.columns.tolist()}")
print(f"인덱스: {df.index.tolist()}")
print(f"\n데이터 타입:\n{df.dtypes}\n")

# 첫/마지막 행
print(f"처음 2행:\n{df.head(2)}\n")
print(f"마지막 2행:\n{df.tail(2)}\n")

# 통계 요약
print(f"통계 요약:\n{df.describe()}\n")

# 정보 확인 (null 체크 등)
print("데이터 정보:")
df.info()


# =============================================================================
# 4. 데이터 선택
# =============================================================================

print("\n=== 데이터 선택 ===")

# 열 선택
print(f"name 열:\n{df['name']}\n")
print(f"여러 열:\n{df[['name', 'age']]}\n")

# 행 선택 (loc: 레이블, iloc: 인덱스)
print(f"loc[0] (첫 번째 행):\n{df.loc[0]}\n")
print(f"iloc[0:2] (처음 2행):\n{df.iloc[0:2]}\n")

# 조건 선택
print(f"age > 28:\n{df[df['age'] > 28]}\n")
print(f"Seoul 거주:\n{df[df['city'] == 'Seoul']}\n")

# 여러 조건
condition = (df['age'] > 25) & (df['city'] == 'Seoul')
print(f"age>25 AND Seoul:\n{df[condition]}\n")


# =============================================================================
# 5. 데이터 수정
# =============================================================================

print("=== 데이터 수정 ===")

# 열 추가
df['bonus'] = df['salary'] * 0.1
print(f"bonus 열 추가:\n{df}\n")

# 열 이름 변경
df_renamed = df.rename(columns={'name': 'employee_name'})
print(f"컬럼 이름 변경:\n{df_renamed.columns.tolist()}\n")

# 값 변경
df.loc[df['name'] == 'Alice', 'salary'] = 55000
print(f"Alice 급여 변경:\n{df}\n")

# 열 삭제
df_dropped = df.drop(columns=['bonus'])
print(f"bonus 열 삭제:\n{df_dropped}\n")


# =============================================================================
# 6. 결측치 처리
# =============================================================================

print("=== 결측치 처리 ===")

# 결측치가 있는 데이터
df_null = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [9, 10, 11, 12]
})
print(f"결측치 데이터:\n{df_null}\n")

# 결측치 확인
print(f"결측치 개수:\n{df_null.isnull().sum()}\n")

# 결측치 제거
print(f"결측치 행 제거:\n{df_null.dropna()}\n")

# 결측치 채우기
print(f"0으로 채우기:\n{df_null.fillna(0)}\n")
print(f"평균으로 채우기:\n{df_null.fillna(df_null.mean())}\n")

# 앞/뒤 값으로 채우기
print(f"앞 값으로 채우기 (ffill):\n{df_null.ffill()}\n")


# =============================================================================
# 7. 그룹화 (GroupBy)
# =============================================================================

print("=== 그룹화 ===")

df = pd.DataFrame({
    'department': ['IT', 'HR', 'IT', 'HR', 'IT'],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'salary': [50000, 45000, 60000, 48000, 55000]
})
print(f"원본:\n{df}\n")

# 그룹별 통계
print(f"부서별 평균 급여:\n{df.groupby('department')['salary'].mean()}\n")

# 여러 집계 함수
agg_result = df.groupby('department').agg({
    'salary': ['mean', 'sum', 'count'],
    'name': 'count'
})
print(f"여러 집계:\n{agg_result}\n")

# 그룹별 변환
df['salary_rank'] = df.groupby('department')['salary'].rank(ascending=False)
print(f"부서별 급여 순위:\n{df}\n")


# =============================================================================
# 8. 정렬
# =============================================================================

print("=== 정렬 ===")

# 값 기준 정렬
print(f"급여 오름차순:\n{df.sort_values('salary')}\n")
print(f"급여 내림차순:\n{df.sort_values('salary', ascending=False)}\n")

# 여러 열 기준
print(f"부서, 급여 순:\n{df.sort_values(['department', 'salary'])}\n")

# 인덱스 정렬
print(f"인덱스 정렬:\n{df.sort_index()}\n")


# =============================================================================
# 9. 데이터 합치기 (Merge/Join)
# =============================================================================

print("=== 데이터 합치기 ===")

# 예제 데이터
employees = pd.DataFrame({
    'emp_id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'David']
})

departments = pd.DataFrame({
    'emp_id': [1, 2, 3, 5],
    'dept': ['IT', 'HR', 'IT', 'Sales']
})

print(f"employees:\n{employees}\n")
print(f"departments:\n{departments}\n")

# Inner Join (교집합)
inner = pd.merge(employees, departments, on='emp_id', how='inner')
print(f"Inner Join:\n{inner}\n")

# Left Join
left = pd.merge(employees, departments, on='emp_id', how='left')
print(f"Left Join:\n{left}\n")

# Outer Join (합집합)
outer = pd.merge(employees, departments, on='emp_id', how='outer')
print(f"Outer Join:\n{outer}\n")

# concat (행 결합)
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
concatenated = pd.concat([df1, df2], ignore_index=True)
print(f"Concat:\n{concatenated}\n")


# =============================================================================
# 10. 피벗 테이블
# =============================================================================

print("=== 피벗 테이블 ===")

sales = pd.DataFrame({
    'date': ['2024-01', '2024-01', '2024-02', '2024-02'],
    'product': ['A', 'B', 'A', 'B'],
    'region': ['East', 'East', 'West', 'West'],
    'amount': [100, 150, 120, 180]
})
print(f"원본:\n{sales}\n")

# 피벗 테이블
pivot = pd.pivot_table(
    sales,
    values='amount',
    index='date',
    columns='product',
    aggfunc='sum'
)
print(f"피벗 테이블:\n{pivot}\n")


# =============================================================================
# 11. 날짜/시간 처리
# =============================================================================

print("=== 날짜/시간 ===")

# 날짜 파싱
dates = pd.to_datetime(['2024-01-01', '2024-02-15', '2024-03-30'])
print(f"날짜: {dates}\n")

# 날짜 인덱스
df_dates = pd.DataFrame({
    'value': [10, 20, 30]
}, index=pd.date_range('2024-01-01', periods=3, freq='D'))
print(f"날짜 인덱스:\n{df_dates}\n")

# 날짜 컴포넌트 추출
df_dt = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=5, freq='D')
})
df_dt['year'] = df_dt['date'].dt.year
df_dt['month'] = df_dt['date'].dt.month
df_dt['day'] = df_dt['date'].dt.day
df_dt['dayofweek'] = df_dt['date'].dt.dayofweek
print(f"날짜 분해:\n{df_dt}\n")


# =============================================================================
# 12. 실용 예제
# =============================================================================

print("=== 실용 예제 ===")

# 예제: 판매 데이터 분석
np.random.seed(42)
sales_data = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=100, freq='D'),
    'product': np.random.choice(['A', 'B', 'C'], 100),
    'region': np.random.choice(['North', 'South', 'East', 'West'], 100),
    'quantity': np.random.randint(1, 50, 100),
    'price': np.random.uniform(10, 100, 100).round(2)
})
sales_data['revenue'] = sales_data['quantity'] * sales_data['price']

print(f"판매 데이터:\n{sales_data.head()}\n")

# 분석
print(f"총 매출: ${sales_data['revenue'].sum():,.2f}")
print(f"평균 매출: ${sales_data['revenue'].mean():,.2f}")

print(f"\n제품별 매출:\n{sales_data.groupby('product')['revenue'].sum().round(2)}")
print(f"\n지역별 판매량:\n{sales_data.groupby('region')['quantity'].sum()}")


# =============================================================================
# 정리: Pandas 핵심 기능
# =============================================================================

"""
Pandas 핵심:

1. 데이터 구조
   - Series: 1차원
   - DataFrame: 2차원 (표 형태)

2. 데이터 I/O
   - read_csv(), read_excel(), read_json()
   - to_csv(), to_excel(), to_json()

3. 데이터 선택
   - df['col'], df[['col1', 'col2']]
   - df.loc[], df.iloc[]
   - 조건 선택: df[df['col'] > value]

4. 데이터 처리
   - 결측치: dropna(), fillna()
   - 그룹화: groupby()
   - 정렬: sort_values()
   - 합치기: merge(), concat()

5. 통계
   - describe(), mean(), sum()
   - pivot_table()

PHP에 없는 기능:
- SQL 같은 데이터 조작
- 벡터화 연산
- 시계열 처리
- 피벗 테이블
"""
