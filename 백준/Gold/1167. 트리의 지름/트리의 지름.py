def dfs(s, dist):
    for go, dis in tree[s]:
        temp = dist + dis
        if visited[go] == 0:
            visited[go] = temp
            dfs(go, temp)
    return


V = int(input())

tree = [[] for _ in range(V + 1)]
for _ in range(V):
    num_l = list(map(int, input().split()))

    for i in range(1, len(num_l) - 1, 2):
        tree[num_l[0]].append((num_l[i], num_l[i + 1]))

visited = [0] * (V + 1)
visited[1] = 0
dfs(1, 0)

start = 0
check = 0
for i in range(1, V + 1):
    if visited[i] > check:
        check = visited[i]
        start = i

visited = [0] * (V + 1)
visited[start] = 1
dfs(start, 0)

print(max(visited))