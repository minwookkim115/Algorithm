import sys
from collections import deque

N, M = map(int, input().split())
arr = list(map(int, input().split()))

q = deque()
for i in range(1, N + 1):
    q.append(i)

answer = 0
i = 0
while True:
    if i == M:
        break
    if arr[i] == q[0]:
        q.popleft()
        i += 1
    else:
        for j in range(len(q)):
            if arr[i] == q[j]:
                if j > len(q) // 2:
                    q.appendleft(q.pop())
                    answer += 1
                    break
                else:
                    q.append(q.popleft())
                    answer += 1
                    break

print(answer)
