def solution(today, terms, privacies):
    answer = []

    term = {}
    for t in terms:
        a, b = t.split(' ')
        term[a] = int(b)

    for i in range(len(privacies)):
        date, t_type = privacies[i].split(' ')
        month = term[t_type]

        y, m, d = date.split('.')
        y = int(y)
        m = int(m)
        d = int(d)

        if month >= 12:
            y += month // 12
            month %= 12
            if month + m > 12:
                y += 1
                m = month + m - 12
            else:
                m += month
        else:
            if month + m > 12:
                y += 1
                m = month + m - 12
            else:
                m += month

        if d == 1:
            m -= 1
            d = 28
        else:
            d -= 1

        ty, tm, td = today.split('.')
        ty = int(ty)
        tm = int(tm)
        td = int(td)

        if ty > y:
            answer.append(i + 1)
        elif ty == y:
            if tm > m:
                answer.append(i + 1)
            elif tm == m:
                if td > d:
                    answer.append(i + 1)
    print(answer)
    return answer