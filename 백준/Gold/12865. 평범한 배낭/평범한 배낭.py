import sys

N, K = map(int, input().split())
things = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (K + 1)

for w, v in things:
    for i in range(K, w - 1, -1):
        dp[i] = max(dp[i], dp[i - w] + v)

print(dp[K])