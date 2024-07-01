str1 = input()
str2 = input()
s1_l = len(str1)
s2_l = len(str2)

dp = [[0] * (s1_l + 1) for _ in range(s2_l + 1)]

for i in range(1, s2_l + 1):
    for j in range(1, s1_l + 1):
        if str2[i - 1] == str1[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[s2_l][s1_l])
