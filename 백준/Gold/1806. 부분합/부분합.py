N, S = map(int, input().split())
nums = list(map(int, input().split()))

s = 0
e = 0
sum_v = nums[0]
answer = 100001

while True:
    if sum_v < S:
        e += 1
        if e == N:
            break
        sum_v += nums[e]
    else:
        sum_v -= nums[s]
        answer = min(answer, e - s + 1)
        s += 1

if answer == 100001:
    print(0)
else:
    print(answer)