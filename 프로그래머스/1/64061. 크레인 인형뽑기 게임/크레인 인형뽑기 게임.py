def solution(board, moves):
    answer = 0
    
    check = []
    
    for move in moves:
        if len(check) >= 2:
            if check[-1] == check[-2]:
                check.pop()
                check.pop()
                answer += 2
            
        for i in range(len(board)):
            if board[i][move - 1] != 0:
                check.append(board[i][move - 1])
                board[i][move - 1] = 0
                break
                
    return answer