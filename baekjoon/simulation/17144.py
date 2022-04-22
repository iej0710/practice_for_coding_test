from collections import deque

def diffuse(table, dust):
    delta_x = [1, -1, 0, 0]
    delta_y = [0, 0, 1, -1]

    while len(dust) > 0:
        x, y, w = dust.popleft()
        diffuse_count = 0
        diffuse_amount = w // 5
        for dx, dy in zip(delta_x, delta_y):
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(table) and 0 <= ny < len(table[0]) and table[nx][ny] != -1:
                table[nx][ny] += diffuse_amount
                diffuse_count += 1
        table[x][y] -= diffuse_amount * diffuse_count

    '''for r in range(len(table)):
        for c in range(len(table[r])):
            if table[r][c] > 0 and check[r][c] > 0:
                diffuse_count = 0
                diffuse_amount = check[r][c] // 5
                for dx, dy in zip(delta_x, delta_y):
                    nx, ny = r + dx, c + dy
                    if 0 <= nx < len(table) and 0 <= ny < len(table[r]) and table[nx][ny] != -1:
                        table[nx][ny] += diffuse_amount
                        diffuse_count += 1
                table[r][c] -= diffuse_count * diffuse_amount'''

def clearing(table, pos):
    delta = [[[0, 1], [-1, 0], [0, -1], [1, 0]],
             [[0, 1], [1, 0], [0, -1], [-1, 0]]]
    #start = [[[pos[0][0], 0], [pos[0][0], len(table[0]) - 1], [0, len(table[0]) - 1], [0, 0]],
    #         [[len(table) - 1, 0], [len(table) - 1, len(table[0]) - 1], [pos[1][0], len(table[0]) - 1], [pos[1][0], 0]]]

    for idx in range(len(pos)):
        d_idx = 0
        row, col = pos[idx]
        tmp = 0
        while d_idx < 4:
            if 0 <= row + delta[idx][d_idx][0] < len(table) and 0 <= col + delta[idx][d_idx][1] < len(table[0]):
                if table[row][col] != -1:
                    table[row][col], tmp = tmp, table[row][col]
                row, col = row + delta[idx][d_idx][0], col + delta[idx][d_idx][1]
            else:
                d_idx += 1
            if row == pos[idx][0] and col == pos[idx][1]:
                break

def print_map(table):
    for i in table:
        print(i)
    print()


R, C, T = map(int, input().split())
room = []
dust = deque()
air_conditioner = []
for r in range(R):
    tmp = list(map(int, input().split()))
    for c in range(C):
        if tmp[c] == -1:
            air_conditioner.append([r, c])
        elif tmp[c] > 4:
            dust.append([r, c, tmp[c]])
    room.append(tmp)

for t in range(T):
    diffuse(room, dust)
    clearing(room, air_conditioner)
    for r in range(R):
        for c in range(C):
            if room[r][c] > 4:
                dust.append([r, c, room[r][c]])


print(sum([sum(room[i]) for i in range(len(room))]) + 2)