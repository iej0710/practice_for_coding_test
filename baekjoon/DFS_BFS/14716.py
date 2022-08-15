from collections import deque
import sys

def alphabet(table, pos, visit):
    delta_x = [-1, -1, -1, 0, 0, 1, 1, 1]
    delta_y = [-1, 0, 1, -1, 1, -1, 0, 1]

    que = deque()
    que.append(pos)

    while len(que) > 0:
        x, y = que.popleft()

        visit[x][y] = 1
        for dx, dy in zip(delta_x, delta_y):
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(table) and 0 <= ny < len(table[0]) and table[nx][ny] == 1 and visit[nx][ny] == 0:
                que.append([nx, ny])
                visit[nx][ny] = 1


m, n = map(int, input().split())

visit = [[0] * n for i in range(m)]
table = []

for i in range(m):
    table.append(list(map(int, sys.stdin.readline().rstrip().split())))

res = 0
for i in range(m):
    for j in range(n):
        if table[i][j] == 1 and visit[i][j] == 0:
            alphabet(table, [i, j], visit)
            res += 1

print(res)