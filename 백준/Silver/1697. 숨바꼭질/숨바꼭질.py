import sys

N, K = map(int, input().split())

check = [0] * 100001

q = []
q.append(N)

while q:
    num = q.pop(0)
    if num == K:
        print(check[num])
        break
    else:
        for i in (num - 1, num + 1, num * 2):
            if 0 <= i <= 100000 and check[i] == 0:
                check[i] = check[num] + 1
                q.append(i)