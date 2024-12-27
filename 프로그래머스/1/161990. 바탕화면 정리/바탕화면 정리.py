def solution(wallpaper):
    answer = [len(wallpaper) + 1, len(wallpaper[0]) + 1, 0, 0]
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                t = i
                l = j
                b = i + 1
                r = j + 1
                answer[0] = min(answer[0], t)
                answer[1] = min(answer[1], l)
                answer[2] = max(answer[2], b)
                answer[3] = max(answer[3], r)
                    
    
    return answer