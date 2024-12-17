def solution(s):
    answer = 0
    
    count = 0
    temp_c = 0
    temp_s = ''
    
    for i in range(len(s)):
        if count == temp_c:
            temp_s = s[i]
            answer += 1
            count = 0
            temp_c = 0
        
        if temp_s != s[i]:
            temp_c += 1
        else:
            count += 1
        
    return answer