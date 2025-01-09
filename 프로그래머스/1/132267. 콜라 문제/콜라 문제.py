def solution(a, b, n):
    answer = 0
    
    temp = 0
    while True:
        if n < a:
            break
        answer += (n // a) * b
        temp += n % a
        n = (n // a) * b
        n += temp
        temp = 0
        
    return answer