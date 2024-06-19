import sys

money = int(input())
check = 1000 - money

answer = 0

while True:
    if check == 0:
        break
    elif check >= 500:
        answer += 1
        check -= 500
    elif check >= 100:
        answer += check // 100
        check = check % 100
    elif check >= 50:
        answer += 1
        check -= 50
    elif check >= 10:
        answer += check // 10
        check = check % 10
    elif check >= 5:
        answer += 1
        check -= 5
    elif check >= 1:
        answer += check
        break

print(answer)