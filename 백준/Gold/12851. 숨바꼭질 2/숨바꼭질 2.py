import sys
from collections import deque

N, K = map(int, input().split())

check = [0] * 100001

q = deque()
q.append(N)

answer_time = 0
answer_count = 0
while q:
    num = q.popleft()
    if num == K:
        answer_time = check[num]
        answer_count += 1
        continue

    for i in (num - 1, num + 1, num * 2):
        if 0 <= i <= 100000 and (check[i] == 0 or check[i] == check[num] + 1):
            check[i] = check[num] + 1
            q.append(i)

print(answer_time)
print(answer_count)
