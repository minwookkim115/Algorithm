import sys

N = int(input())
slide = [list(map(int, input().split())) for _ in range(N)]

max_dp = [[0, 0, 0] for _ in range(2)]
min_dp = [[0, 0, 0] for _ in range(2)]
max_dp[0] = slide[0].copy()
min_dp[0] = slide[0].copy()

for j in range(1, N):
    i = j % 2
    max_dp[i][0] = max(slide[j][0] + max_dp[i - 1][0], slide[j][0] + max_dp[i - 1][1])
    max_dp[i][1] = max(slide[j][1] + max_dp[i - 1][0], slide[j][1] + max_dp[i - 1][1],
                       slide[j][1] + max_dp[i - 1][2])
    max_dp[i][2] = max(slide[j][2] + max_dp[i - 1][1], slide[j][2] + max_dp[i - 1][2])

    min_dp[i][0] = min(slide[j][0] + min_dp[i - 1][0], slide[j][0] + min_dp[i - 1][1])
    min_dp[i][1] = min(slide[j][1] + min_dp[i - 1][0], slide[j][1] + min_dp[i - 1][1],
                       slide[j][1] + min_dp[i - 1][2])
    min_dp[i][2] = min(slide[j][2] + min_dp[i - 1][1], slide[j][2] + min_dp[i - 1][2])

print(max(max_dp[N % 2 - 1]), min(min_dp[N % 2 - 1]))