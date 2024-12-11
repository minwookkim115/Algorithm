def solution(name, yearning, photo):
    answer = []
    
    name_year = {}
    for i in range(len(name)):
        name_year[name[i]] = yearning[i]

    for i in range(len(photo)):
        temp = 0
        for j in range(len(photo[i])):
            if photo[i][j] in name_year.keys():
                temp += name_year[photo[i][j]]
                
        answer.append(temp)
        
    return answer