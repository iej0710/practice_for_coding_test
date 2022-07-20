def solution(n, s, a, b, fares):
    answer = 0
    table = [[float('inf')] * n for i in range(n)]

    for src, dst, w in fares:
        table[src - 1][dst - 1] = w
        table[dst - 1][src - 1] = w

    for k in range(n):
        table[k][k] = 0
        for i in range(n):
            if i != k:
                for j in range(i + 1, n):
                    if j != k:
                        table[i][j] = min(table[i][j], table[i][k] + table[k][j])
                        table[j][i] = table[i][j]

    min_cost = float('inf')
    for i in range(1, n + 1):
        min_cost = min(min_cost, table[s - 1][i - 1] + table[i - 1][a - 1] + table[i - 1][b - 1])
    return min_cost