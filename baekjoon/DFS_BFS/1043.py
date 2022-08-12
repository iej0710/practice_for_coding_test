import sys
from collections import deque

def bfs(g, src, visit):
    que = deque()
    que.append(src)
    visit[src] = 1
    while len(que) > 0:
        v = que.popleft()

        for neighbor in range(len(g[v])):
            if g[v][neighbor] == 1 and visit[neighbor] == 0:
                que.append(neighbor)
                visit[neighbor] = 1

n, m = map(int, input().split())

n_truth, *truth = map(int, sys.stdin.readline().rstrip().split())

g = [[0] * n for i in range(n)]
party = []
for i in range(m):
    p_num, *pid = map(int, sys.stdin.readline().rstrip().split())
    party.append(pid)
    for p1 in range(len(pid)):
        for p2 in range(p1, len(pid)):
            g[pid[p1] - 1][pid[p2] - 1] = 1
            g[pid[p2] - 1][pid[p1] - 1] = 1

if n_truth == 0:
    print(m)
else:
    know = [0] * n
    for v in truth:
        bfs(g, v - 1, know)
    res = [1] * m
    for i in range(m):
        for p in party[i]:
            if know[p - 1] == 1:
                res[i] = 0
                break
    print(sum(res))