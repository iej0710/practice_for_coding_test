import sys
import math

N, L = map(int, input().split())

info = []
for i in range(N):
    info.append(list(map(int, sys.stdin.readline().rstrip().split())))

info.sort(key=lambda x: x[1])

tmp = 0
res = 0
p_src, p_dst = 0, 0
for i in range(N):
    src, dst = info[i]

    if p_dst >= src:
        p_dst = dst
    else:
        res += math.ceil((p_dst - max(p_src, tmp)) / L)
        tmp = max(p_src, tmp) + math.ceil((p_dst - max(p_src, tmp)) / L) * L
        p_src, p_dst = src, dst

if p_dst > tmp:
    res += math.ceil((p_dst - max(p_src, tmp)) / L)

print(res)