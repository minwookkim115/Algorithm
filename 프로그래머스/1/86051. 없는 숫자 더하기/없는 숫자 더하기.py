def solution(numbers):
    answer = 0
    check = [0 for _ in range(10)]
    
    for num in numbers:
        check[num] = 1
    
    for i in range(len(check)):
        if check[i] == 0:
            answer += i
    
    return answer