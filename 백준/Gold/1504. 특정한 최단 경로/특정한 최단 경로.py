import sys
from heapq import heappop, heappush


def dijkstra(s):
    d = [10000000] * (N + 1)
    q = []
    heappush(q, (0, s))
    d[s] = 0

    while q:
        w, v = heappop(q)

        if w > d[v]:
            continue

        for i in graph[v]:
            sum = d[v] + i[1]
            if sum < d[i[0]]:
                d[i[0]] = sum
                heappush(q, (sum, i[0]))

    return d


N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
v1, v2 = map(int, input().split())

s_dist = dijkstra(1)
v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)

t1 = s_dist[v1] + v1_dist[v2] + v2_dist[N]
t2 = s_dist[v2] + v2_dist[v1] + v1_dist[N]
answer = min(t1, t2)
if answer >= 10000000:
    print(-1)
else:
    print(answer)