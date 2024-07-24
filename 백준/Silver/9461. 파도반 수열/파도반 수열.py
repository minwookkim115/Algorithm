T = int(input())
for _ in range(T):
    N = int(input())

    dp = [0] * (N + 1)

    if N == 1:
        dp[0] = 1
    elif N == 2:
        dp[0] = 1
        dp[1] = 1
    else:
        dp[0] = 1
        dp[1] = 1
        dp[2] = 1

    if N >= 3:
        for i in range(3, N + 1):
            dp[i] = dp[i - 3] + dp[i - 2]

    print(dp[N - 1])