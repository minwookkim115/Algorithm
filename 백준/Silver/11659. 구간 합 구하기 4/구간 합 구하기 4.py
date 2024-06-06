import sys

N, M = map(int, input().split())
num_l = list(map(int, input().split()))

sum_l = [0 for _ in range(N)]
sum_l[0] = num_l[0]

for i in range(1, len(num_l)):
    sum_l[i] = num_l[i] + sum_l[i - 1]

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())

    if s == 1:
        print(sum_l[e - 1])
    else:
        print(sum_l[e - 1] - sum_l[s - 2])