from collections import deque

def dfs(g,start,visited):
    if len(visited) == len(g):
        return None
    print(start,end=' ')
    visited.add(start)
    for v in sorted(g[start]):
        if v not in visited:
            dfs(g,v,visited)


def bfs(g,start,visited):
    visited.add(start)
    neighbor = deque([start])
    while len(neighbor) > 0:
        tmp = neighbor.popleft()
        print(tmp,end=' ')
        for v in sorted(g[tmp]):
            if v not in visited:
                neighbor.append(v)
                visited.add(v)
    return None

n, m, src = map(int,input().split())
graph = {i:[] for i in range(1,n+1)}

for i in range(m):
    e = list(map(int,input().split()))
    graph[e[0]].append(e[1])
    graph[e[1]].append(e[0])


dfs(graph,src,set())
print()
bfs(graph,src,set())