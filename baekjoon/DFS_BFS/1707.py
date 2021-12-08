import sys
from collections import deque
def dfs(g, s, visited, ans, color):
    visited[s] = color
    for neighbor in g[s]:
        if visited[neighbor] == 0:
            ans = dfs(g, neighbor, visited, ans, -color)
            if ans is False:
                return ans
        elif visited[neighbor] == visited[s]:
            return False
    return ans

def bfs(g, s, visited):
    color = 1
    queue = deque()
    queue.append([s, color])
    while len(queue) > 0:
        v, color = queue.popleft()

        visited[v] = color
        for neighbor in g[v]:
            if visited[neighbor] == 0:
                queue.append([neighbor, -color])
            elif visited[neighbor] == visited[v]:
                return False
    return True

T = int(sys.stdin.readline())

for test in range(T):
    v, e = map(int, sys.stdin.readline().rstrip().split())

    g = [[] for i in range(v + 1)]
    for i in range(e):
        src, dst = map(int, sys.stdin.readline().rstrip().split())
        g[src].append(dst)
        g[dst].append(src)

    visited = [0] * (v + 1)
    ans = True
    for src in range(1, v + 1):
        if visited[src] == 0:
            #ans = dfs(g, src, visited, ans, 1)
            ans = bfs(g, src, visited)
            if ans is False:
                break
    if ans is True:
        print('YES')
    else:
        print('NO')