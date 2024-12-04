def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    pos_m = int(pos[0:2])
    pos_s = pos_m * 60 + int(pos[3:5])
    
    video_m = int(video_len[0:2])
    video_s = video_m * 60 + int(video_len[3:5])
    
    op_start_m = int(op_start[0:2])
    op_start_s = op_start_m * 60 + int(op_start[3:5])
    
    op_end_m = int(op_end[0:2])
    op_end_s = op_end_m * 60 + int(op_end[3:5])
    
    for i in range(len(commands)):
        if pos_s >= op_start_s and pos_s <= op_end_s:
            pos_s = op_end_s
            
        if commands[i] == 'next':
            if pos_s + 10 >= video_s:
                pos_s = video_s
            elif pos_s + 10 >= op_start_s and pos_s + 10 <= op_end_s :
                pos_s = op_end_s
            else:
                pos_s += 10
        else:
            if pos_s - 10 <= 0:
                pos_s = 0
            elif pos_s - 10 >= op_start_s and pos_s - 10 <= op_end_s :
                pos_s = op_end_s
            else:
                pos_s -= 10

    answer_m = str(pos_s // 60)
    answer_s = str(pos_s % 60)

    if len(answer_m) == 1:
        answer += '0' + answer_m
    else:
        answer += answer_m
    
    if len(answer_s) == 1:
        answer += ':0' + answer_s
    else:
        answer += ':' + answer_s
        
    return answer