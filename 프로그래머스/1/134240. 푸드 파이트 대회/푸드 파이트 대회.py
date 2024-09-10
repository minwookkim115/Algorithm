def solution(food):
    answer = ''

    right_answer = ''    
    for i in range(len(food) - 1, 0, -1):
        if food[i] // 2 >= 1:
            right_answer += str(i) * (food[i] // 2)
    
    left_answer = ''
    for i in range(1, len(food)):
        if food[i] // 2 >= 1:
            left_answer += str(i) * (food[i] // 2)
            
    answer += left_answer + '0' + right_answer
    
    return answer