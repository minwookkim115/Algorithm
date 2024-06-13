import sys

T = int(input())

for _ in range(T):
    p = list(map(str, input()))
    n = int(input())
    if n == 0:
        list_str = sys.stdin.readline()
        num_l = []
    else:
        num_l = list(map(int, input().lstrip('[').rstrip(']').split(',')))

    fORb = True
    check = 0
    s = 0
    e = 0

    for i in p:
        if i == 'R':
            fORb = not fORb
        if i == 'D':
            if n > s + e:
                if fORb:
                    s += 1
                else:
                    e += 1
            else:
                print('error')
                check = 1
                break

    if n > s + e:
        if fORb:
            answer = ''
            for i in range(s, n - e):
                answer = answer + str(num_l[i]) + ','
            print('['+answer.rstrip(',')+']')
        else:
            answer = ''
            for i in range(n - e - 1, s - 1, -1):
                answer = answer + str(num_l[i]) + ','
            print('[' + answer.rstrip(',') + ']')
    elif check == 0:
        print('[]')