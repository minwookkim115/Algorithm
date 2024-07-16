from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

chickens = []
homes = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            homes.append([i, j])
        elif city[i][j] == 2:
            chickens.append([i, j])

answer = 1000001
for chicken in combinations(chickens, M):
    temp = 0
    for home in homes:
        chicken_road = 1000001
        for i in range(M):
            chicken_road = min(chicken_road, abs(home[0] - chicken[i][0]) + abs(home[1] - chicken[i][1]))
        temp += chicken_road
    answer = min(answer, temp)

print(answer)