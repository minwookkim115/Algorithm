N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
check = []

def dfs(arr):

    if len(check) == M:
        print(*check)

    for i in range(N):
        if arr[i] not in check:
            check.append(arr[i])
        else:
            continue
        dfs(arr)
        check.pop()

dfs(arr)