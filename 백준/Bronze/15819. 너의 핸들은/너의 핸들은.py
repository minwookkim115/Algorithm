N, I = map(int, input().split())

answer_l = []
for i in range(N):
    string = input()
    answer_l.append(string)

answer_l.sort()

print(answer_l[I - 1])