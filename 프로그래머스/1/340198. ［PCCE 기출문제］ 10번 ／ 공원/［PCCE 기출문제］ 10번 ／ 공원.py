def solution(mats, park):
    answer = -1
    print(mats)
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == '-1':
                for mat in mats:
                    check = True
                    if i + mat <= len(park) and j + mat <= len(park[0]):
                        for r in range(i, i + mat):
                            for c in range(j, j + mat):
                                if i == 2 and j == 2:
                                    print(r, c, mat)
                                if park[r][c] != '-1':
                                    check = False
                    else:
                        check = False
                                    
                    if check == True:
                        answer = max(answer, mat)
                            
    return answer