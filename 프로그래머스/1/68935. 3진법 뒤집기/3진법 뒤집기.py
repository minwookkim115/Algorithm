def solution(n):
    answer = 0

    num = 0
    three = ''
    while True:
        if 3 ** num > n:
            num -= 1
            three += str(n // 3 ** num)
            n %= 3 ** num
        else:
            num += 1

        if num == 0:
            break
    
    for i in range(len(three)):
        temp = int(three[i])
        answer += (3 ** i) * temp
            
        
    return answer