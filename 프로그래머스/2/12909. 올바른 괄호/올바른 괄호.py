def solution(s):
    answer = True
    
    stack = []
    i = - 1
    for v in s:
        if v == '(':
            stack.append(v)
            i += 1
        else:
            if i == - 1:
                answer = False
                break
            else:
                i -= 1
    
    if i > - 1:
        answer = False

    return answer