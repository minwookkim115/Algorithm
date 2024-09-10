def solution(progresses, speeds):
    answer = []
    
    idx = 0
    while True:
        if idx == len(progresses):
            break

        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        if progresses[idx] >= 100:
            count = 0
            for j in range(idx, len(progresses)):
                if progresses[j] >= 100:
                    count += 1
                    idx += 1
                else:
                    break
            answer.append(count)
    
    return answer