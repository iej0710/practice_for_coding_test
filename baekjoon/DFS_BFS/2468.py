import sys
from collections import deque

def print_map(A):
    for i in A:
        print(i)
    print()

def sink(g, h, state):#bfs(g, src, h, state):
    for i in range(len(g)):
        for j in range(len(g)):
            if g[i][j] <= h and state[i][j] == 0:
                state[i][j] = 1

def check_area(g, src, state, visit):
    delta_x, delta_y = [1, -1, 0, 0], [0, 0, 1, -1]

    que = deque()
    que.append(src)

    while len(que) > 0:
        x, y = que.popleft()
        for dx, dy in zip(delta_x, delta_y):
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(g) and 0 <= ny < len(g) and state[nx][ny] == 0 and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                que.append([nx, ny])


n = int(input())
mapping = []
#height = set()
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    mapping.append(tmp)
    #height.update(tmp)
max_h = max(max(mapping[i]) for i in range(n))
height = [i for i in range(max_h)]#sorted(list(height))
state = [[0] * n for i in range(n)]

max_area = 0
for h in height:
    sink(mapping, h, state)
    visit = [[0] * n for i in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if state[i][j] == 0 and visit[i][j] == 0:
                visit[i][j] = 1
                check_area(mapping, [i,j], state, visit)
                count += 1

    max_area = max(max_area, count)

print(max_area)
