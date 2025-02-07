import copy

def solution(want, number, discount):
    answer = 0

    for i in range(0, len(discount) - 9):
        check = copy.copy(number)
        for j in range(len(want)):
            for k in range(i, i + 10):

                if want[j] == discount[k]:
                    check[j] -= 1

            if check[j] != 0:
                break

        if max(check) == 0:
            answer += 1

    return answer