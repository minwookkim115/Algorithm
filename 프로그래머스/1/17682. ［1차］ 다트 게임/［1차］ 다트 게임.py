def solution(dartResult):
    answer = 0
    temp = 0
    last = 0

    for i in range(len(dartResult)):
        if dartResult[i] == '1':
            if dartResult[i + 1] == '0':
                if dartResult[i + 2] == 'S':
                    temp += 10
                    if i < len(dartResult) - 3:
                        if dartResult[i + 2] != '*' and dartResult[i + 2] != '#':
                            answer += temp
                            last = temp
                            temp = 0
                    else:
                        answer += temp
                        last = temp
                        temp = 0
                elif dartResult[i + 2] == 'D':
                    temp += 10 ** 2
                    if i < len(dartResult) - 3:
                        if dartResult[i + 2] != '*' and dartResult[i + 2] != '#':
                            answer += temp
                            last = temp
                            temp = 0
                    else:
                        answer += temp
                        last = temp
                        temp = 0
                elif dartResult[i + 2] == 'T':
                    temp += 10 ** 3
                    if i < len(dartResult) - 3:
                        if dartResult[i + 2] != '*' and dartResult[i + 2] != '#':
                            answer += temp
                            last = temp
                            temp = 0
                    else:
                        answer += temp
                        last = temp
                        temp = 0
            else:
                temp += 1
                if i < len(dartResult) - 2:
                    if dartResult[i + 2] != '*' and dartResult[i + 2] != '#':
                        answer += temp
                        last = temp
                        temp = 0
                else:
                    answer += temp
                    last = temp
                    temp = 0

        elif dartResult[i] in ['2', '3', '4', '5', '6', '7', '8', '9']:
            if dartResult[i + 1] == 'S':
                temp += int(dartResult[i]) ** 1
                if i < len(dartResult) - 2:
                    if dartResult[i + 2] != '*' and dartResult[i + 2] != '#':
                        answer += temp
                        last = temp
                        temp = 0
                else:
                    answer += temp
                    last = temp
                    temp = 0
            elif dartResult[i + 1] == 'D':
                temp += int(dartResult[i]) ** 2
                if i < len(dartResult) - 2:
                    if dartResult[i + 2] != '*' and dartResult[i + 2] != '#':
                        answer += temp
                        last = temp
                        temp = 0
                else:
                    answer += temp
                    last = temp
                    temp = 0
            elif dartResult[i + 1] == 'T':
                temp += int(dartResult[i]) ** 3
                if i < len(dartResult) - 2:
                    if dartResult[i + 2] != '*' and dartResult[i + 2] != '#':
                        answer += temp
                        last = temp
                        temp = 0
                else:
                    answer += temp
                    last = temp
                    temp = 0

        if dartResult[i] == '*':
            last += temp
            last *= 2
            answer += last
            answer -= last
            temp = 0

        if dartResult[i] == '#':
            answer += -temp
            temp = 0

    return answer