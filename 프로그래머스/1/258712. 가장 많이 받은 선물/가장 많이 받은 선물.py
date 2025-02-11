def solution(friends, gifts):
    answer = 0
    answer_gift = {}
    gift_score = {}
    for f in friends:
        gift_score[f] = 0
        answer_gift[f] = 0

    gift_state = [[0] * len(friends) for _ in range(len(friends))]
    for g in gifts:
        get, give = g.split(' ')

        gift_state[friends.index(get)][friends.index(give)] += 1
    print(gift_state)
    for i in range(len(friends)):
        give_all = 0
        get_all = 0
        for j in range(len(friends)):
            give_all += gift_state[i][j]
            get_all += gift_state[j][i]
        gift_score[friends[i]] = give_all - get_all

    for i in range(len(friends)):
        for j in range(len(friends)):
            if i != j:
                if gift_state[i][j] > gift_state[j][i]:
                    answer_gift[friends[i]] += 1
                elif gift_state[i][j] < gift_state[j][i]:
                    answer_gift[friends[j]] += 1
                else:
                    if gift_score[friends[i]] > gift_score[friends[j]]:
                        answer_gift[friends[i]] += 1
                    elif gift_score[friends[i]] < gift_score[friends[j]]:
                        answer_gift[friends[j]] += 1
    
    for v in answer_gift.values():
        answer = max(answer, v)
    
    answer //= 2

    return answer