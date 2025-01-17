def solution(X, Y):
    answer = ''
    
    check = []
    for num in range(0, 10):
        count_x = 0
        count_y = 0
        if str(num) in X and str(num) in Y:
            count_x = X.count(str(num))
            count_y = Y.count(str(num))
            
            if count_x > count_y:
                for i in range(count_y):
                    check.append(str(num))
            else:
                for i in range(count_x):
                    check.append(str(num))
    check.sort(reverse=True)
    
    if len(check) == 0:
        answer = '-1'
    elif check[0] == '0':
        answer = '0'
    else:
        for i in range(len(check)):
            answer += check[i]
    return answer