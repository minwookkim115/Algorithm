N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
check = []


def dfs(s):
    if len(check) == M:
        print(*check)
        return

    temp = 0
    for i in range(s, N):
        if temp != arr[i]:
            check.append(arr[i])
            temp = arr[i]
            dfs(i)
            check.pop()


dfs(0)