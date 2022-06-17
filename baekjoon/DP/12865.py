import sys

N, K = map(int, input().split())
goods = []

for i in range(N):
    goods.append(list(map(int, sys.stdin.readline().rstrip().split())))

res = [[0] * (K + 1) for i in range(N + 1)]

for idx in range(1, N + 1):
    for weight in range(1, K + 1):
        if goods[idx - 1][0] > weight:
            res[idx][weight] = res[idx - 1][weight]
        else:
            res[idx][weight] = max(res[idx - 1][weight], res[idx - 1][weight - goods[idx - 1][0]] + goods[idx - 1][1])

print(res[N][K])