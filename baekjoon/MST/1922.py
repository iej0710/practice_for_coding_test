# https://www.acmicpc.net/problem/1922
import sys

def find(seq, x):
    if seq[x] == x:
        return x
    else:
        seq[x] = find(seq, seq[x])
        return seq[x]

def union(seq, x, y):
    parent_x = find(seq, x)
    parent_y = find(seq, y)

    if parent_x <= parent_y:
        seq[parent_y] = parent_x
    else:
        seq[parent_x] = parent_y

n = int(input())
m = int(input())

link = []
for e in range(m):
    link.append(list(map(int, sys.stdin.readline().rstrip().split())))

link.sort(key=lambda x: x[2])

visit = [i for i in range(n + 1)]
min_cost = 0
edge = []

for src, dst, w in link:
    if find(visit, src) != find(visit, dst):
        union(visit, src, dst)
        min_cost += w
        edge.append([src, dst])
    if sum(visit) == n:
        break

print(min_cost)