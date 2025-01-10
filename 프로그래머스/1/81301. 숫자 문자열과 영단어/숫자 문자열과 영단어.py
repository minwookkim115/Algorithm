def solution(s):
    answer = ''

    check = 'zotfsen'

    i = 0
    while True:
        if i >= len(s):
            break

        if s[i] in check:
            
            if s[i] == 'z':
                i += 4
                answer += '0'
            elif s[i] == 'o':
                i += 3
                answer += '1'
            elif s[i] == 't':
                if s[i + 1] == 'w':
                    i += 3
                    answer += '2'
                else:
                    i += 5
                    answer += '3'
            elif s[i] == 'f':
                if s[i + 1] == 'o':
                    i += 4
                    answer += '4'
                else:
                    i += 4
                    answer += '5'
            elif s[i] == 's':
                if s[i + 1] == 'i':
                    i += 3
                    answer += '6'
                else:
                    i += 5
                    answer += '7'
            elif s[i] == 'e':
                i += 5
                answer += '8'
            elif s[i] == 'n':
                i += 4
                answer += '9'
        else:
            answer += s[i]
            i += 1

    return int(answer)