def solution(people, limit):
    answer = 0
    e = len(people)
    people.sort()

    for i in range(len(people) // 2):
        while e > i + 1:
            e -= 1
            if people[i] + people[e] <= limit:
                answer += 1
                break

    answer += len(people) - answer * 2

    return answer
