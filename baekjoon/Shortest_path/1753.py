import sys
import heapq
def dijkstra(g, s):
    visited = [0] * len(g)
    cost = [sys.maxsize] * len(g)
    cost[s] = 0
    queue = []
    heapq.heappush(queue, [cost[s], s])
    while len(queue) > 0:
        cost_tmp, src = heapq.heappop(queue)
        visited[src] = 1
        for neighbor in g[src]:
            if visited[neighbor] == 0 and cost[neighbor] > cost[src] + g[src][neighbor]:
                cost[neighbor] = cost[src] + g[src][neighbor]
                heapq.heappush(queue,[cost[neighbor], neighbor])

    return cost

V, E = map(int, input().split())
start = int(input()) - 1
g = {i: {} for i in range(V)}

for e in range(E):
    src, dst, w = map(int, sys.stdin.readline().rstrip().split())
    try:
        g[src - 1][dst - 1] = min(g[src - 1][dst - 1], w)
    except: g[src - 1][dst - 1] = w

res = dijkstra(g, start)
for i in res:
    if i == sys.maxsize:
        print('INF')
    else:
        print(i)