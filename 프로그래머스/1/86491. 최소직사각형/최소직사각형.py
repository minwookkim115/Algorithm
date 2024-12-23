def solution(sizes):
    answer = 0
    
    for i in range(len(sizes)):
        sizes[i][0], sizes[i][1] = max(sizes[i]), min(sizes[i])
    
    temp = 0
    for i in range(len(sizes)):
        temp = max(temp, sizes[i][0])
    
    for i in range(len(sizes)):
        answer = max(answer, temp * sizes[i][1])
            
    return answer