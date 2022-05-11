from collections import deque


def solution(triangle):
    delta_x = [1, 1]
    delta_y = [0, 1]
    res = [[0] * (i + 1) for i in range(len(triangle))]
    res[0][0] = triangle[0][0]
    max_cost = 0

    for x in range(len(triangle) - 1):
        for y in range(len(triangle[x])):
            for dx, dy in zip(delta_x, delta_y):
                nx, ny = x + dx, y + dy
                if nx < len(triangle) and ny <= nx:
                    res[nx][ny] = max(res[nx][ny], res[x][y] + triangle[nx][ny])

    return max(res[-1])