import sys


def dfs(v):
    global answer_dfs
    global visited
    visited[v] = 1

    for i in range(1, N + 1):
        if visited[i] == 0 and v_list[v][i] == 1:
            visited[i] = 1
            answer_dfs.append(i)
            dfs(i)


def bfs():
    global answer_bfs

    visited = [0] * (N + 1)
    queue = []

    num = V
    visited[num] = 1
    answer_bfs.append(V)
    queue.append(V)

    while queue:
        go = queue.pop(0)

        for i in range(N + 1):
            if v_list[go][i] == 1 and visited[i] == 0:
                queue.append(i)
                answer_bfs.append(i)
                visited[i] = 1


N, M, V = map(int, input().split())

v_list = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    v_list[s][e] = 1
    v_list[e][s] = 1

visited = [0] * (N + 1)

answer_dfs = []
answer_dfs.append(V)
answer_bfs = []

dfs(V)
bfs()
print(*answer_dfs)
print(*answer_bfs)