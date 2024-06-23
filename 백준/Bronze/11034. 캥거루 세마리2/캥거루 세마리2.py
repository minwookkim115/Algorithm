while True:
    try:
        a, b, c = map(int, input().split())

        check1 = abs(a - b)
        check2 = abs(b - c)

        print(max(check1, check2) - 1)
    except:
        exit()