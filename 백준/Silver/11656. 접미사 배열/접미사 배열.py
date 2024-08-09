S = input()

answer_l = []

for i in range(len(S)):
    temp = S[len(S) - i - 1:]
    answer_l.append(temp)

answer_l.sort()
for i in answer_l:
    print(i)