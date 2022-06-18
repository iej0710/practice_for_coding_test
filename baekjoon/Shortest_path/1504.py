import sys
import heapq

def dijkstra(g, src, dst):
    que = []
    cost = [float('inf')] * (len(g) + 1)
    cost[src] = 0
    heapq.heappush(que, [0, src])

    while len(que) > 0:
        w, v = heapq.heappop(que)
        if v == dst:
            continue
        for u, weight in g[v]:
            if cost[u] > cost[v] + weight:
                cost[u] = cost[v] + weight
                heapq.heappush(que, [cost[u], u])

    return cost[dst]

V, E = map(int, input().split())
g = {v + 1: [] for v in range(V)}

for e in range(E):
    u, v, w = map(int, sys.stdin.readline().rstrip().split())
    try:
        g[u].append([v, w])
    except:
        g[u] = [[v, w]]
    try:
        g[v].append([u, w])
    except:
        g[v] = [[u, w]]

v1, v2 = map(int, input().split())

v1_cost = dijkstra(g, 1, v1)
v2_cost = dijkstra(g, 1, v2)
intermediate_cost = dijkstra(g, v1, v2)
l_cost1 = dijkstra(g, v2, V)
l_cost2 = dijkstra(g, v1, V)

if float('inf') in [v1_cost, v2_cost, intermediate_cost, l_cost1, l_cost2]:
    print(-1)
else:
    print(intermediate_cost + min(v1_cost + l_cost1, v2_cost + l_cost2))