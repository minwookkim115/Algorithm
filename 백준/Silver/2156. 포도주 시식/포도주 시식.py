import sys

n = int(input())

grape = [int(input()) for _ in range(n)]

dp = [0] * 10001

dp[0] = grape[0]
if len(grape) >= 2:
    dp[1] = grape[0] + grape[1]
if len(grape) >= 3:
    dp[2] = max(grape[0] + grape[2], grape[1] + grape[2], dp[1])

    for i in range(3, n):
        dp[i] = max(dp[i - 3] + grape[i - 1] + grape[i], dp[i - 2] + grape[i], dp[i - 1])

print(dp[n - 1])
