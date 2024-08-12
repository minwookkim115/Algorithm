N, M = map(int, input().split())

floor = [list(map(str, input())) for _ in range(N)]

def find_answer(r, c):
    global visited
    global answer

    if floor[r][c] == '-':
        for i in range(c, M):
            if floor[r][i] == '-':
                visited[r][i] = 1
            elif floor[r][i] != '-':
                answer += 1
                break
            if i == (M - 1):
                answer += 1
    else:
        for i in range(r, N):
            if floor[i][c] == '|':
                visited[i][c] = 1
            elif floor[i][c] != '|':
                answer += 1
                break
            if i == (N - 1):
                answer += 1


visited = [[0] * M for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            visited[i][j] = 1
            find_answer(i, j)

print(answer)