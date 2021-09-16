from collections import deque

n, m = map(int,input().split())

mat = []
for y in range(n):
    mat.append(list(map(int,input())))

visited = [[[0 for i in range(m)] for j in range(n)] for k in range(2)]
process = deque([[0,0,1]])
flag = 0
delta_x = [1, -1, 0, 0]
delta_y = [0, 0, 1, -1]
visited[1][0][0] = 1
while len(process) > 0:
    print(process)
    y,x,count = process.popleft()
    if x == m - 1 and y == n - 1:
        flag = 1
        break
    for dx,dy in zip(delta_x,delta_y):
        idx = x + dx
        idy = y + dy
        if 0 <= idx < m and 0 <= idy < n:
            if mat[idy][idx] == 1 and count == 1:
                visited[0][idy][idx] = visited[1][y][x] + 1
                process.append([idy,idx,0])
            elif mat[idy][idx] == 0 and visited[count][idy][idx] == 0:
                visited[count][idy][idx] = visited[count][y][x] + 1
                process.append([idy,idx,count])

if flag == 0:
    print(-1)