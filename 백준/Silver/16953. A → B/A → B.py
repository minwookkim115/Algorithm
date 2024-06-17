import sys
from collections import deque

A, B = map(str, input().split())

q = deque()
q.append(int(B))

answer = 0
avail = False
while q:
    next = q.popleft()

    if str(next) == A:
        avail = True
        break

    if str(next)[-1] == '1':
        if next == 1:
            break
        else:
            temp = str(next)[: len(str(next)) - 1]
            q.append(int(temp))
            answer += 1
    elif next % 2 == 0:
        q.append(next // 2)
        answer += 1

if avail:
    print(answer + 1)
else:
    print(-1)