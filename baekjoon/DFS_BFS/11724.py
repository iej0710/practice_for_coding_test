import sys
sys.setrecursionlimit(10**6)
def dfs(g, src, visited):
    if sum(visited) == len(g):
        return
    visited[src] = 1
    for neighbor in g[src]:
        if visited[neighbor] == 0:
            visited[neighbor] = 1
            dfs(g, neighbor, visited)




n, m = map(int, input().split())

visit = [0] * n
g = {i: [] for i in range(n)}
for e in range(m):
    edge = list(map(int, sys.stdin.readline().rstrip().split()))
    g[edge[0] - 1].append(edge[1] - 1)
    g[edge[1] - 1].append(edge[0] - 1)
ans = 0
for v in range(n):
    if visit[v] == 0:
        dfs(g, v, visit)
        ans += 1

print(ans)