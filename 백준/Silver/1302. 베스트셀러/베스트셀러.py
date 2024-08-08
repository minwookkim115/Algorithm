N = int(input())

answer_d = {}
answer_w = []
for _ in range(N):
    string = input()

    if string in answer_d:
        answer_d[string] += 1
    else:
        answer_w.append(string)
        answer_d[string] = 1

answer_l = []
check = 0
for w in answer_w:
    if answer_d[w] > check:
        answer_l.clear()
        answer_l.append(w)
        check = answer_d[w]
    elif answer_d[w] == check:
        answer_l.append(w)

print(sorted(answer_l)[0])