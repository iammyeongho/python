"""
백트래킹 (Backtracking)
=====================================
모든 경우의 수를 탐색하되, 조건에 맞지 않으면 되돌아가는 기법
"""

from typing import List

# =============================================================================
# 1. 백트래킹 기본 개념
# =============================================================================

"""
백트래킹 vs 완전 탐색:
- 완전 탐색: 모든 경우의 수를 다 확인
- 백트래킹: 가망 없는 경로는 조기에 포기 (가지치기/Pruning)

백트래킹 패턴:
1. 현재 상태가 정답인지 확인
2. 모든 선택지에 대해:
   a. 선택
   b. 재귀 호출
   c. 선택 취소 (되돌리기)
"""


# =============================================================================
# 2. 순열 (Permutation)
# =============================================================================

print("=== 순열 ===")

def permutations(nums: List[int]) -> List[List[int]]:
    """
    LeetCode 46. Permutations
    모든 순열 생성
    """
    result = []

    def backtrack(path: List[int], remaining: List[int]):
        if not remaining:
            result.append(path[:])
            return

        for i in range(len(remaining)):
            # 선택
            path.append(remaining[i])
            # 재귀
            backtrack(path, remaining[:i] + remaining[i+1:])
            # 선택 취소
            path.pop()

    backtrack([], nums)
    return result


print(f"[1,2,3] 순열: {permutations([1, 2, 3])}")


# 중복이 있는 순열
def permutations_unique(nums: List[int]) -> List[List[int]]:
    """
    LeetCode 47. Permutations II
    중복 원소가 있는 순열
    """
    result = []
    nums.sort()  # 중복 처리를 위해 정렬
    used = [False] * len(nums)

    def backtrack(path: List[int]):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            # 이미 사용했거나, 이전과 같은데 이전을 안 썼으면 스킵
            if used[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue

            used[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i] = False

    backtrack([])
    return result


print(f"[1,1,2] 순열: {permutations_unique([1, 1, 2])}")


# =============================================================================
# 3. 조합 (Combination)
# =============================================================================

print("\n=== 조합 ===")

def combinations(n: int, k: int) -> List[List[int]]:
    """
    LeetCode 77. Combinations
    1~n에서 k개 선택하는 모든 조합
    """
    result = []

    def backtrack(start: int, path: List[int]):
        if len(path) == k:
            result.append(path[:])
            return

        # 가지치기: 남은 원소가 부족하면 스킵
        need = k - len(path)
        available = n - start + 1
        if available < need:
            return

        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(1, [])
    return result


print(f"C(4,2): {combinations(4, 2)}")


# 조합 합
def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    LeetCode 39. Combination Sum
    합이 target이 되는 조합 (중복 사용 가능)
    """
    result = []
    candidates.sort()

    def backtrack(start: int, path: List[int], remaining: int):
        if remaining == 0:
            result.append(path[:])
            return

        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break  # 가지치기

            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])  # i: 중복 사용 가능
            path.pop()

    backtrack(0, [], target)
    return result


print(f"합이 7인 조합: {combination_sum([2, 3, 6, 7], 7)}")


# =============================================================================
# 4. 부분집합 (Subset)
# =============================================================================

print("\n=== 부분집합 ===")

def subsets(nums: List[int]) -> List[List[int]]:
    """
    LeetCode 78. Subsets
    모든 부분집합 생성
    """
    result = []

    def backtrack(start: int, path: List[int]):
        result.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


print(f"[1,2,3] 부분집합: {subsets([1, 2, 3])}")


# 비트마스크로 부분집합
def subsets_bitmask(nums: List[int]) -> List[List[int]]:
    """비트마스크를 이용한 부분집합"""
    n = len(nums)
    result = []

    for mask in range(1 << n):  # 0 ~ 2^n - 1
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        result.append(subset)

    return result


print(f"비트마스크: {subsets_bitmask([1, 2, 3])}")


# =============================================================================
# 5. N-Queens 문제
# =============================================================================

print("\n=== N-Queens ===")

def solve_n_queens(n: int) -> List[List[str]]:
    """
    LeetCode 51. N-Queens
    n x n 체스판에 n개의 퀸 배치
    """
    result = []
    board = [['.'] * n for _ in range(n)]

    # 퀸이 놓인 열, 대각선 추적
    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col

    def backtrack(row: int):
        if row == n:
            result.append([''.join(r) for r in board])
            return

        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            # 선택
            board[row][col] = 'Q'
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            backtrack(row + 1)

            # 선택 취소
            board[row][col] = '.'
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return result


n_queens_result = solve_n_queens(4)
print(f"4-Queens 해의 개수: {len(n_queens_result)}")
for solution in n_queens_result:
    for row in solution:
        print(row)
    print()


# =============================================================================
# 6. 수도쿠
# =============================================================================

print("=== 수도쿠 ===")

def solve_sudoku(board: List[List[str]]) -> bool:
    """
    LeetCode 37. Sudoku Solver
    수도쿠 풀기
    """
    def is_valid(row: int, col: int, num: str) -> bool:
        # 행 체크
        if num in board[row]:
            return False

        # 열 체크
        for r in range(9):
            if board[r][col] == num:
                return False

        # 3x3 박스 체크
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if board[r][c] == num:
                    return False

        return True

    def backtrack() -> bool:
        # 빈 칸 찾기
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for num in '123456789':
                        if is_valid(row, col, num):
                            board[row][col] = num

                            if backtrack():
                                return True

                            board[row][col] = '.'

                    return False  # 어떤 숫자도 불가능

        return True  # 모든 칸이 채워짐

    return backtrack()


# =============================================================================
# 7. 문자열 분할
# =============================================================================

print("\n=== 문자열 분할 ===")

def partition_palindrome(s: str) -> List[List[str]]:
    """
    LeetCode 131. Palindrome Partitioning
    문자열을 팰린드롬으로만 분할
    """
    result = []

    def is_palindrome(text: str) -> bool:
        return text == text[::-1]

    def backtrack(start: int, path: List[str]):
        if start == len(s):
            result.append(path[:])
            return

        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                path.append(substring)
                backtrack(end, path)
                path.pop()

    backtrack(0, [])
    return result


print(f"'aab' 팰린드롬 분할: {partition_palindrome('aab')}")


# =============================================================================
# 8. 실전 문제 예제
# =============================================================================

print("\n=== 실전 문제 ===")

# 문제 1: 전화번호 문자 조합
def letter_combinations(digits: str) -> List[str]:
    """
    LeetCode 17. Letter Combinations of a Phone Number
    """
    if not digits:
        return []

    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    result = []

    def backtrack(index: int, path: str):
        if index == len(digits):
            result.append(path)
            return

        for char in phone_map[digits[index]]:
            backtrack(index + 1, path + char)

    backtrack(0, '')
    return result


print(f"'23' 문자 조합: {letter_combinations('23')}")


# 문제 2: 단어 검색
def word_search(board: List[List[str]], word: str) -> bool:
    """
    LeetCode 79. Word Search
    2D 보드에서 단어 찾기
    """
    rows, cols = len(board), len(board[0])

    def backtrack(row: int, col: int, index: int) -> bool:
        if index == len(word):
            return True

        if (row < 0 or row >= rows or col < 0 or col >= cols or
            board[row][col] != word[index]):
            return False

        # 임시로 방문 표시
        temp = board[row][col]
        board[row][col] = '#'

        # 4방향 탐색
        found = (backtrack(row - 1, col, index + 1) or
                 backtrack(row + 1, col, index + 1) or
                 backtrack(row, col - 1, index + 1) or
                 backtrack(row, col + 1, index + 1))

        # 원복
        board[row][col] = temp

        return found

    for row in range(rows):
        for col in range(cols):
            if backtrack(row, col, 0):
                return True

    return False


board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
print(f"'ABCCED' 찾기: {word_search(board, 'ABCCED')}")  # True


# 문제 3: 괄호 생성
def generate_parenthesis(n: int) -> List[str]:
    """
    LeetCode 22. Generate Parentheses
    n쌍의 유효한 괄호 조합
    """
    result = []

    def backtrack(path: str, open_count: int, close_count: int):
        if len(path) == 2 * n:
            result.append(path)
            return

        if open_count < n:
            backtrack(path + '(', open_count + 1, close_count)

        if close_count < open_count:
            backtrack(path + ')', open_count, close_count + 1)

    backtrack('', 0, 0)
    return result


print(f"n=3 괄호: {generate_parenthesis(3)}")


# =============================================================================
# 정리: 백트래킹 템플릿
# =============================================================================

"""
백트래킹 기본 템플릿:

def backtrack(상태):
    # 1. 종료 조건
    if 정답 조건:
        결과 저장
        return

    # 2. 모든 선택지 탐색
    for 선택지 in 가능한_선택지:
        # 가지치기 (불가능한 선택은 스킵)
        if 불가능:
            continue

        # 선택
        상태 변경
        선택지 선택

        # 재귀
        backtrack(다음_상태)

        # 선택 취소 (되돌리기)
        상태 복원

문제 유형별 접근:
1. 순열: 순서 중요, 모든 원소 사용
2. 조합: 순서 무관, k개 선택
3. 부분집합: 순서 무관, 모든 크기
4. 제약 조건: N-Queens, 수도쿠

시간 복잡도:
- 순열: O(n!)
- 조합: O(C(n,k))
- 부분집합: O(2^n)
- 가지치기로 실제로는 더 빠름
"""
