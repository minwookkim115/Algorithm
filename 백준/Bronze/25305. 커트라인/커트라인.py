import sys

N, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
print(arr[N - k])