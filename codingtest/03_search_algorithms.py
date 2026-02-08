"""
탐색 알고리즘
=====================================
코딩 테스트에서 자주 나오는 탐색 알고리즘들을 알아봅니다.
"""

from typing import List, Optional
from collections import deque

# =============================================================================
# 1. 선형 탐색 (Linear Search)
# =============================================================================
# 시간 복잡도: O(n)

def linear_search(arr: List[int], target: int) -> int:
    """선형 탐색: 처음부터 끝까지 순차 탐색"""
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

print("=== 선형 탐색 ===")
arr = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"배열: {arr}")
print(f"5의 인덱스: {linear_search(arr, 5)}")  # 4


# =============================================================================
# 2. 이진 탐색 (Binary Search) ⭐ 매우 중요
# =============================================================================
# 시간 복잡도: O(log n)
# 조건: 배열이 정렬되어 있어야 함

def binary_search(arr: List[int], target: int) -> int:
    """이진 탐색 (반복)"""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_recursive(arr: List[int], target: int,
                            left: int = 0, right: int = None) -> int:
    """이진 탐색 (재귀)"""
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


print("\n=== 이진 탐색 ===")
sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"배열: {sorted_arr}")
print(f"5의 인덱스: {binary_search(sorted_arr, 5)}")  # 4
print(f"10의 인덱스: {binary_search(sorted_arr, 10)}")  # -1


# Python bisect 모듈 활용
import bisect

print("\n=== bisect 모듈 ===")
arr = [1, 2, 4, 4, 5, 6]

# bisect_left: target이 들어갈 왼쪽 위치
print(f"bisect_left(4): {bisect.bisect_left(arr, 4)}")   # 2

# bisect_right: target이 들어갈 오른쪽 위치
print(f"bisect_right(4): {bisect.bisect_right(arr, 4)}")  # 4

# insort: 정렬 유지하며 삽입
bisect.insort(arr, 3)
print(f"3 삽입 후: {arr}")  # [1, 2, 3, 4, 4, 5, 6]


# =============================================================================
# 3. 이진 탐색 변형 문제들 ⭐
# =============================================================================

# 하한선 찾기 (Lower Bound)
def lower_bound(arr: List[int], target: int) -> int:
    """target 이상인 첫 번째 위치"""
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


# 상한선 찾기 (Upper Bound)
def upper_bound(arr: List[int], target: int) -> int:
    """target 초과인 첫 번째 위치"""
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left


print("\n=== Lower/Upper Bound ===")
arr = [1, 2, 4, 4, 4, 5, 6]
print(f"배열: {arr}")
print(f"4의 lower_bound: {lower_bound(arr, 4)}")  # 2
print(f"4의 upper_bound: {upper_bound(arr, 4)}")  # 5
print(f"4의 개수: {upper_bound(arr, 4) - lower_bound(arr, 4)}")  # 3


# 회전 정렬 배열 탐색
def search_rotated(nums: List[int], target: int) -> int:
    """
    회전된 정렬 배열에서 target 찾기
    예: [4, 5, 6, 7, 0, 1, 2]에서 0 찾기
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # 왼쪽이 정렬되어 있음
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # 오른쪽이 정렬되어 있음
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


print("\n=== 회전 배열 탐색 ===")
rotated = [4, 5, 6, 7, 0, 1, 2]
print(f"배열: {rotated}")
print(f"0의 인덱스: {search_rotated(rotated, 0)}")  # 4
print(f"3의 인덱스: {search_rotated(rotated, 3)}")  # -1


# =============================================================================
# 4. DFS (깊이 우선 탐색) ⭐ 매우 중요
# =============================================================================

print("\n=== DFS (깊이 우선 탐색) ===")

# 재귀적 DFS
def dfs_recursive(graph: dict, node: int, visited: set = None) -> List[int]:
    """재귀적 DFS"""
    if visited is None:
        visited = set()

    visited.add(node)
    result = [node]

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))

    return result


# 스택을 이용한 DFS
def dfs_iterative(graph: dict, start: int) -> List[int]:
    """반복적 DFS (스택)"""
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            # 역순으로 추가 (순서 유지)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result


graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

print(f"그래프: {graph}")
print(f"DFS (재귀): {dfs_recursive(graph, 1)}")
print(f"DFS (스택): {dfs_iterative(graph, 1)}")


# 2D 그리드 DFS
def dfs_grid(grid: List[List[int]], row: int, col: int,
             visited: set = None) -> int:
    """2D 그리드 DFS - 연결된 1의 개수"""
    if visited is None:
        visited = set()

    rows, cols = len(grid), len(grid[0])

    # 범위 체크 및 방문 체크
    if (row < 0 or row >= rows or col < 0 or col >= cols or
        grid[row][col] == 0 or (row, col) in visited):
        return 0

    visited.add((row, col))
    count = 1

    # 상하좌우 탐색
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        count += dfs_grid(grid, row + dr, col + dc, visited)

    return count


# =============================================================================
# 5. BFS (너비 우선 탐색) ⭐ 매우 중요
# =============================================================================

print("\n=== BFS (너비 우선 탐색) ===")

def bfs(graph: dict, start: int) -> List[int]:
    """BFS (큐)"""
    visited = set([start])
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


print(f"BFS: {bfs(graph, 1)}")


# BFS로 최단 경로 찾기
def bfs_shortest_path(graph: dict, start: int, end: int) -> List[int]:
    """BFS로 최단 경로 찾기"""
    if start == end:
        return [start]

    visited = set([start])
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()

        for neighbor in graph.get(node, []):
            if neighbor == end:
                return path + [neighbor]

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return []


path_graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2, 6],
    6: [3, 5]
}

print(f"\n최단 경로 (1->6): {bfs_shortest_path(path_graph, 1, 6)}")


# 2D 그리드 BFS - 최단 거리
def bfs_grid(grid: List[List[int]], start: tuple, end: tuple) -> int:
    """2D 그리드에서 최단 거리 (0: 벽, 1: 통로)"""
    rows, cols = len(grid), len(grid[0])

    if grid[start[0]][start[1]] == 0 or grid[end[0]][end[1]] == 0:
        return -1

    visited = set([start])
    queue = deque([(start[0], start[1], 0)])  # row, col, distance

    while queue:
        row, col, dist = queue.popleft()

        if (row, col) == end:
            return dist

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc

            if (0 <= new_row < rows and 0 <= new_col < cols and
                grid[new_row][new_col] == 1 and
                (new_row, new_col) not in visited):

                visited.add((new_row, new_col))
                queue.append((new_row, new_col, dist + 1))

    return -1


print("\n=== 2D 그리드 BFS ===")
maze = [
    [1, 1, 0, 1],
    [1, 1, 1, 1],
    [0, 1, 0, 1],
    [1, 1, 1, 1]
]
print(f"최단 거리 (0,0) -> (3,3): {bfs_grid(maze, (0, 0), (3, 3))}")  # 6


# =============================================================================
# 6. 이진 탐색 응용 문제
# =============================================================================

print("\n=== 이진 탐색 응용 ===")

# 파라메트릭 서치: 조건을 만족하는 최솟값/최댓값 찾기
def can_finish(tasks: List[int], days: int, capacity: int) -> bool:
    """capacity로 days일 안에 모든 task 완료 가능?"""
    current_day = 1
    current_load = 0

    for task in tasks:
        if task > capacity:
            return False
        if current_load + task > capacity:
            current_day += 1
            current_load = task
        else:
            current_load += task

    return current_day <= days


def min_capacity(tasks: List[int], days: int) -> int:
    """주어진 일수 내에 완료하기 위한 최소 capacity"""
    left = max(tasks)
    right = sum(tasks)

    while left < right:
        mid = (left + right) // 2
        if can_finish(tasks, days, mid):
            right = mid
        else:
            left = mid + 1

    return left


tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"작업: {tasks}")
print(f"5일 내 최소 capacity: {min_capacity(tasks, 5)}")  # 15


# =============================================================================
# 7. 실전 문제 예제
# =============================================================================

print("\n=== 실전 문제 ===")

# 문제 1: 섬의 개수
def count_islands(grid: List[List[str]]) -> int:
    """
    LeetCode 200. Number of Islands
    1로 연결된 섬의 개수 세기
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'  # 방문 표시
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1

    return count


island_grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]
print(f"섬의 개수: {count_islands(island_grid)}")  # 3


# 문제 2: 타겟 넘버 (DFS)
def target_number(numbers: List[int], target: int) -> int:
    """
    프로그래머스 타겟 넘버
    +/- 조합으로 target을 만드는 경우의 수
    """
    count = 0

    def dfs(index: int, current_sum: int):
        nonlocal count

        if index == len(numbers):
            if current_sum == target:
                count += 1
            return

        dfs(index + 1, current_sum + numbers[index])
        dfs(index + 1, current_sum - numbers[index])

    dfs(0, 0)
    return count


print(f"타겟 넘버: {target_number([1, 1, 1, 1, 1], 3)}")  # 5


# 문제 3: 게임 맵 최단거리 (BFS)
def shortest_path_game(maps: List[List[int]]) -> int:
    """
    프로그래머스 게임 맵 최단거리
    (0,0)에서 (n-1,m-1)까지 최단 거리
    """
    if not maps:
        return -1

    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    queue = deque([(0, 0, 1)])  # row, col, distance
    visited[0][0] = True

    while queue:
        row, col, dist = queue.popleft()

        if row == n - 1 and col == m - 1:
            return dist

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc

            if (0 <= nr < n and 0 <= nc < m and
                maps[nr][nc] == 1 and not visited[nr][nc]):
                visited[nr][nc] = True
                queue.append((nr, nc, dist + 1))

    return -1


game_map = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1]
]
print(f"게임 맵 최단거리: {shortest_path_game(game_map)}")  # 11


# =============================================================================
# 정리: DFS vs BFS
# =============================================================================

"""
DFS vs BFS 선택 가이드:

DFS 사용:
- 모든 경로 탐색 필요할 때
- 경로의 특징을 저장해야 할 때
- 백트래킹 문제
- 그래프가 매우 깊고 해가 깊은 곳에 있을 때
- 재귀적 구조가 자연스러운 문제

BFS 사용:
- 최단 경로/최소 비용 찾기 ⭐
- 레벨별 탐색이 필요할 때
- 가까운 노드부터 탐색해야 할 때
- 그래프가 넓고 해가 얕은 곳에 있을 때

시간 복잡도:
- DFS: O(V + E) (정점 + 간선)
- BFS: O(V + E)
- 이진 탐색: O(log n)
"""
