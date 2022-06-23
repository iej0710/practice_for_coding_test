from collections import deque
from itertools import combinations

a, b, c = map(int, input().split())

que = deque()
que.append([min([a, b, c]), max([a, b, c])])
total = a + b + c

if a == b and b == c:
    print(1)
elif (a + b + c) % 3 != 0:
    print(0)
else:
    flag = 0
    visit = [[0] * (total + 1) for i in range(total * 2 + 1)]
    while len(que) > 0:
        pa, pc = que.popleft()
        pb = total - pa - pc
        if pa == pb and pb == pc:
            flag = 1
            break
        else:
            for x, y in combinations([pa, pb, pc], 2):
                if x > y:
                    x -= y
                    y *= 2
                else:
                    y -= x
                    x *= 2
                nx = min([x, y, total - x - y])
                ny = max([x, y, total - x - y])
                if visit[nx][ny] == 0:
                    que.append([nx, ny])
                    visit[nx][ny] = 1
    print(flag)