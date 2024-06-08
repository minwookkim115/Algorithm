import sys
from collections import deque

N, M = map(int, input().split())
relation = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    relation[s].append(e)
    relation[e].append(s)

answer = 0
min_v = 1000000


def bfs(n):
    global answer
    global min_v

    q = deque()
    visited = [-1] * (N + 1)
    visited[0] = 0

    q.append(n)
    visited[n] = 0

    while q:
        go = q.popleft()
        for j in relation[go]:
            if visited[j] == -1:
                q.append(j)
                visited[j] = visited[go] + 1

    if sum(visited) < min_v:
        min_v = sum(visited)
        answer = n


for i in range(1, N + 1):
    bfs(i)

print(answer)
