def solution(dartResult):
    answer = 0

    score_list = [[] for _ in range(3)]
    idx = 0
    for i in range(len(dartResult)):
        if dartResult[i] in ['S', 'D', 'T'] and i != len(dartResult) - 1:
            if dartResult[i + 1] in ['*', '#']:
                if dartResult[i - 1] == '0' and dartResult[i - 2] == '1':
                    score_list[idx].append(dartResult[i - 2: i])
                    score_list[idx].append(dartResult[i: i + 1])
                    score_list[idx].append(dartResult[i + 1: i + 2])
                    idx += 1
                else:
                    score_list[idx].append(dartResult[i - 1: i])
                    score_list[idx].append(dartResult[i: i + 1])
                    score_list[idx].append(dartResult[i + 1: i + 2])
                    idx += 1
            else:
                if dartResult[i - 1] == '0' and dartResult[i - 2] == '1':
                    score_list[idx].append(dartResult[i - 2: i])
                    score_list[idx].append(dartResult[i: i + 1])
                    idx += 1
                else:
                    score_list[idx].append(dartResult[i - 1: i])
                    score_list[idx].append(dartResult[i: i + 1])
                    idx += 1
        elif dartResult[i] in ['S', 'D', 'T'] and i == len(dartResult) - 1:
            if dartResult[i - 1] == '0' and dartResult[i - 2] == '1':
                score_list[idx].append(dartResult[i - 2: i])
                score_list[idx].append(dartResult[i: i + 1])
                idx += 1
            else:
                score_list[idx].append(dartResult[i - 1: i])
                score_list[idx].append(dartResult[i: i + 1])
                idx += 1
            break

    print(score_list)

    last = 0
    for i in range(len(score_list)):
        if score_list[i][-1] == '*':
            if i != 2 and score_list[i + 1][-1] == '*':
                if score_list[i][1] == 'S':
                    last += int(score_list[i][0]) * 2
                elif score_list[i][1] == 'D':
                    last += int(score_list[i][0]) ** 2 * 2
                elif score_list[i][1] == 'T':
                    last += int(score_list[i][0]) ** 3 * 2
            elif i != 2 and score_list[i + 1][-1] != '*':
                if score_list[i][1] == 'S':
                    last += int(score_list[i][0])
                elif score_list[i][1] == 'D':
                    last += int(score_list[i][0]) ** 2
                elif score_list[i][1] == 'T':
                    last += int(score_list[i][0]) ** 3
                answer += last * 2
                last = 0
            elif i == 2:
                if score_list[i][1] == 'S':
                    last += int(score_list[i][0])
                elif score_list[i][1] == 'D':
                    last += int(score_list[i][0]) ** 2
                elif score_list[i][1] == 'T':
                    last += int(score_list[i][0]) ** 3
                answer += last * 2
                last = 0

        elif score_list[i][-1] == '#':
            if i != 2 and score_list[i + 1][-1] == '*':
                if score_list[i][1] == 'S':
                    last += int(score_list[i][0]) * -1
                elif score_list[i][1] == 'D':
                    last += int(score_list[i][0]) ** 2 * -1
                elif score_list[i][1] == 'T':
                    last += int(score_list[i][0]) ** 3 * -1
            else:
                if score_list[i][1] == 'S':
                    answer += int(score_list[i][0]) * -1
                elif score_list[i][1] == 'D':
                    answer += int(score_list[i][0]) ** 2 * -1
                elif score_list[i][1] == 'T':
                    answer += int(score_list[i][0]) ** 3 * -1
        else:
            if i != 2 and score_list[i + 1][-1] == '*':
                if score_list[i][1] == 'S':
                    last += int(score_list[i][0])
                elif score_list[i][1] == 'D':
                    last += int(score_list[i][0]) ** 2
                elif score_list[i][1] == 'T':
                    last += int(score_list[i][0]) ** 3
            else:
                if score_list[i][1] == 'S':
                    answer += int(score_list[i][0])
                elif score_list[i][1] == 'D':
                    answer += int(score_list[i][0]) ** 2
                elif score_list[i][1] == 'T':
                    answer += int(score_list[i][0]) ** 3

    return answer
