def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    banned = {}
    for id in id_list:
        banned[id] = []
    
    for r in report:
        a, b = r.split(' ')
        if a not in banned[b]:
            banned[b].append(a)
    
    for i in range(len(id_list)):
        if len(banned[id_list[i]]) >= k:
            for j in range(len(id_list)):
                if id_list[j] in banned[id_list[i]]:
                    answer[j] += 1
        
    return answer