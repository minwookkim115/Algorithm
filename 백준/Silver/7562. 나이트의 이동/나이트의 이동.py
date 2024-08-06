import sys
from collections import deque


dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]

T = int(input())

for _ in range(T):
    I = int(input())
    sr, sc = map(int, input().split())
    er, ec = map(int, input().split())

    chess = [[0] * I for _ in range(I)]

    chess[sr][sc] = 1
    chess[er][ec] = 2

    visited = [[0] * I for _ in range(I)]

    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = 1

    while True:
        r, c = q.popleft()

        if chess[r][c] == 2:
            break

        for k in range(8):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < I and 0 <= nc < I and visited[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1

    print(visited[er][ec] - 1)