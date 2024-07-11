def remove_node(node, tree):
    tree[node] = -2
    for i in range(N):
        if node == tree[i]:
            remove_node(i, tree)


N = int(input())
arr = list(map(int, input().split()))
remove = int(input())

remove_node(remove, arr)
answer = 0
for i in range(N):
    if arr[i] != -2 and i not in arr:
        answer += 1

print(answer)