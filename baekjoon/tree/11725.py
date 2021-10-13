from collections import deque
n = int(input())

tree = {i:[] for i in range(1,n+1)}
for i in range(n-1):
    e = list(map(int,input().split()))
    tree[e[0]].append(e[1])
    tree[e[1]].append(e[0])

ans = [1 for i in range(len(tree.keys()))]

start = 1
neighbor = deque([1])
visited = set()
while len(neighbor) > 0:
    node = neighbor.popleft()
    visited.add(node)
    for v in tree[node]:
        if v not in visited:
            neighbor.append(v)
            visited.add(v)
            ans[v-1] = node

for i in ans[1:]:
    print(i)
