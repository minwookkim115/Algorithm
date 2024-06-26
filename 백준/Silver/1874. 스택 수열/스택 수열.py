import sys

n = int(input())

stack = []
check = 1
answer = ''

for _ in range(n):
    num = int(input())

    if stack:
        if stack[-1] < num:
            for i in range(check, num + 1):
                stack.append(i)
                check = num + 1
                answer += '+'
            stack.pop()
            answer += '-'
        elif stack[-1] == num:
            stack.pop()
            answer += '-'
        else:
            answer = 'NO'
            break
    else:
        for i in range(check, num + 1):
            stack.append(i)
            check = num + 1
            answer += '+'
        stack.pop()
        answer += '-'

if answer == 'NO':
    print(answer)
else:
    for i in answer:
        print(i)