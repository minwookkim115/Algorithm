import sys

num = 1
for _ in range(3):
    n = int(input())
    num *= n

answer = [0] * 10
for i in str(num):
    if i == '0':
        answer[0] += 1
    elif i == '1':
        answer[1] += 1
    elif i == '2':
        answer[2] += 1
    elif i == '3':
        answer[3] += 1
    elif i == '4':
        answer[4] += 1
    elif i == '5':
        answer[5] += 1
    elif i == '6':
        answer[6] += 1
    elif i == '7':
        answer[7] += 1
    elif i == '8':
        answer[8] += 1
    elif i == '9':
        answer[9] += 1

for i in answer:
    print(i)