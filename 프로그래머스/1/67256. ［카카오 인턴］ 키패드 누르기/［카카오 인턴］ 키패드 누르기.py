def solution(numbers, hand):
    answer = ''
    
    phone = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ['*', 0, '#']
    ]

    l_hand = [3, 0]
    r_hand = [3, 2]
    
    for num in numbers:
        
        for r in range(len(phone)):
            for c in range(len(phone[0])):
                if phone[r][c] == num:
                    
                    if num in [1, 4, 7]:
                        answer += 'L'
                        l_hand = [r, c]
                    elif num in [3, 6, 9]:
                        answer += 'R'
                        r_hand = [r, c]
                    elif num in [2, 5, 8, 0]:
                        l_d = abs(r - l_hand[0]) + abs(c - l_hand[1])
                        r_d = abs(r - r_hand[0]) + abs(c - r_hand[1])
                        
                        if l_d > r_d:
                            answer += 'R'
                            r_hand = [r, c]
                        elif l_d < r_d:
                            answer += 'L'
                            l_hand = [r, c]
                        else:
                            if hand =='right':
                                answer += 'R'
                                r_hand = [r, c]
                            else:
                                answer += 'L'
                                l_hand = [r, c]
    
    return answer