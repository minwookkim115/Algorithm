import sys

sys.setrecursionlimit(10**6)
N = int(input())

graph = [[0] for _ in range(N + 1)]
visited = [0] * (N + 1)
answer = [0] * (N + 1)

for _ in range(N - 1):
    s, e = map(int, input().split())

    graph[s].append(e)
    graph[e].append(s)


def find_answer(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            answer[i] = v
            find_answer(i)


find_answer(1)

for i in range(2, N + 1):
    print(answer[i])
