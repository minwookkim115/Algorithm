import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    paper = list(map(int, sys.stdin.readline().split()))

    answer = 0
    check_paper = []

    for j in range(len(paper)):
        check_paper.append([paper[j], j])

    if len(paper) == 1:
        print(1)
    else:

        while True:
            for i in range(1, len(check_paper)):
                if check_paper[0][0] < check_paper[i][0]:
                    check_paper.append(check_paper[0])
                    check_paper.pop(0)
                    break
            else:
                if check_paper[0][1] == M:
                    print(answer + 1)
                    break
                else:
                    check_paper.pop(0)
                    answer += 1