"""
동적 프로그래밍 (Dynamic Programming)
=====================================
DP는 큰 문제를 작은 부분 문제로 나누어 해결하는 기법입니다.
"""

from typing import List
from functools import lru_cache

# =============================================================================
# 1. DP 기본 개념
# =============================================================================

"""
DP의 두 가지 조건:
1. 최적 부분 구조 (Optimal Substructure)
   - 큰 문제의 최적해가 작은 문제의 최적해를 포함

2. 중복되는 부분 문제 (Overlapping Subproblems)
   - 동일한 작은 문제가 반복적으로 나타남

DP 구현 방식:
1. Top-Down (Memoization): 재귀 + 캐싱
2. Bottom-Up (Tabulation): 반복문 + 테이블
"""


# =============================================================================
# 2. 피보나치 수열 - DP 입문
# =============================================================================

print("=== 피보나치 수열 ===")

# 방법 1: 일반 재귀 (비효율적) - O(2^n)
def fib_recursive(n: int) -> int:
    """일반 재귀 - 지수 시간"""
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# 방법 2: Memoization (Top-Down) - O(n)
def fib_memo(n: int, memo: dict = None) -> int:
    """메모이제이션"""
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# 방법 3: @lru_cache 데코레이터 (가장 간단)
@lru_cache(maxsize=None)
def fib_cache(n: int) -> int:
    """lru_cache 활용"""
    if n <= 1:
        return n
    return fib_cache(n - 1) + fib_cache(n - 2)


# 방법 4: Tabulation (Bottom-Up) - O(n)
def fib_tab(n: int) -> int:
    """바텀업 방식"""
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# 방법 5: 공간 최적화 - O(1) 공간
def fib_optimized(n: int) -> int:
    """공간 최적화"""
    if n <= 1:
        return n

    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current

    return prev1


print(f"fib(10) = {fib_tab(10)}")  # 55
print(f"fib(30) = {fib_optimized(30)}")  # 832040


# =============================================================================
# 3. 계단 오르기 문제
# =============================================================================

print("\n=== 계단 오르기 ===")

def climb_stairs(n: int) -> int:
    """
    LeetCode 70. Climbing Stairs
    한 번에 1칸 또는 2칸씩 오를 수 있을 때, n칸 오르는 방법의 수
    """
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def climb_stairs_optimized(n: int) -> int:
    """공간 최적화 버전"""
    if n <= 2:
        return n

    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current

    return prev1


print(f"5칸 오르기: {climb_stairs(5)} 가지")  # 8


# =============================================================================
# 4. 최대 부분 합 (Kadane's Algorithm)
# =============================================================================

print("\n=== 최대 부분 합 ===")

def max_subarray(nums: List[int]) -> int:
    """
    LeetCode 53. Maximum Subarray
    연속된 부분 배열의 최대 합
    """
    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        # 현재 요소를 포함하여 계속할지, 새로 시작할지
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"배열: {nums}")
print(f"최대 부분 합: {max_subarray(nums)}")  # 6 (4 + -1 + 2 + 1)


# =============================================================================
# 5. 동전 교환 (Coin Change)
# =============================================================================

print("\n=== 동전 교환 ===")

def coin_change(coins: List[int], amount: int) -> int:
    """
    LeetCode 322. Coin Change
    amount를 만들기 위한 최소 동전 개수
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


def coin_change_ways(coins: List[int], amount: int) -> int:
    """동전으로 amount를 만드는 경우의 수"""
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]


coins = [1, 2, 5]
print(f"동전: {coins}")
print(f"11원 최소 동전: {coin_change(coins, 11)}개")  # 3 (5+5+1)
print(f"5원 만드는 방법: {coin_change_ways(coins, 5)}가지")  # 4


# =============================================================================
# 6. 최장 증가 부분 수열 (LIS)
# =============================================================================

print("\n=== 최장 증가 부분 수열 ===")

def longest_increasing_subsequence(nums: List[int]) -> int:
    """
    LeetCode 300. Longest Increasing Subsequence
    O(n²) 솔루션
    """
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n  # dp[i]: nums[i]를 마지막으로 하는 LIS 길이

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def lis_binary_search(nums: List[int]) -> int:
    """O(n log n) 솔루션"""
    import bisect

    if not nums:
        return 0

    tails = []  # tails[i]: 길이가 i+1인 LIS의 마지막 최솟값

    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num

    return len(tails)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(f"배열: {nums}")
print(f"LIS 길이: {longest_increasing_subsequence(nums)}")  # 4 (2,3,7,101 or 2,5,7,101)


# =============================================================================
# 7. 0/1 배낭 문제 (Knapsack)
# =============================================================================

print("\n=== 0/1 배낭 문제 ===")

def knapsack(weights: List[int], values: List[int], capacity: int) -> int:
    """
    0/1 배낭 문제
    각 아이템을 넣거나 안 넣거나
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # 현재 아이템을 넣지 않는 경우
            dp[i][w] = dp[i - 1][w]

            # 현재 아이템을 넣는 경우
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )

    return dp[n][capacity]


def knapsack_optimized(weights: List[int], values: List[int], capacity: int) -> int:
    """공간 최적화 버전"""
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        # 역순으로 순회 (중복 방지)
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 8

print(f"무게: {weights}, 가치: {values}, 용량: {capacity}")
print(f"최대 가치: {knapsack(weights, values, capacity)}")  # 10


# =============================================================================
# 8. 편집 거리 (Edit Distance)
# =============================================================================

print("\n=== 편집 거리 ===")

def edit_distance(word1: str, word2: str) -> int:
    """
    LeetCode 72. Edit Distance
    word1을 word2로 변환하는 최소 연산 횟수
    연산: 삽입, 삭제, 교체
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 초기화
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # 삭제
                    dp[i][j - 1],      # 삽입
                    dp[i - 1][j - 1]   # 교체
                )

    return dp[m][n]


print(f"'horse' -> 'ros': {edit_distance('horse', 'ros')}")  # 3
print(f"'intention' -> 'execution': {edit_distance('intention', 'execution')}")  # 5


# =============================================================================
# 9. 최장 공통 부분 수열 (LCS)
# =============================================================================

print("\n=== 최장 공통 부분 수열 ===")

def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    LeetCode 1143. Longest Common Subsequence
    두 문자열의 최장 공통 부분 수열 길이
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


print(f"'abcde' & 'ace': {longest_common_subsequence('abcde', 'ace')}")  # 3


# =============================================================================
# 10. 실전 문제 예제
# =============================================================================

print("\n=== 실전 문제 ===")

# 문제 1: 정수 삼각형
def integer_triangle(triangle: List[List[int]]) -> int:
    """
    프로그래머스 정수 삼각형
    위에서 아래로 내려올 때 최대 합
    """
    n = len(triangle)
    dp = [row[:] for row in triangle]  # 깊은 복사

    for i in range(1, n):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] += dp[i - 1][0]
            elif j == len(triangle[i]) - 1:
                dp[i][j] += dp[i - 1][-1]
            else:
                dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])

    return max(dp[-1])


triangle = [
    [7],
    [3, 8],
    [8, 1, 0],
    [2, 7, 4, 4],
    [4, 5, 2, 6, 5]
]
print(f"정수 삼각형 최대 합: {integer_triangle(triangle)}")  # 30


# 문제 2: 등굣길
def school_path(m: int, n: int, puddles: List[List[int]]) -> int:
    """
    프로그래머스 등굣길
    (1,1)에서 (m,n)까지 가는 최단 경로 수
    """
    MOD = 1_000_000_007
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1

    puddle_set = set((p[0], p[1]) for p in puddles)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if (j, i) in puddle_set:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD

    return dp[n][m]


print(f"등굣길: {school_path(4, 3, [[2, 2]])}")  # 4


# 문제 3: 도둑질
def house_robber(money: List[int]) -> int:
    """
    프로그래머스 도둑질 (원형)
    LeetCode 213. House Robber II
    인접한 집은 털 수 없음 (원형 배열)
    """
    def rob_linear(houses: List[int]) -> int:
        if len(houses) == 1:
            return houses[0]

        dp = [0] * len(houses)
        dp[0] = houses[0]
        dp[1] = max(houses[0], houses[1])

        for i in range(2, len(houses)):
            dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])

        return dp[-1]

    if len(money) == 1:
        return money[0]

    # 첫 집 포함 (마지막 집 제외) vs 첫 집 제외 (마지막 집 포함)
    return max(rob_linear(money[:-1]), rob_linear(money[1:]))


money = [1, 2, 3, 1]
print(f"도둑질 최대 금액: {house_robber(money)}")  # 4


# =============================================================================
# 정리: DP 문제 접근법
# =============================================================================

"""
DP 문제 해결 4단계:

1. 상태 정의
   - dp[i]가 무엇을 의미하는지 명확히 정의
   - 예: dp[i] = i번째까지 고려했을 때 최대값

2. 점화식 찾기
   - 현재 상태가 이전 상태들과 어떻게 연결되는지
   - 예: dp[i] = max(dp[i-1], dp[i-2] + value[i])

3. 초기값 설정
   - 기저 사례 설정
   - 예: dp[0] = 0, dp[1] = value[1]

4. 계산 순서 결정
   - Bottom-Up: 작은 문제부터 큰 문제로
   - Top-Down: 큰 문제에서 작은 문제로 (재귀)

자주 나오는 DP 패턴:
1. 1차원 DP: 피보나치, 계단 오르기
2. 2차원 DP: 편집 거리, LCS
3. 배낭 DP: 0/1 배낭, 동전 교환
4. 구간 DP: 최적 이진 검색 트리
5. 비트마스크 DP: 외판원 문제 (TSP)
"""
