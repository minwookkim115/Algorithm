def solution(babbling):
    answer = 0
    
    for word in babbling:
        i = 0
        check = ''
        while True:
            if i >= len(word):
                answer += 1
                break
                
            if word[i: i + 3] == 'aya' and check != 'aya':
                check = 'aya'
                i += 3
            elif word[i: i + 2] == 'ye' and check != 'ye':
                check = 'ye'
                i += 2
            elif word[i: i + 3] == 'woo' and check != 'woo':
                check = 'woo'
                i += 3
            elif word[i: i + 2] == 'ma' and check != 'ma':
                check = 'ma'
                i += 2
            else:
                break
        
        
    return answer