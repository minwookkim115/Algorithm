def solution(schedules, timelogs, startday):
    answer = 0

    for i in range(len(timelogs)):

        work_h = int(str(schedules[i])[:-2])
        work_m = int(str(schedules[i])[-2:]) + 10
        if work_m >= 60:
            work_h += 1
            work_m -= 60

        for j in range(len(timelogs[i])):
            real_work_h = int(str(timelogs[i][j])[:-2])
            real_work_m = int(str(timelogs[i][j])[-2:])

            if (startday + j) % 7 != 6 and (startday + j) % 7 != 0:
                if real_work_h > work_h:
                    break
                elif real_work_h == work_h and real_work_m > work_m:
                    break
        else:
            answer += 1

    return answer