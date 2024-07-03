N = int(input())
left_l = [0] * (N + 1)
right_l = [0] * (N + 1)
for _ in range(N):
    node, left, right = map(str, input().split())
    left_l[ord(node) - 64] = left
    right_l[ord(node) - 64] = right


def preorder(start):
    if start != ".":
        print(start, end="")
        preorder(left_l[ord(start) - 64])
        preorder(right_l[ord(start) - 64])


def inorder(start):
    if start != ".":
        inorder(left_l[ord(start) - 64])
        print(start, end="")
        inorder(right_l[ord(start) - 64])


def postorder(start):
    if start != ".":
        postorder(left_l[ord(start) - 64])
        postorder(right_l[ord(start) - 64])
        print(start, end="")


preorder('A')
print()
inorder('A')
print()
postorder('A')
