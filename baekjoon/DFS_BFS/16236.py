from collections import deque
def print_map(mat):
    for i in mat:
        print(i)
    print()

def nearest_fish(g, src, size):
    t = 0
    que = deque()
    que.append([src, t])
    delta_x = [1, -1, 0, 0]
    delta_y = [0, 0, 1, -1]
    min_t = float('inf')
    res_pos = src
    visited = [[0] * len(g) for i in range(len(g))]
    visited[src[0]][src[1]] = 1
    while len(que) > 0:
        pos, t = que.popleft()
        if 0 < g[pos[0]][pos[1]] < size and min_t >= t:
            min_t = t
            if res_pos[0] == src[0] and res_pos[1] == src[1]:
                res_pos = pos
            else:
                if res_pos[0] > pos[0]:
                    res_pos = pos
                elif res_pos[0] == pos[0] and res_pos[1] > pos[1]:
                    res_pos = pos

        elif min_t < t:
            continue
        else:
            for dx, dy in zip(delta_x, delta_y):
                nx, ny = pos[0] + dx, pos[1] + dy
                if 0 <= nx < len(g) and 0 <= ny < len(g):
                    if g[nx][ny] <= size and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        que.append([[nx, ny], t + 1])
    return res_pos, min_t


n = int(input())
space = []
baby = []
fish = 0
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        if tmp[j] == 9:
            baby = [i, j]
            tmp[j] = 0
            break
    space.append(tmp)

cand = deque()
cand.append([2, baby, 0, 0])
res = 0
while len(cand) > 0:
    size, pos, count, t = cand.popleft()

    n_pos, time = nearest_fish(space, pos, size)
    if n_pos[0] == pos[0] and n_pos[1] == pos[1]:
        res = t
        break
    else:
        count += 1
        space[n_pos[0]][n_pos[1]] = 0
        if count == size:
            size += 1
            count = 0
        cand.append([size, n_pos, count, t + time])
    #print_map(space)

print(res)