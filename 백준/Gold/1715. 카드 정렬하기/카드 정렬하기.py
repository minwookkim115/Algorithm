import heapq

N = int(input())

cards = []
for _ in range(N):
    heapq.heappush(cards, int(input()))

answer = 0
while len(cards) > 1:

    num1 = heapq.heappop(cards)
    num2 = heapq.heappop(cards)
    sum_v = num1 + num2

    answer += sum_v
    heapq.heappush(cards, sum_v)

print(answer)