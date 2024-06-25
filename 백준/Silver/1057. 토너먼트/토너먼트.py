import sys

N, ji, han = map(int, input().split())

answer = 1
while True:
    check1 = max(ji, han)
    check2 = min(ji, han)
    if check1 % 2 == 0 and check2 % 2 == 1:
        if check1 - check2 == 1:
            break

    if ji % 2 == 0:
        ji //= 2
    else:
        ji = (ji + 1) // 2

    if han % 2 == 0:
        han //= 2
    else:
        han = (han + 1) // 2

    answer += 1

print(answer)