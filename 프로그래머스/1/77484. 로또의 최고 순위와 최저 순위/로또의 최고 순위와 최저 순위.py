def solution(lottos, win_nums):
    answer = [0, 0]

    good_check = 0
    bad_check = 0

    for num in lottos:
        if num in win_nums:
            good_check += 1
        elif num != 0 and num not in win_nums:
            bad_check += 1

    print(good_check)
    print(bad_check)
    
    if bad_check == 6:
        answer[0] = 6
    else:
        answer[0] = 1 + bad_check
        
    if good_check == 0 or good_check == 1:
        answer[1] = 6
    else:
        answer[1] = 7 - good_check

    return answer
