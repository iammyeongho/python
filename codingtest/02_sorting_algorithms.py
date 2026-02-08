"""
정렬 알고리즘
=====================================
코딩 테스트에서 자주 나오는 정렬 알고리즘들을 알아봅니다.
"""

from typing import List
import random

# =============================================================================
# 1. 버블 정렬 (Bubble Sort)
# =============================================================================
# 시간 복잡도: O(n²), 공간 복잡도: O(1)
# 특징: 인접한 두 원소를 비교하여 교환

def bubble_sort(arr: List[int]) -> List[int]:
    """버블 정렬"""
    n = len(arr)
    arr = arr.copy()  # 원본 보존

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # 교환이 없으면 이미 정렬됨
        if not swapped:
            break

    return arr

print("=== 버블 정렬 ===")
test_arr = [64, 34, 25, 12, 22, 11, 90]
print(f"원본: {test_arr}")
print(f"정렬: {bubble_sort(test_arr)}")


# =============================================================================
# 2. 선택 정렬 (Selection Sort)
# =============================================================================
# 시간 복잡도: O(n²), 공간 복잡도: O(1)
# 특징: 최솟값을 찾아 맨 앞과 교환

def selection_sort(arr: List[int]) -> List[int]:
    """선택 정렬"""
    n = len(arr)
    arr = arr.copy()

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

print("\n=== 선택 정렬 ===")
print(f"정렬: {selection_sort(test_arr)}")


# =============================================================================
# 3. 삽입 정렬 (Insertion Sort)
# =============================================================================
# 시간 복잡도: O(n²), 공간 복잡도: O(1)
# 특징: 정렬된 부분에 새 원소를 삽입

def insertion_sort(arr: List[int]) -> List[int]:
    """삽입 정렬"""
    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # key보다 큰 원소들을 오른쪽으로 이동
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

print("\n=== 삽입 정렬 ===")
print(f"정렬: {insertion_sort(test_arr)}")


# =============================================================================
# 4. 병합 정렬 (Merge Sort) ⭐ 중요
# =============================================================================
# 시간 복잡도: O(n log n), 공간 복잡도: O(n)
# 특징: 분할 정복, 안정 정렬

def merge_sort(arr: List[int]) -> List[int]:
    """병합 정렬"""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """두 정렬된 리스트 병합"""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남은 원소 추가
    result.extend(left[i:])
    result.extend(right[j:])

    return result

print("\n=== 병합 정렬 ===")
print(f"정렬: {merge_sort(test_arr)}")


# =============================================================================
# 5. 퀵 정렬 (Quick Sort) ⭐ 중요
# =============================================================================
# 시간 복잡도: 평균 O(n log n), 최악 O(n²)
# 공간 복잡도: O(log n)
# 특징: 분할 정복, 피벗 기준 분할

def quick_sort(arr: List[int]) -> List[int]:
    """퀵 정렬"""
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # 중간값을 피벗으로
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# In-place 퀵 정렬 (메모리 효율적)
def quick_sort_inplace(arr: List[int], low: int = 0, high: int = None) -> List[int]:
    """In-place 퀵 정렬"""
    if high is None:
        arr = arr.copy()
        high = len(arr) - 1

    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort_inplace(arr, low, pivot_idx - 1)
        quick_sort_inplace(arr, pivot_idx + 1, high)

    return arr


def partition(arr: List[int], low: int, high: int) -> int:
    """파티션 함수"""
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

print("\n=== 퀵 정렬 ===")
print(f"정렬: {quick_sort(test_arr)}")


# =============================================================================
# 6. 힙 정렬 (Heap Sort)
# =============================================================================
# 시간 복잡도: O(n log n), 공간 복잡도: O(1)
# 특징: 힙 자료구조 활용

def heap_sort(arr: List[int]) -> List[int]:
    """힙 정렬"""
    import heapq

    arr = arr.copy()
    heapq.heapify(arr)  # O(n)
    return [heapq.heappop(arr) for _ in range(len(arr))]

print("\n=== 힙 정렬 ===")
print(f"정렬: {heap_sort(test_arr)}")


# =============================================================================
# 7. 계수 정렬 (Counting Sort)
# =============================================================================
# 시간 복잡도: O(n + k), 공간 복잡도: O(k)
# 특징: 정수에만 사용 가능, 범위가 작을 때 효율적

def counting_sort(arr: List[int]) -> List[int]:
    """계수 정렬"""
    if not arr:
        return arr

    min_val, max_val = min(arr), max(arr)
    range_size = max_val - min_val + 1

    # 카운트 배열
    count = [0] * range_size
    for num in arr:
        count[num - min_val] += 1

    # 결과 생성
    result = []
    for i, c in enumerate(count):
        result.extend([i + min_val] * c)

    return result

print("\n=== 계수 정렬 ===")
print(f"정렬: {counting_sort(test_arr)}")


# =============================================================================
# 8. Python 내장 정렬 ⭐ 실전에서 사용
# =============================================================================

print("\n=== Python 내장 정렬 ===")

# sorted(): 새 리스트 반환
arr = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_arr = sorted(arr)
print(f"sorted(): {sorted_arr}")

# sort(): 원본 수정
arr_copy = arr.copy()
arr_copy.sort()
print(f"sort(): {arr_copy}")

# 역순 정렬
print(f"역순: {sorted(arr, reverse=True)}")

# 키 함수 사용
words = ["apple", "pie", "banana", "cherry"]
print(f"길이순: {sorted(words, key=len)}")
print(f"알파벳순: {sorted(words)}")

# 복잡한 정렬 (튜플)
students = [
    ("Alice", 85, 22),
    ("Bob", 90, 20),
    ("Charlie", 85, 21),
]

# 점수 내림차순, 같으면 나이 오름차순
sorted_students = sorted(students, key=lambda x: (-x[1], x[2]))
print(f"\n학생 정렬: {sorted_students}")

# itemgetter 사용 (더 빠름)
from operator import itemgetter
sorted_by_name = sorted(students, key=itemgetter(0))
print(f"이름순: {sorted_by_name}")


# =============================================================================
# 9. 실전 문제 예제
# =============================================================================

# 문제 1: K번째 수 찾기
def find_kth_number(array: List[int], commands: List[List[int]]) -> List[int]:
    """
    프로그래머스 K번째 수
    배열을 i~j까지 자르고 정렬했을 때 k번째 수 찾기
    """
    result = []
    for i, j, k in commands:
        sliced = sorted(array[i-1:j])
        result.append(sliced[k-1])
    return result

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(f"\nK번째 수: {find_kth_number(array, commands)}")  # [5, 6, 3]


# 문제 2: 가장 큰 수 만들기
def largest_number(numbers: List[int]) -> str:
    """
    프로그래머스 가장 큰 수
    숫자를 조합하여 가장 큰 수 만들기
    """
    # 문자열로 변환 후 비교
    str_nums = list(map(str, numbers))
    # 두 수를 이어 붙여서 비교
    str_nums.sort(key=lambda x: x * 3, reverse=True)

    result = ''.join(str_nums)
    # 0으로만 이루어진 경우
    return '0' if result[0] == '0' else result

print(f"가장 큰 수: {largest_number([6, 10, 2])}")    # "6210"
print(f"가장 큰 수: {largest_number([3, 30, 34, 5, 9])}")  # "9534330"


# 문제 3: H-Index
def h_index(citations: List[int]) -> int:
    """
    프로그래머스 H-Index
    h번 이상 인용된 논문이 h편 이상일 때 h의 최댓값
    """
    citations.sort(reverse=True)

    for i, citation in enumerate(citations):
        if citation < i + 1:
            return i
    return len(citations)

print(f"H-Index: {h_index([3, 0, 6, 1, 5])}")  # 3


# =============================================================================
# 정리: 정렬 알고리즘 선택 가이드
# =============================================================================

"""
정렬 알고리즘 선택 가이드:

1. 실전에서는 Python 내장 sorted() / sort() 사용
   - Timsort 알고리즘 (병합 + 삽입 정렬)
   - 평균 O(n log n), 안정 정렬

2. 알고리즘 선택 기준:
   - 작은 배열 (n < 20): 삽입 정렬
   - 거의 정렬된 배열: 삽입 정렬
   - 정수 범위 작음: 계수 정렬
   - 안정 정렬 필요: 병합 정렬
   - 메모리 제한: 힙 정렬, 퀵 정렬

3. 면접용 필수 암기:
   - 퀵 정렬: O(n log n), 분할 정복
   - 병합 정렬: O(n log n), 안정 정렬
   - 힙 정렬: O(n log n), 제자리 정렬

시간 복잡도 비교:
| 알고리즘    | 평균      | 최악      | 공간   | 안정 |
|------------|----------|----------|--------|------|
| 버블 정렬   | O(n²)    | O(n²)    | O(1)   | O    |
| 선택 정렬   | O(n²)    | O(n²)    | O(1)   | X    |
| 삽입 정렬   | O(n²)    | O(n²)    | O(1)   | O    |
| 병합 정렬   | O(n log n)| O(n log n)| O(n)  | O    |
| 퀵 정렬     | O(n log n)| O(n²)    | O(log n)| X   |
| 힙 정렬     | O(n log n)| O(n log n)| O(1)  | X    |
| 계수 정렬   | O(n + k) | O(n + k) | O(k)   | O    |
"""
