import sys
from collections import deque

def bfs(g, src, visit):
    if sum(visit) == len(g):
        return 0
    que = deque()
    que.append([src, 1])

    while len(que) > 0:
        v, depth = que.popleft()
        if depth > 3:
            continue
        visit[v] = 1
        for neighbor in g[v]:
            if visit[neighbor] == 0:
                que.append([neighbor, depth + 1])


n = int(input())
m = int(input())

g = {i: [] for i in range(n)}
visit = [0] * n

for i in range(m):
    src, dst = map(int, sys.stdin.readline().rstrip().split())
    g[src - 1].append(dst - 1)
    g[dst - 1].append(src - 1)

visit[0] = 1
bfs(g, 0, visit)

print(sum(visit) - 1)