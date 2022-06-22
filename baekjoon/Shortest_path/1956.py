import sys

V, E = map(int, input().split())

g = [[float('inf')] * V for i in range(V)]

for _ in range(E):
    s, e, w = map(int, sys.stdin.readline().rstrip().split())
    g[s - 1][e - 1] = w

for i in range(V):
    for j in range(V):
        for k in range(V):
            if j != k and i != k:
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])

res = min([g[i][i] for i in range(V)])

if res == float('inf'):
    print(-1)
else:
    print(res)