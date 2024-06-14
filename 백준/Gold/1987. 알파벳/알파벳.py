import sys

R, C = map(int, input().split())
alpha = [list(map(lambda x:ord(x)-65, input())) for _ in range(R)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

alpha_check = [0] * 26
alpha_check[alpha[0][0]] = 1
answer = 1
def dfs(r, c, count):
    global answer
    answer = max(answer, count)

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < R and 0 <= nc < C and alpha_check[alpha[nr][nc]] == 0:
            alpha_check[alpha[nr][nc]] = 1
            dfs(nr, nc, count + 1)
            alpha_check[alpha[nr][nc]] = 0

dfs(0, 0, answer)
print(answer)