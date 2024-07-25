import sys
sys.setrecursionlimit(10 ** 6)


def dfs(s):
    visited[s] = 1

    for go in graph[s]:
        if visited[go] == 0:
            dfs(go)
    return


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N + 1)
answer = 0
for i in range(1, N + 1):
    if visited[i] == 0:
        dfs(i)
        answer += 1

print(answer)
