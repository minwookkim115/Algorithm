def solution(players, callings):
    
    check = {}
    for i in range(len(players)):
        check[players[i]] = i
        
        
    for c in callings:
        idx = check[c]
        check[c] -= 1
        check[players[idx - 1]] += 1
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
        
    return players