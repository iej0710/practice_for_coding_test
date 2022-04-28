from collections import deque
import sys
input = sys.stdin.readline

def nearest_person(table, taxi, people, fuel, c):
    min_len = len(table) ** 2
    pos = [len(table), len(table)]
    delta_x = [1, -1, 0, 0]
    delta_y = [0, 0, 1, -1]
    idx = len(people)
    for i in range(len(people)):
        if c[i] == 1:
            continue
        min_d = len(table) ** 2
        cand = deque()
        cand.append([taxi, 0, fuel])
        visit = [[0] * len(table) for k in range(len(table))]
        while len(cand) > 0:
            t_pos, d, f = cand.popleft()
            if t_pos[0] == people[i][0] and t_pos[1] == people[i][1]:
                min_d = min(min_d, d)
            elif min_d < d:
                continue
            else:
                if fuel > 0:
                    for dx, dy in zip(delta_x, delta_y):
                        nx, ny = t_pos[0] + dx, t_pos[1] + dy
                        if 0 <= nx < len(table) and 0 <= ny < len(table):
                            if visit[nx][ny] == 0 and table[nx][ny] == 0:
                                visit[nx][ny] = 1
                                cand.append([[nx, ny], d + 1, f - 1])

        if min_len > min_d:
            min_len = min_d
            pos = people[i]
            idx = i
        elif min_len == min_d:
            if pos[0] > people[i][0]:
                pos = people[i]
                idx = i
            elif pos[0] == people[i][0] and pos[1] > people[i][1]:
                pos[1] = people[i][1]
                idx = i
    return min_len, idx

def drive(table, src, dst, fuel):
    delta_x = [1, -1, 0, 0]
    delta_y = [0, 0, 1, -1]
    min_d = len(table) ** 2
    cand = deque()
    cand.append([src, 0, fuel])
    visit = [[0] * len(table) for i in range(len(table))]
    while len(cand) > 0:
        pos, d, f = cand.popleft()
        if pos[0] == dst[0] and pos[1] == dst[1]:
            min_d = min(min_d, d)
        elif min_d < d:
            continue
        else:
            if f > 0:
                for dx, dy in zip(delta_x, delta_y):
                    nx, ny = pos[0] + dx, pos[1] + dy
                    if 0 <= nx < len(table) and 0 <= ny < len(table) and table[nx][ny] == 0 and visit[nx][ny] == 0:
                        visit[nx][ny] = 1
                        cand.append([[nx, ny], d + 1, f - 1])
    return min_d

n, m, init_fuel = map(int, input().split())
table = []
for i in range(n):
    table.append(list(map(int, input().split())))

x, y = map(int, input().split())
taxi = [x - 1, y - 1]

people = []
for i in range(m):
    tmp = list(map(int, input().split()))
    for i in range(len(tmp)):
        tmp[i] -= 1
    people.append(tmp)
flag = 1
check = [0] * len(people)
for i in range(m):
    distance, src = nearest_person(table, taxi, people, init_fuel, check)
    check[src] = 1
    if distance == len(table) ** 2:
        flag = 0
        break
    init_fuel -= distance
    use_fuel = drive(table, people[src][:2], people[src][2:], init_fuel)
    if use_fuel == len(table) ** 2:
        flag = 0
        break
    init_fuel += use_fuel
    taxi = people[src][2:]
    #del people[src]

if flag == 0:
    print(-1)
else:
    print(init_fuel)