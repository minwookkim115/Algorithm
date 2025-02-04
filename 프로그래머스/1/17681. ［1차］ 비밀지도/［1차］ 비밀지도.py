def solution(n, arr1, arr2):
    answer = []
    
    pw1 = [''] * n
    pw2 = [''] * n
    
    for i in range(len(arr1)):
        temp = format(arr1[i], 'b')
        num_b = ''
        
        if len(temp) < n:
            s_temp = '0' * (n - len(temp))
            num_b += s_temp + temp
        else:
            num_b = temp
        
        pw = ''
        for tf in num_b:
            if tf == '0':
                pw += ' '
            else:
                pw += '#'
        
        pw1[i] = pw
        
    for i in range(len(arr2)):
        temp = format(arr2[i], 'b')
        num_b = ''
        
        if len(temp) < n:
            s_temp = '0' * (n - len(temp))
            num_b += s_temp + temp
        else:
            num_b = temp
        
        pw = ''
        for tf in num_b:
            if tf == '0':
                pw += ' '
            else:
                pw += '#'
        
        pw2[i] = pw

    
    for i in range(n):
        temp = ''
        for j in range(n):
            if pw1[i][j] == ' ' and pw2[i][j] == ' ':
                temp += ' '
            else:
                temp += '#'
            
        answer.append(temp)
        
    return answer