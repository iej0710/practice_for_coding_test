from collections import deque
import sys

def bfs(g, src):
    visit = [0] * len(g)
    que = deque()
    que.append(src)
    visit[src] = 1
    while len(que) > 0:
        v = que.popleft()

        for neighbor in g[v]:
            if visit[neighbor] == 0:
                que.append(neighbor)
                visit[neighbor] = 1

    return sum(visit)

n = int(input())
num_edge = int(input())

g = {i:[] for i in range(n)}
for e in range(num_edge):
    u, v = map(int, sys.stdin.readline().rstrip().split())

    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)

print(bfs(g, 0))