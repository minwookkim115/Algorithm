import sys
from heapq import heappop, heappush


def dijkstra(s, x):
    q = []
    heappush(q, (0, s))
    min_t = [10000000] * (N + 1)
    min_t[s] = 0

    while q:
        w, party = heappop(q)

        if w > min_t[party]:
            continue

        for i in students[party]:
            sum = min_t[party] + i[1]
            if sum < min_t[i[0]]:
                min_t[i[0]] = sum
                heappush(q, (sum, i[0]))

    return min_t[x]


N, M, X = map(int, input().split())
students = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    students[s].append([e, t])

answer = 0
for i in range(1, N + 1):
    if i == X:
        continue
    answer = max(dijkstra(X, i) + dijkstra(i, X), answer)

print(answer)