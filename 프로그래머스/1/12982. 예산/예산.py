def solution(d, budget):
    answer = len(d)
    
    d.sort()
    
    temp = 0
    for i in range(len(d)):
        temp += d[i]
        print(temp, i)
        if temp > budget:
            answer = i
            break
        elif temp == budget:
            answer = i + 1
            break
            
    return answer