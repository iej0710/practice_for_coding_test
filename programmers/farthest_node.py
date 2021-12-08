def floyd_warshall(table, maxlen):
    for k in range(1, len(table)):
        for j in range(len(table)):
            if k != j:
                table[0][j] = min(table[0][j], table[0][k] + table[k][j])
                if table[0][j] < float('inf'):
                    maxlen = max(maxlen, table[0][j])
    return maxlen


def solution(n, edge):
    answer = 0
    table = [[float('inf')] * n for i in range(n)]
    for src, dst in edge:
        table[src - 1][dst - 1] = 1
        table[dst - 1][src - 1] = 1

    maxlen = floyd_warshall(table, 0)
    for i in range(1, n):
        if table[0][i] == maxlen:
            answer += 1

    return answer

