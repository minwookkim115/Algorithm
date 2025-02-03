def solution(N, stages):
    answer = []
    
    check = {}
    
    for i in range(1, N + 1):
        n_clear = 0
        on_stage = 0
        
        for j in stages:
            if j >= i:
                on_stage += 1
            if i == j:
                n_clear += 1
        
        if on_stage == 0 and n_clear == 0:
            check[i] = 0
        elif on_stage == 0:
            check[i] = 1
        else:
            check[i] = n_clear / on_stage
        print(n_clear, on_stage)
        
    check = sorted(check.items(), key = lambda item: item[1], reverse=True)
    
    for k, v in check:
        answer.append(k)
    
    print(check)
    
    return answer