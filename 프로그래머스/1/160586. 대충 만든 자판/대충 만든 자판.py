def solution(keymap, targets):
    answer = []

    for i in range(len(targets)):
        temp = 0
        for j in range(len(targets[i])):
            count = 100
            for k in range(len(keymap)):
                if targets[i][j] in keymap[k]:
                    for l in range(len(keymap[k])):
                        if targets[i][j] == keymap[k][l]:
                            count = min(count, l + 1)
                            
            if count == 100:
                temp = -1
                break
            else:
                temp += count
        
        answer.append(temp)
            
    return answer