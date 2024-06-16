import sys
from heapq import heappop, heappush

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

# print(graph)

INF = 10000000
D = [INF] * (V + 1)


# print(D)
def dijkstra(s):
    q = []
    heappush(q, (0, s))
    D[s] = 0

    while q:
        w, v = heappop(q)

        if D[v] < w:
            continue

        for i in graph[v]:
            sum = D[v] + i[1]
            if sum < D[i[0]]:
                D[i[0]] = sum
                heappush(q, (sum, i[0]))


dijkstra(K)
for i in range(1, len(D)):
    if D[i] == 10000000:
        print('INF')
    else:
        print(D[i])
