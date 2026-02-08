"""
코딩 테스트를 위한 자료구조 기초
=====================================
Python에서 자주 사용되는 자료구조들을 알아봅니다.
"""

# =============================================================================
# 1. 스택 (Stack) - LIFO (Last In First Out)
# =============================================================================

# Python에서는 리스트를 스택으로 사용
stack = []

# push: append()
stack.append(1)
stack.append(2)
stack.append(3)
print(f"스택: {stack}")  # [1, 2, 3]

# pop: pop()
top = stack.pop()
print(f"pop된 값: {top}")  # 3
print(f"스택: {stack}")    # [1, 2]

# peek: 마지막 요소 확인 (제거하지 않음)
if stack:
    print(f"top 값: {stack[-1]}")  # 2


# 스택 활용 예제: 괄호 유효성 검사
def is_valid_parentheses(s: str) -> bool:
    """
    괄호 문자열이 유효한지 검사
    예: "(())" -> True, "(()" -> False
    """
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0

print(f"\n괄호 검사 '(())': {is_valid_parentheses('(())')}")  # True
print(f"괄호 검사 '(()': {is_valid_parentheses('(()')}")      # False


# =============================================================================
# 2. 큐 (Queue) - FIFO (First In First Out)
# =============================================================================

from collections import deque

# deque를 사용한 큐 (리스트보다 효율적)
queue = deque()

# enqueue: append()
queue.append(1)
queue.append(2)
queue.append(3)
print(f"\n큐: {list(queue)}")  # [1, 2, 3]

# dequeue: popleft()
front = queue.popleft()
print(f"dequeue된 값: {front}")  # 1
print(f"큐: {list(queue)}")      # [2, 3]


# 큐 활용 예제: BFS (너비 우선 탐색)
def bfs(graph: dict, start: str) -> list:
    """
    그래프에서 BFS 수행
    """
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            # 인접 노드들을 큐에 추가
            queue.extend(graph.get(node, []))

    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
print(f"\nBFS 탐색 결과: {bfs(graph, 'A')}")  # ['A', 'B', 'C', 'D', 'E', 'F']


# =============================================================================
# 3. 힙 (Heap) - 우선순위 큐
# =============================================================================

import heapq

# 최소 힙 (기본)
min_heap = []
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 4)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 5)

print(f"\n최소 힙: {min_heap}")  # [1, 1, 4, 3, 5]

# 최솟값 추출
smallest = heapq.heappop(min_heap)
print(f"최솟값: {smallest}")  # 1

# 최대 힙 (음수로 변환)
max_heap = []
for num in [3, 1, 4, 1, 5]:
    heapq.heappush(max_heap, -num)

largest = -heapq.heappop(max_heap)
print(f"최댓값: {largest}")  # 5


# 힙 활용 예제: K번째 큰 수 찾기
def find_kth_largest(nums: list, k: int) -> int:
    """
    배열에서 K번째로 큰 수 찾기
    """
    # 최소 힙을 사용하여 k개 요소만 유지
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]

nums = [3, 2, 1, 5, 6, 4]
print(f"\n2번째로 큰 수: {find_kth_largest(nums, 2)}")  # 5


# =============================================================================
# 4. 해시맵 (HashMap) - 딕셔너리
# =============================================================================

# Python의 dict가 해시맵
hash_map = {}

# 삽입: O(1)
hash_map['apple'] = 3
hash_map['banana'] = 5
hash_map['orange'] = 2

# 조회: O(1)
print(f"\napple 개수: {hash_map['apple']}")  # 3

# 키 존재 확인: O(1)
print(f"'grape' 존재?: {'grape' in hash_map}")  # False

# defaultdict 활용
from collections import defaultdict

# 기본값 설정
count_map = defaultdict(int)  # 기본값 0
count_map['a'] += 1
count_map['b'] += 1
count_map['a'] += 1
print(f"카운트 맵: {dict(count_map)}")  # {'a': 2, 'b': 1}

# Counter 활용
from collections import Counter

text = "hello world"
char_count = Counter(text)
print(f"문자 빈도: {char_count}")
print(f"가장 흔한 2개: {char_count.most_common(2)}")  # [('l', 3), ('o', 2)]


# 해시맵 활용 예제: 두 수의 합
def two_sum(nums: list, target: int) -> list:
    """
    배열에서 합이 target이 되는 두 수의 인덱스 찾기
    """
    num_map = {}  # 값 -> 인덱스 매핑

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

    return []

nums = [2, 7, 11, 15]
print(f"\nTwo Sum 결과: {two_sum(nums, 9)}")  # [0, 1]


# =============================================================================
# 5. 집합 (Set)
# =============================================================================

# 중복 제거, O(1) 조회
my_set = {1, 2, 3, 3, 4}
print(f"\n집합: {my_set}")  # {1, 2, 3, 4}

# 집합 연산
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(f"합집합: {set_a | set_b}")       # {1, 2, 3, 4, 5, 6}
print(f"교집합: {set_a & set_b}")       # {3, 4}
print(f"차집합: {set_a - set_b}")       # {1, 2}
print(f"대칭차집합: {set_a ^ set_b}")   # {1, 2, 5, 6}


# 집합 활용 예제: 중복 문자 찾기
def find_duplicates(s: str) -> set:
    """
    문자열에서 중복되는 문자 찾기
    """
    seen = set()
    duplicates = set()

    for char in s:
        if char in seen:
            duplicates.add(char)
        seen.add(char)

    return duplicates

print(f"\n중복 문자: {find_duplicates('programming')}")  # {'r', 'g', 'm'}


# =============================================================================
# 6. 연결 리스트 (Linked List)
# =============================================================================

class ListNode:
    """단일 연결 리스트 노드"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(values: list) -> ListNode:
    """리스트로 연결 리스트 생성"""
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(head: ListNode) -> str:
    """연결 리스트 출력"""
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    return " -> ".join(values)


# 연결 리스트 활용 예제: 뒤집기
def reverse_linked_list(head: ListNode) -> ListNode:
    """연결 리스트 뒤집기"""
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

linked_list = create_linked_list([1, 2, 3, 4, 5])
print(f"\n원본 연결 리스트: {print_linked_list(linked_list)}")

reversed_list = reverse_linked_list(linked_list)
print(f"뒤집은 연결 리스트: {print_linked_list(reversed_list)}")


# =============================================================================
# 7. 트리 (Tree)
# =============================================================================

class TreeNode:
    """이진 트리 노드"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 트리 순회
def preorder(node: TreeNode) -> list:
    """전위 순회: 루트 -> 왼쪽 -> 오른쪽"""
    if not node:
        return []
    return [node.val] + preorder(node.left) + preorder(node.right)


def inorder(node: TreeNode) -> list:
    """중위 순회: 왼쪽 -> 루트 -> 오른쪽"""
    if not node:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)


def postorder(node: TreeNode) -> list:
    """후위 순회: 왼쪽 -> 오른쪽 -> 루트"""
    if not node:
        return []
    return postorder(node.left) + postorder(node.right) + [node.val]


# 트리 생성
#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(f"\n전위 순회: {preorder(root)}")   # [1, 2, 4, 5, 3]
print(f"중위 순회: {inorder(root)}")      # [4, 2, 5, 1, 3]
print(f"후위 순회: {postorder(root)}")    # [4, 5, 2, 3, 1]


# 트리 활용 예제: 최대 깊이
def max_depth(root: TreeNode) -> int:
    """이진 트리의 최대 깊이"""
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

print(f"트리 최대 깊이: {max_depth(root)}")  # 3


# =============================================================================
# 8. 그래프 (Graph)
# =============================================================================

# 인접 리스트로 그래프 표현
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}


# DFS (깊이 우선 탐색) - 재귀
def dfs_recursive(graph: dict, node: int, visited: set = None) -> list:
    """재귀적 DFS"""
    if visited is None:
        visited = set()

    visited.add(node)
    result = [node]

    for neighbor in graph[node]:
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))

    return result


# DFS - 스택
def dfs_iterative(graph: dict, start: int) -> list:
    """반복적 DFS (스택 사용)"""
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            # 역순으로 추가해야 왼쪽부터 탐색
            stack.extend(reversed(graph[node]))

    return visited


print(f"\nDFS (재귀): {dfs_recursive(graph, 0)}")
print(f"DFS (스택): {dfs_iterative(graph, 0)}")


# =============================================================================
# 정리: 자료구조별 시간 복잡도
# =============================================================================

"""
자료구조별 주요 연산 시간 복잡도:

| 자료구조    | 접근   | 탐색   | 삽입   | 삭제   |
|------------|--------|--------|--------|--------|
| 배열       | O(1)   | O(n)   | O(n)   | O(n)   |
| 스택       | O(n)   | O(n)   | O(1)   | O(1)   |
| 큐         | O(n)   | O(n)   | O(1)   | O(1)   |
| 해시맵     | -      | O(1)   | O(1)   | O(1)   |
| 힙         | -      | O(n)   | O(log n)| O(log n)|
| 연결리스트 | O(n)   | O(n)   | O(1)   | O(1)   |
| 이진트리   | O(log n)| O(log n)| O(log n)| O(log n)|
"""
