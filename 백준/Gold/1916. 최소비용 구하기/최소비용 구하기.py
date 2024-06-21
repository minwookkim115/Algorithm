import sys
from heapq import heappush, heappop


def dijkstra(s):
    q = []
    heappush(q, (0, s))
    min_cost[s] = 0

    while q:
        w, v = heappop(q)

        if w > min_cost[v]:
            continue

        for i in bus[v]:
            sum = min_cost[v] + i[1]
            if sum < min_cost[i[0]]:
                min_cost[i[0]] = sum
                heappush(q, (sum, i[0]))


N = int(input())
M = int(input())
bus = [[] for _ in range(N + 1)]
for _ in range(M):
    c1, c2, cost = map(int, input().split())
    bus[c1].append([c2, cost])

s, e = map(int, input().split())

min_cost = [1000000000] * (N + 1)

dijkstra(s)

print(min_cost[e])