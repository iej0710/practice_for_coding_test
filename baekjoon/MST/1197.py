def find(arr, x):
    if arr[x] == x:
        return x
    else:
        arr[x] = find(arr, arr[x])
        return arr[x]

def union(arr, x, y):
    px = find(arr, x)
    py = find(arr, y)

    if px > py:
        arr[px] = py
    else:
        arr[py] = px

V, E = map(int, input().split())

group = [i for i in range(V + 1)]
g = []
for i in range(E):
    g.append(list(map(int, input().split())))

g = sorted(g, key= lambda x: x[2])
count = 0
res = 0
for u, v, w in g:
    if find(group, u) != find(group, v):
        union(group, u, v)
        res += w
        count += 1

    if count == V - 1:
        break
print(res)
