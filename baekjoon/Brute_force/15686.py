import sys
from itertools import combinations

n, m = map(int, input().split())

table = []
chicken = []
house = []
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(n):
        if tmp[j] == 1:
            house.append([i, j])
        elif tmp[j] == 2:
            chicken.append([i, j])

c_index = [i for i in range(len(chicken))]
min_d = float('inf')

for run in combinations(c_index, m):
    city_d = 0
    for hx, hy in house:
        d = float('inf')
        for each_chicken in run:
            d = min(d, abs(hx - chicken[each_chicken][0]) + abs(hy - chicken[each_chicken][1]))
        city_d += d
    min_d = min(min_d, city_d)

print(min_d)