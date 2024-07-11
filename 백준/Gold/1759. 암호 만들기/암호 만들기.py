import sys

L, C = map(int, input().split())
str_l = list(map(str, input().split()))
str_l.sort()

password = ''
answer = []


def find_answer(i, count):
    global password
    if count == L:
        temp1 = 0
        temp2 = 0

        for j in password:
            if j in ['a', 'e', 'i', 'o', 'u']:
                temp1 += 1
            else:
                temp2 += 1

        if temp1 >= 1 and temp2 >= 2:
            answer.append(password)
            return

    for k in range(i, C):
        password += str_l[k]
        find_answer(k + 1, count + 1)
        password = password[:-1]


find_answer(0, 0)
for i in answer:
    print(i)