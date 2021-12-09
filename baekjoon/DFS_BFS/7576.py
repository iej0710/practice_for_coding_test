import sys
from collections import deque
def show(map):
    for i in map:
        print(i)

def bfs(map, src, visited):
    global count, empty
    delta_x = [1, -1, 0, 0]
    delta_y = [0, 0, 1, -1]
    queue = deque([src])
    res = 0
    while len(queue) > 0:
        tomato = queue.popleft()
        tmp = deque()
        res += 1

        for x, y in tomato:
            if visited[x][y] == 1:
                continue

            visited[x][y] = 1
            for dx, dy in zip(delta_x, delta_y):
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(map) and 0 <= ny < len(map[0]):
                    if map[nx][ny] == 0 and visited[nx][ny] == 0:
                        map[nx][ny] = 1
                        count += 1
                        tmp.append([nx, ny])

        if len(tmp) > 0:
            queue.append(tmp)
        if count + empty == len(map) * len(map[0]):
            break
        #print(res, count, empty, tomato)
        #show(map)
    return res

m, n = map(int, input().split())

status = []
tomato = []
count = 0
empty = 0
visited = [[0] * m for i in range(n)]
for i in range(n):
    status.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(m):
        if status[i][j] == 1:
            tomato.append([i, j])
            count += 1
        elif status[i][j] == -1:
            empty += 1

if count + empty == m * n:
    print(0)
else:
    ans = bfs(status, tomato, visited)
    if count + empty == m * n:
        print(ans)
    else:
        print(-1)