N = int(input())
cards = list(map(int, input().split()))
M = int(input())
have = list(map(int, input().split()))

answer = {}

for i in cards:
    if i in answer:
        answer[i] += 1
    else:
        answer[i] = 1

for i in have:
    if i in answer:
        print(answer[i], end=' ')
    else:
        print(0, end=' ')