from collections import deque
import sys
import copy

def print_map(A):
    for i in range(len(A)):
        print(A[i])
    print()

n, m = map(int, sys.stdin.readline().rstrip().split())

table = []
pos = {}
visit = [[[[0] * m for i in range(n)] for j in range(m)] for k in range(n)]
for i in range(n):
    tmp = sys.stdin.readline().rstrip()
    for j in range(m):
        if tmp[j] == 'R':
            pos['R'] = [i, j]
        elif tmp[j] == 'B':
            pos['B'] = [i, j]
        elif tmp[j] == 'O':
            pos['O'] = [i, j]
    table.append(tmp)

cand = deque()
cand.append([pos['R'], pos['B'], 0])
visit[pos['R'][0]][pos['R'][1]][pos['B'][0]][pos['B'][1]] = 1

delta_x = [1, -1, 0, 0]
delta_y = [0, 0, 1, -1]
min_count = 11
while len(cand) > 0:
    r_pos, b_pos, count = cand.popleft()
    if count > 10:
        continue
    for dx, dy in zip(delta_x, delta_y):
        nx_r_pos, ny_r_pos = r_pos
        nx_b_pos, ny_b_pos = b_pos
        r_move, b_move = 0, 0
        while table[nx_r_pos + dx][ny_r_pos + dy] != '#' and (nx_r_pos != pos['O'][0] or ny_r_pos != pos['O'][1]):
            nx_r_pos += dx
            ny_r_pos += dy
            r_move += 1
        while table[nx_b_pos + dx][ny_b_pos + dy] != '#' and (nx_b_pos != pos['O'][0] or ny_b_pos != pos['O'][1]):
            nx_b_pos += dx
            ny_b_pos += dy
            b_move += 1

        if nx_b_pos == pos['O'][0] and ny_b_pos == pos['O'][1]:
            continue
        if nx_r_pos == pos['O'][0] and ny_r_pos == pos['O'][1]:
            min_count = min(min_count, count + 1)
            continue
        if nx_r_pos == nx_b_pos and ny_r_pos == ny_b_pos:
            if r_move > b_move:
                nx_r_pos -= dx
                ny_r_pos -= dy
            else:
                nx_b_pos -= dx
                ny_b_pos -= dy
        if visit[nx_r_pos][ny_r_pos][nx_b_pos][ny_b_pos] == 0:
            visit[nx_r_pos][ny_r_pos][nx_b_pos][ny_b_pos] = 1
            cand.append([[nx_r_pos, ny_r_pos], [nx_b_pos, ny_b_pos], count + 1])

if min_count == 11:
    print(-1)
else:
    print(min_count)



'''n, m = map(int, sys.stdin.readline().rstrip().split())

table = [[0] * m for i in range(n)]
r_pos = [0, 0]
b_pos = [0, 0]
target = [0, 0]
for i in range(n):
    tmp = list(sys.stdin.readline().rstrip())
    for j in range(m):
        if tmp[j] == '#':
            table[i][j] = 1
        elif tmp[j] == '.':
            table[i][j] = 0
        elif tmp[j] == 'R':
            r_pos = [i, j]
            table[i][j] = 0
        elif tmp[j] == 'B':
            b_pos = [i, j]
            table[i][j] = 0
        elif tmp[j] == 'O':
            target = [i, j]

cand = deque()
cand.append([r_pos, b_pos, 0])
delta_x = [1, -1, 0, 0]
delta_y = [0, 0, 1, -1]
visit = [[[[0] * m for i in range(n)] for j in range(m)] for k in range(n)]
visit[r_pos[0]][r_pos[1]][b_pos[0]][b_pos[1]] = 1
min_count = 11
while len(cand) > 0:
    r_pos, b_pos, count = cand.popleft()
    if count > 10:
        continue
    for dx, dy in zip(delta_x, delta_y):
        nrx, nry = r_pos
        nbx, nby = b_pos
        r_move, b_move = 0, 0
        while table[nrx + dx][nry + dy] != 1 and table[nrx][nry] != 1:
            nrx += dx
            nry += dy
            r_move += 1

        while table[nbx + dx][nby + dy] != 1 and table[nbx][nby] != 1:
            nbx += dx
            nby += dy
            b_move += 1

        if nbx == target[0] and nby == target[1]:
            continue
        if nrx == target[0] and nry == target[1]:
            min_count = min(min_count, count + 1)
            continue
        if nrx == nbx and nry == nby:
            if r_move > b_move:
                nrx -= dx
                nry -= dy
            else:
                nbx -= dx
                nby -= dy
                
        if visit[nrx][nry][nbx][nby] == 0:
            visit[nrx][nry][nbx][nby] = 1
            cand.append([[nrx, nry], [nbx, nby], count + 1])


        #print_map(visit)
if min_count == 11:
    print(-1)
else:
    print(min_count)'''