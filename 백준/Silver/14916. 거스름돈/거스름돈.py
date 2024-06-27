n = int(input())

answer = 0
if n == 1 or n == 3:
    answer = -1
elif n % 5 == 0:
    answer = n // 5
else:
    while True:
        if n % 5 == 0:
            break
        n -= 2
        answer += 1
    answer += n // 5

print(answer)