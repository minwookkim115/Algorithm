def solution(s, skip, index):
    answer = ''
    
    alpha = 'abcdefghijklmnopqrstuvwxyz' * 3
    
    for a in s:
        for i in range(len(alpha)):
            if alpha[i] == a:
                idx = i + 1
                count = 0
                while True:
                    if count == index:
                        break
                    if alpha[idx] in skip:
                        idx += 1
                    else:
                        count += 1
                        idx += 1
                
                answer += alpha[idx - 1]
                break
    
    return answer