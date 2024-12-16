def solution(s):
    answer = []
    
    check = []
    
    for i in range(len(s)):
        if s[i] not in check:
            check.append(s[i])
            answer.append(-1)
        else:
            for j in range(i - 1, -1, -1):
                if s[j] == s[i]:
                    answer.append(i - j)
                    break
                else:
                    continue
        
    return answer