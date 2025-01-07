def solution(cards1, cards2, goal):
    answer = 'Yes'
    
    for g in goal:
        if g in cards1:
            if g == cards1[0]:
                cards1.pop(0)
            else:
                answer = 'No'
                break
        elif g in cards2:
            if g == cards2[0]:
                cards2.pop(0)
            else:
                answer = 'No'
                break
            
    return answer