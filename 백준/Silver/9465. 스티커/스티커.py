T = int(input())

for _ in range(T):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * (n + 1) for _ in range(2)]

    for i in range(1, n + 1):
        dp[0][i] = max(sticker[0][i - 1] + dp[1][i - 1], dp[0][i - 1])
        dp[1][i] = max(sticker[1][i - 1] + dp[0][i - 1], dp[1][i - 1])

    print(max(dp[0][n], dp[1][n]))