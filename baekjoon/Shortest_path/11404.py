import sys

n = int(input())
m = int(input())

g = [[float('inf')] * n for i in range(n)]

for e in range(m):
    s, d, w = map(int, sys.stdin.readline().rstrip().split())
    g[s - 1][d - 1] = min(g[s - 1][d - 1], w)

for k in range(n):
    for i in range(n):
        if i != k:
            for j in range(n):
                if j != i and j != k:
                    g[i][j] = min(g[i][j], g[i][k] + g[k][j])

for i in range(n):
    for j in range(n):
        if g[i][j] < sys.maxsize:
            print(g[i][j], end=' ')
        else:
            print(0, end=' ')
    print()
