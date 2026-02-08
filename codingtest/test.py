import sys
N, M = map(int, sys.stdin.readline().split())
baskets = [i for i in range(N + 1)]  # 1~N번 공이 들어있음

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    A = baskets[i]
    baskets[i] = baskets[j]
    baskets[j] = A

print(' '.join(map(str, baskets[1:N+1])))
