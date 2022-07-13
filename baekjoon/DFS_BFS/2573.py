from collections import deque
import sys


def year_after(table):
    delta_x = [1, -1, 0, 0]
    delta_y = [0, 0, 1, -1]
    res = [[0] * len(table[0]) for i in range(len(table))]
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] > 0:
                count = 0
                for dx, dy in zip(delta_x, delta_y):
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < len(table) and 0 <= ny < len(table[i]) and table[nx][ny] == 0:
                        count += 1
                res[i][j] = max(0, table[i][j] - count)
    return res

def count_ice(table, x, y, visit):
    delta_x = [1, -1, 0, 0]
    delta_y = [0, 0, 1, -1]

    que = deque()
    que.append([x, y])
    visit[x][y] = 1
    while len(que) > 0:
        x, y = que.popleft()

        for dx, dy in zip(delta_x, delta_y):
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(table) and 0 <= ny < len(table[0]) and visit[nx][ny] == 0 and table[nx][ny] > 0:
                que.append([nx, ny])
                visit[nx][ny] = 1
    return 1

n, m = map(int, input().split())
ice = []
for i in range(n):
    ice.append(list(map(int, sys.stdin.readline().rstrip().split())))

count = 1
year = 0
while count == 1:
    ice = year_after(ice)
    year += 1
    visit = [[0] * m for i in range(n)]
    count = 0
    for i in range(len(ice)):
        for j in range(len(ice[i])):
            if ice[i][j] > 0 and visit[i][j] == 0:
                count += count_ice(ice, i, j, visit)

if count == 0:
    print(0)
else:
    print(year)

