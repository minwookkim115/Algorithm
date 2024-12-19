def solution(number, limit, power):
    answer = 0
    
    divisor_count = []

    for i in range(1, number + 1):
        temp = []
        for j in range(1, int(i**(1/2)) + 1):
            if i % j == 0:
                temp.append(j)
                if j < i // j:
                    temp.append(i // j)
            
        divisor_count.append(len(temp))

    
    for attack in divisor_count:
        if attack > limit:
            answer += power
        else:
            answer += attack
        
    return answer