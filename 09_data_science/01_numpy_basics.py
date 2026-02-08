"""
NumPy 기초
=====================================
수치 계산과 배열 처리를 위한 NumPy 라이브러리
pip install numpy
"""

import numpy as np

# =============================================================================
# 1. NumPy 배열 생성
# =============================================================================

print("=== NumPy 배열 생성 ===")

# 리스트에서 배열 생성
arr1 = np.array([1, 2, 3, 4, 5])
print(f"1D 배열: {arr1}")
print(f"타입: {arr1.dtype}")

# 2차원 배열
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n2D 배열:\n{arr2}")
print(f"형태: {arr2.shape}")  # (2, 3)

# 다양한 생성 방법
zeros = np.zeros((3, 4))       # 0으로 채운 배열
ones = np.ones((2, 3))         # 1로 채운 배열
full = np.full((2, 2), 7)      # 특정 값으로 채움
eye = np.eye(3)                # 단위 행렬
empty = np.empty((2, 2))       # 초기화되지 않은 배열

print(f"\nzeros(3,4):\n{zeros}")
print(f"\nones(2,3):\n{ones}")
print(f"\neye(3):\n{eye}")


# 범위로 생성
range_arr = np.arange(0, 10, 2)      # [0, 2, 4, 6, 8]
linspace = np.linspace(0, 1, 5)       # [0, 0.25, 0.5, 0.75, 1]
print(f"\narange(0,10,2): {range_arr}")
print(f"linspace(0,1,5): {linspace}")

# 랜덤 배열
random_arr = np.random.rand(3, 3)     # 0~1 균등분포
normal_arr = np.random.randn(3, 3)    # 표준정규분포
randint = np.random.randint(0, 10, (3, 3))  # 정수 랜덤
print(f"\nrandom(3,3):\n{random_arr}")


# =============================================================================
# 2. 배열 속성
# =============================================================================

print("\n=== 배열 속성 ===")

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(f"배열:\n{arr}")
print(f"차원 수 (ndim): {arr.ndim}")      # 2
print(f"형태 (shape): {arr.shape}")        # (2, 3)
print(f"전체 요소 수 (size): {arr.size}")  # 6
print(f"데이터 타입 (dtype): {arr.dtype}") # int64
print(f"요소 크기 (itemsize): {arr.itemsize} bytes")


# =============================================================================
# 3. 인덱싱과 슬라이싱
# =============================================================================

print("\n=== 인덱싱과 슬라이싱 ===")

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

print(f"원본:\n{arr}")

# 기본 인덱싱
print(f"\narr[0, 0] = {arr[0, 0]}")  # 1
print(f"arr[1, 2] = {arr[1, 2]}")    # 7
print(f"arr[-1, -1] = {arr[-1, -1]}")  # 12

# 슬라이싱
print(f"\narr[0:2, 1:3]:\n{arr[0:2, 1:3]}")  # [[2,3], [6,7]]
print(f"arr[:, 0] = {arr[:, 0]}")    # 첫 번째 열
print(f"arr[1, :] = {arr[1, :]}")    # 두 번째 행

# 조건 인덱싱 (Boolean indexing)
print(f"\narr > 5: {arr[arr > 5]}")  # 5보다 큰 요소들

# Fancy indexing
indices = [0, 2]
print(f"arr[[0, 2], :] (행 0, 2):\n{arr[indices, :]}")


# =============================================================================
# 4. 배열 연산
# =============================================================================

print("\n=== 배열 연산 ===")

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# 요소별 연산 (element-wise)
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a ** 2 = {a ** 2}")

# 브로드캐스팅
c = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\nc + 10:\n{c + 10}")
print(f"\nc * 2:\n{c * 2}")

# 수학 함수
print(f"\nnp.sqrt(a) = {np.sqrt(a)}")
print(f"np.exp(a) = {np.exp(a)}")
print(f"np.sin(a) = {np.sin(a)}")
print(f"np.log(a) = {np.log(a)}")


# =============================================================================
# 5. 통계 함수
# =============================================================================

print("\n=== 통계 함수 ===")

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(f"배열:\n{arr}")
print(f"\n합계: {np.sum(arr)}")
print(f"평균: {np.mean(arr)}")
print(f"표준편차: {np.std(arr):.4f}")
print(f"분산: {np.var(arr):.4f}")
print(f"최솟값: {np.min(arr)}")
print(f"최댓값: {np.max(arr)}")

# 축(axis)별 연산
print(f"\n행별 합계 (axis=1): {np.sum(arr, axis=1)}")
print(f"열별 합계 (axis=0): {np.sum(arr, axis=0)}")
print(f"행별 평균 (axis=1): {np.mean(arr, axis=1)}")

# 위치 찾기
print(f"\n최댓값 인덱스: {np.argmax(arr)}")
print(f"최솟값 인덱스: {np.argmin(arr)}")


# =============================================================================
# 6. 배열 형태 변환
# =============================================================================

print("\n=== 배열 형태 변환 ===")

arr = np.arange(12)
print(f"원본: {arr}")

# reshape
reshaped = arr.reshape(3, 4)
print(f"\nreshape(3,4):\n{reshaped}")

reshaped2 = arr.reshape(2, 2, 3)
print(f"\nreshape(2,2,3):\n{reshaped2}")

# flatten (평탄화)
print(f"\nflatten: {reshaped.flatten()}")

# transpose (전치)
print(f"\ntranspose:\n{reshaped.T}")

# 차원 추가/제거
arr1d = np.array([1, 2, 3])
print(f"\nnewaxis: {arr1d[np.newaxis, :].shape}")  # (1, 3)
print(f"expand_dims: {np.expand_dims(arr1d, axis=0).shape}")  # (1, 3)


# =============================================================================
# 7. 배열 결합과 분할
# =============================================================================

print("\n=== 배열 결합과 분할 ===")

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# 수직 결합 (vstack)
print(f"vstack:\n{np.vstack([a, b])}")

# 수평 결합 (hstack)
print(f"\nhstack:\n{np.hstack([a, b])}")

# concatenate
print(f"\nconcatenate axis=0:\n{np.concatenate([a, b], axis=0)}")
print(f"\nconcatenate axis=1:\n{np.concatenate([a, b], axis=1)}")

# 분할
arr = np.arange(16).reshape(4, 4)
print(f"\n원본:\n{arr}")

# 수직 분할
v1, v2 = np.vsplit(arr, 2)
print(f"\nvsplit[0]:\n{v1}")

# 수평 분할
h1, h2 = np.hsplit(arr, 2)
print(f"\nhsplit[0]:\n{h1}")


# =============================================================================
# 8. 선형대수
# =============================================================================

print("\n=== 선형대수 ===")

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# 행렬 곱
print(f"행렬 곱 (A @ B):\n{A @ B}")
print(f"행렬 곱 (np.dot):\n{np.dot(A, B)}")

# 전치 행렬
print(f"\n전치 (A.T):\n{A.T}")

# 역행렬
print(f"\n역행렬:\n{np.linalg.inv(A)}")

# 행렬식
print(f"\n행렬식: {np.linalg.det(A):.4f}")

# 고유값, 고유벡터
eigenvalues, eigenvectors = np.linalg.eig(A)
print(f"\n고유값: {eigenvalues}")


# =============================================================================
# 9. 브로드캐스팅 규칙
# =============================================================================

print("\n=== 브로드캐스팅 ===")

"""
브로드캐스팅 규칙:
1. 차원 수가 다르면 작은 쪽 앞에 1을 추가
2. 각 차원에서 크기가 1인 쪽이 다른 쪽에 맞춰짐
3. 크기가 다르고 1도 아니면 오류
"""

a = np.array([[1], [2], [3]])  # (3, 1)
b = np.array([10, 20, 30])      # (3,) -> (1, 3)

print(f"a (3,1):\n{a}")
print(f"b (3,):\n{b}")
print(f"\na + b (3,3):\n{a + b}")


# =============================================================================
# 10. 실용 예제
# =============================================================================

print("\n=== 실용 예제 ===")

# 예제 1: 정규화 (Normalization)
data = np.random.rand(5, 3) * 100
normalized = (data - data.min()) / (data.max() - data.min())
print(f"원본 데이터:\n{data.round(2)}")
print(f"\n정규화된 데이터:\n{normalized.round(4)}")

# 예제 2: 표준화 (Standardization)
standardized = (data - data.mean()) / data.std()
print(f"\n표준화된 데이터:\n{standardized.round(4)}")

# 예제 3: 원-핫 인코딩
labels = np.array([0, 1, 2, 1, 0])
one_hot = np.eye(3)[labels]
print(f"\n레이블: {labels}")
print(f"원-핫:\n{one_hot}")

# 예제 4: 이동 평균
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
window = 3
moving_avg = np.convolve(data, np.ones(window)/window, mode='valid')
print(f"\n원본: {data}")
print(f"이동 평균 (window=3): {moving_avg}")


# =============================================================================
# 정리: NumPy 핵심 기능
# =============================================================================

"""
NumPy 핵심:

1. 배열 생성
   - np.array(), np.zeros(), np.ones()
   - np.arange(), np.linspace()
   - np.random.rand(), np.random.randn()

2. 인덱싱
   - arr[i, j], arr[i:j, k:l]
   - arr[arr > 5] (조건 인덱싱)

3. 연산
   - 요소별 연산 (+, -, *, /)
   - 브로드캐스팅
   - np.sum(), np.mean(), np.std()

4. 형태 변환
   - reshape(), flatten()
   - T (전치)

5. 선형대수
   - @, np.dot() (행렬 곱)
   - np.linalg.inv(), np.linalg.det()

PHP에 없는 기능:
- 벡터화 연산 (매우 빠름)
- 브로드캐스팅
- 선형대수 연산
- 메모리 효율적인 대용량 데이터 처리
"""
