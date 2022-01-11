import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

g = []

for e in range(m):
    s, d, w = map(int, sys.stdin.readline().rstrip().split())
    g.append([s - 1, d - 1, w])

res = [sys.maxsize] * n
res[0] = 0
flag = True
for i in range(n):
    for j in range(m):
        if res[g[j][0]] < sys.maxsize:
            if i == n - 1 and res[g[j][1]] > res[g[j][0]] + g[j][2]:
                flag = False
            res[g[j][1]] = min(res[g[j][1]], res[g[j][0]] + g[j][2])



if flag is True:
    for i in range(1, n):
        if res[i] < sys.maxsize:
            print(res[i])
        else:
            print(-1)
else:
    print(-1)