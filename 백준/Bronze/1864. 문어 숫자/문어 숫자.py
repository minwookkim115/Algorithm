while True:
    string = input()

    if string == "#":
        break

    answer = 0
    for i in range(len(string)):
        if string[i] == '-':
            answer += 0 * 8 ** (len(string) - i - 1)
        elif string[i] == "\\":
            answer += 1 * 8 ** (len(string) - i - 1)
        elif string[i] == "(":
            answer += 2 * 8 ** (len(string) - i - 1)
        elif string[i] == "@":
            answer += 3 * 8 ** (len(string) - i - 1)
        elif string[i] == "?":
            answer += 4 * 8 ** (len(string) - i - 1)
        elif string[i] == ">":
            answer += 5 * 8 ** (len(string) - i - 1)
        elif string[i] == "&":
            answer += 6 * 8 ** (len(string) - i - 1)
        elif string[i] == "%":
            answer += 7 * 8 ** (len(string) - i - 1)
        elif string[i] == "/":
            answer += -1 * 8 ** (len(string) - i - 1)

    print(answer)