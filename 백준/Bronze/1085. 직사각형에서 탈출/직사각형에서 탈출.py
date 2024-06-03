x, y, w, h = map(int, input().split())

answer = 1000

if x <= answer:
    answer = x

if y <= answer:
    answer = y

if w - x <= answer:
    answer = w - x

if h - y <= answer:
    answer = h - y

print(answer)