import sys

N = int(input())

house = []
for _ in range(N):
    color = list(map(int, input().split()))
    house.append(color)

dp = [[0] * 3 for _ in range(N)]
for i in range(3):
    dp[0][i] = house[0][i]

for i in range(1, N):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(house[i][j] + dp[i - 1][j + 1], house[i][j] + dp[i - 1][j + 2])
        elif j == 1:
            dp[i][j] = min(house[i][j] + dp[i - 1][j - 1], house[i][j] + dp[i - 1][j + 1])
        else:
            dp[i][j] = min(house[i][j] + dp[i - 1][j - 1], house[i][j] + dp[i - 1][j - 2])

print(min(dp[N - 1]))