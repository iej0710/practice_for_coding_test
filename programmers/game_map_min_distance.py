from collections import deque


def bfs(table, x, y):
    delta_x = [1, -1, 0, 0]
    delta_y = [0, 0, 1, -1]

    visit = [[0] * len(table[0]) for i in range(len(table))]
    visit[x][y] = 1

    que = deque()
    que.append([x, y, 0])
    min_move = float('inf')
    while len(que) > 0:
        x, y, move = que.popleft()
        if x == len(table) - 1 and y == len(table[0]) - 1:
            min_move = min(min_move, move)
        elif min_move > move:
            for dx, dy in zip(delta_x, delta_y):
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(table) and 0 <= ny < len(table[0]) and table[nx][ny] == 1 and visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    que.append([nx, ny, move + 1])
    if min_move < float('inf'):
        return min_move + 1
    else:
        return -1


def solution(maps):
    return bfs(maps, 0, 0)