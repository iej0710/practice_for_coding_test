import sys

def find(cities, x):
    if cities[x] == x:
        return x
    else:
        cities[x] = find(cities, cities[x])
        return cities[x]

def union(cities, x, y):
    x_root = find(cities, x)
    y_root = find(cities, y)

    if x_root >= y_root:
        cities[x_root] = y_root
    else:
        cities[y_root] = x_root

n = int(input())
m = int(input())

mapping = []
city_set = [i for i in range(n)]

for i in range(n):
    mapping.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(n):
        if mapping[i][j] == 1 and j > i:
            union(city_set, i, j)

city = list(map(int, sys.stdin.readline().rstrip().split()))
flag = 1
src = find(city_set, city[0] - 1)
for i in range(1, len(city)):
    if find(city_set, city[i] - 1) != src:
        flag = 0
        break

if flag == 1:
    print('YES')
else:
    print('NO')

