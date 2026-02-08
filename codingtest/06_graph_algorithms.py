"""
그래프 알고리즘
=====================================
코딩 테스트에서 자주 나오는 그래프 알고리즘들
"""

from typing import List, Dict, Tuple
from collections import defaultdict, deque
import heapq

# =============================================================================
# 1. 그래프 표현 방법
# =============================================================================

print("=== 그래프 표현 ===")

# 방법 1: 인접 리스트 (Adjacency List) - 가장 많이 사용
adj_list = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}
print(f"인접 리스트: {adj_list}")

# defaultdict 활용
graph = defaultdict(list)
edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)  # 무방향 그래프
print(f"defaultdict: {dict(graph)}")

# 방법 2: 인접 행렬 (Adjacency Matrix)
n = 4
adj_matrix = [[0] * n for _ in range(n)]
for u, v in edges:
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1
print(f"인접 행렬:\n{adj_matrix}")

# 방법 3: 간선 리스트 (Edge List)
edge_list = [(0, 1, 5), (0, 2, 3), (1, 3, 2), (2, 3, 1)]  # (시작, 끝, 가중치)
print(f"간선 리스트: {edge_list}")


# =============================================================================
# 2. 최단 경로 - 다익스트라 (Dijkstra) ⭐
# =============================================================================

print("\n=== 다익스트라 알고리즘 ===")

def dijkstra(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Dict[int, int]:
    """
    다익스트라 알고리즘 (음수 가중치 없을 때)
    O((V + E) log V)
    """
    # 거리 테이블 초기화
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # 우선순위 큐: (거리, 노드)
    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        # 이미 처리된 노드면 스킵
        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


# 가중치 그래프
weighted_graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}

distances = dijkstra(weighted_graph, 0)
print(f"노드 0에서의 최단 거리: {distances}")


# 경로 추적 버전
def dijkstra_with_path(graph: Dict, start: int, end: int) -> Tuple[int, List[int]]:
    """최단 경로와 함께 경로 추적"""
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}

    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_node == end:
            break

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    # 경로 재구성
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()

    return distances[end], path


dist, path = dijkstra_with_path(weighted_graph, 0, 3)
print(f"0 -> 3 최단 거리: {dist}, 경로: {path}")


# =============================================================================
# 3. 최단 경로 - 벨만-포드 (Bellman-Ford)
# =============================================================================

print("\n=== 벨만-포드 알고리즘 ===")

def bellman_ford(n: int, edges: List[Tuple[int, int, int]], start: int) -> Dict[int, int]:
    """
    벨만-포드 알고리즘 (음수 가중치 가능)
    O(V * E)
    """
    distances = {i: float('inf') for i in range(n)}
    distances[start] = 0

    # V-1번 반복
    for _ in range(n - 1):
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # 음수 사이클 검사
    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            raise ValueError("음수 사이클 존재")

    return distances


edges = [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1), (2, 3, 5)]
print(f"벨만-포드 결과: {bellman_ford(4, edges, 0)}")


# =============================================================================
# 4. 최단 경로 - 플로이드-워셜 (Floyd-Warshall)
# =============================================================================

print("\n=== 플로이드-워셜 알고리즘 ===")

def floyd_warshall(n: int, edges: List[Tuple[int, int, int]]) -> List[List[int]]:
    """
    플로이드-워셜 알고리즘 (모든 쌍 최단 경로)
    O(V³)
    """
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]

    # 자기 자신까지 거리는 0
    for i in range(n):
        dist[i][i] = 0

    # 간선 정보 입력
    for u, v, weight in edges:
        dist[u][v] = weight

    # k를 경유점으로
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


edges = [(0, 1, 4), (0, 2, 1), (1, 2, 2), (2, 3, 3)]
all_pairs = floyd_warshall(4, edges)
print("모든 쌍 최단 거리:")
for row in all_pairs:
    print([x if x != float('inf') else '∞' for x in row])


# =============================================================================
# 5. 최소 신장 트리 - 크루스칼 (Kruskal)
# =============================================================================

print("\n=== 크루스칼 알고리즘 ===")

class UnionFind:
    """Union-Find (Disjoint Set Union)"""

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 경로 압축
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x, root_y = self.find(x), self.find(y)

        if root_x == root_y:
            return False  # 이미 같은 집합

        # 랭크 기반 합치기
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x

        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        return True


def kruskal(n: int, edges: List[Tuple[int, int, int]]) -> Tuple[int, List]:
    """
    크루스칼 알고리즘 (최소 신장 트리)
    O(E log E)
    """
    # 가중치 기준 정렬
    edges.sort(key=lambda x: x[2])

    uf = UnionFind(n)
    mst = []
    total_weight = 0

    for u, v, weight in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

            if len(mst) == n - 1:
                break

    return total_weight, mst


edges = [(0, 1, 4), (0, 2, 1), (1, 2, 2), (1, 3, 5), (2, 3, 3)]
weight, mst = kruskal(4, edges)
print(f"MST 가중치 합: {weight}")
print(f"MST 간선: {mst}")


# =============================================================================
# 6. 최소 신장 트리 - 프림 (Prim)
# =============================================================================

print("\n=== 프림 알고리즘 ===")

def prim(graph: Dict[int, List[Tuple[int, int]]], start: int = 0) -> Tuple[int, List]:
    """
    프림 알고리즘 (최소 신장 트리)
    O((V + E) log V)
    """
    visited = set()
    mst = []
    total_weight = 0

    # (가중치, 현재 노드, 이전 노드)
    pq = [(0, start, -1)]

    while pq and len(visited) < len(graph):
        weight, node, prev = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        if prev != -1:
            mst.append((prev, node, weight))
            total_weight += weight

        for neighbor, edge_weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, neighbor, node))

    return total_weight, mst


prim_graph = {
    0: [(1, 4), (2, 1)],
    1: [(0, 4), (2, 2), (3, 5)],
    2: [(0, 1), (1, 2), (3, 3)],
    3: [(1, 5), (2, 3)]
}
weight, mst = prim(prim_graph)
print(f"프림 MST 가중치: {weight}")
print(f"프림 MST 간선: {mst}")


# =============================================================================
# 7. 위상 정렬 (Topological Sort)
# =============================================================================

print("\n=== 위상 정렬 ===")

def topological_sort_kahn(graph: Dict[int, List[int]], n: int) -> List[int]:
    """
    카안 알고리즘 (BFS 기반 위상 정렬)
    진입 차수가 0인 노드부터 처리
    """
    in_degree = [0] * n
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque([i for i in range(n) if in_degree[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != n:
        return []  # 사이클 존재

    return result


def topological_sort_dfs(graph: Dict[int, List[int]], n: int) -> List[int]:
    """DFS 기반 위상 정렬"""
    visited = [False] * n
    result = []

    def dfs(node: int):
        visited[node] = True
        for neighbor in graph.get(node, []):
            if not visited[neighbor]:
                dfs(neighbor)
        result.append(node)

    for i in range(n):
        if not visited[i]:
            dfs(i)

    return result[::-1]


# DAG (방향 비순환 그래프)
dag = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: [4],
    4: []
}

print(f"위상 정렬 (Kahn): {topological_sort_kahn(dag, 5)}")
print(f"위상 정렬 (DFS): {topological_sort_dfs(dag, 5)}")


# =============================================================================
# 8. 사이클 탐지
# =============================================================================

print("\n=== 사이클 탐지 ===")

def has_cycle_undirected(graph: Dict[int, List[int]], n: int) -> bool:
    """무방향 그래프 사이클 탐지 (Union-Find)"""
    uf = UnionFind(n)

    for node in graph:
        for neighbor in graph[node]:
            if node < neighbor:  # 중복 방지
                if uf.find(node) == uf.find(neighbor):
                    return True
                uf.union(node, neighbor)

    return False


def has_cycle_directed(graph: Dict[int, List[int]], n: int) -> bool:
    """방향 그래프 사이클 탐지 (DFS)"""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n

    def dfs(node: int) -> bool:
        color[node] = GRAY

        for neighbor in graph.get(node, []):
            if color[neighbor] == GRAY:  # 현재 경로에서 다시 방문
                return True
            if color[neighbor] == WHITE and dfs(neighbor):
                return True

        color[node] = BLACK
        return False

    for i in range(n):
        if color[i] == WHITE:
            if dfs(i):
                return True

    return False


cycle_graph = {0: [1], 1: [2], 2: [0]}
print(f"사이클 존재 (방향): {has_cycle_directed(cycle_graph, 3)}")


# =============================================================================
# 9. 실전 문제 예제
# =============================================================================

print("\n=== 실전 문제 ===")

# 문제 1: 네트워크 (연결 요소 개수)
def count_networks(n: int, computers: List[List[int]]) -> int:
    """
    프로그래머스 네트워크
    연결된 컴퓨터 네트워크 개수
    """
    visited = [False] * n

    def dfs(node: int):
        visited[node] = True
        for i in range(n):
            if computers[node][i] == 1 and not visited[i]:
                dfs(i)

    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1

    return count


computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(f"네트워크 수: {count_networks(3, computers)}")  # 2


# 문제 2: 가장 먼 노드
def farthest_node(n: int, edges: List[List[int]]) -> int:
    """
    프로그래머스 가장 먼 노드
    1번 노드에서 가장 먼 노드 개수
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    distances = [-1] * (n + 1)
    distances[1] = 0

    queue = deque([1])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)

    max_dist = max(distances[1:])
    return distances[1:].count(max_dist)


edges = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(f"가장 먼 노드 수: {farthest_node(6, edges)}")  # 3


# 문제 3: 순위 (플로이드-워셜 응용)
def ranking(n: int, results: List[List[int]]) -> int:
    """
    프로그래머스 순위
    정확한 순위를 알 수 있는 선수 수
    """
    INF = float('inf')
    dist = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dist[i][i] = 0

    for winner, loser in results:
        dist[winner][loser] = 1

    # 플로이드-워셜
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # 각 선수별로 연결된 선수 수 확인
    count = 0
    for i in range(1, n + 1):
        known = 0
        for j in range(1, n + 1):
            if i != j and (dist[i][j] != INF or dist[j][i] != INF):
                known += 1
        if known == n - 1:
            count += 1

    return count


results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(f"순위 확정 선수: {ranking(5, results)}")  # 2


# =============================================================================
# 정리: 그래프 알고리즘 선택 가이드
# =============================================================================

"""
그래프 알고리즘 선택 가이드:

1. 최단 경로:
   - 가중치 없음: BFS
   - 양수 가중치: 다익스트라 O((V+E)logV)
   - 음수 가중치: 벨만-포드 O(VE)
   - 모든 쌍: 플로이드-워셜 O(V³)

2. 최소 신장 트리:
   - 간선 기준: 크루스칼 O(ElogE)
   - 정점 기준: 프림 O((V+E)logV)

3. 위상 정렬:
   - BFS (카안): 진입차수 활용
   - DFS: 역순으로 추가

4. 사이클 탐지:
   - 무방향: Union-Find
   - 방향: DFS (색칠법)

5. 연결 요소:
   - DFS/BFS 또는 Union-Find

핵심 자료구조:
- 인접 리스트: defaultdict(list)
- 우선순위 큐: heapq
- 집합 관리: Union-Find
"""
