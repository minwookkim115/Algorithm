import sys

N = int(input())
M = int(input())
IO = input()

check_IO = ''

for i in range((2 * N) + 1):
    if i % 2 == 0:
        check_IO += 'I'
    else:
        check_IO += 'O'

answer = 0
for i in range(len(IO) - (2 * N) + 1):
    if IO[i] == 'I':
        if check_IO == IO[i: i + (2 * N) + 1]:
            answer += 1

print(answer)
