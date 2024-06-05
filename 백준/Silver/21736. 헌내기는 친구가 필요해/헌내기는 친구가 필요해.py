import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

campus = [list(map(str, sys.stdin.readline())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

answer = 0


def find_answer(r, c):
    global answer

    if campus[r][c] == 'P':
        answer += 1

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if 0 <= nr < N and 0 <= nc < M and visit[nr][nc] == 0 and campus[nr][nc] != 'X':
            visit[nr][nc] = 1
            find_answer(nr, nc)


sr = 0
sc = 0
for r in range(N):
    for c in range(M):
        if campus[r][c] == 'I':
            sr = r
            sc = c

find_answer(sr, sc)

if answer == 0:
    print('TT')
else:
    print(answer)