def solution(ingredient):
    answer = 0

    temp = []
    i = 0
    idx = 0
    while True:
        if i == len(ingredient):
            break
            
        temp.append(ingredient[i])
        
        if len(temp) >= 4:
            if temp[idx - 3 : idx + 1] == [1, 2, 3, 1]:
                for _ in range(4):
                    temp.pop()
                    idx -= 1
                answer += 1
        
        i += 1
        idx += 1
            
    return answer