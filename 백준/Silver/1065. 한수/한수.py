N = int(input())

num = 100
answer = 99

while num <= N:

    for i in range(1, len(str(num)) - 1):
        temp = int(str(num)[1]) - int(str(num)[0])
        if int(str(num)[i + 1]) - int(str(num)[i]) != temp:
            break
        answer += 1

    num += 1

if N <= 99:
    print(N)
else:
    print(answer)