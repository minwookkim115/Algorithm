def solution(price, money, count):
    answer = 0
    
    all_price = 0
    for c in range(1, count + 1):
        all_price += price * c
    
    answer = all_price - money
    
    if answer < 0:
        answer = 0
    
    return answer