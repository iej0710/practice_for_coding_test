def dfs(g, v):
    g[v] = len(g)

    for i in range(len(g)):
        if g[i] == v:
            dfs(g, i)

n = int(input())

arr = list(map(int, input().split()))
v = int(input())

dfs(arr, v)
count = 0
for i in range(n):
    if arr[i] != n and i not in arr:
        count += 1
print(count)