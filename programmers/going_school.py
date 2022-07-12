def print_map(M):
    for i in range(len(M)):
        print(M[i])
    print()

def solution(m, n, puddles):
    answer = 0
    dp = [[0] * m for i in range(n)]
    for i in range(m):
        dp[0][i] = 1
    for i in range(n):
        dp[i][0] = 1
    for pos in puddles:
        y, x = pos[0] - 1, pos[1] - 1
        dp[x][y] = -1
        if x == 0:
            for i in range(y + 1, m):
                dp[0][i] = 0
        if y == 0:
            for i in range(x + 1, n):
                dp[i][0] = 0
    #print_map(dp)
    for i in range(1, n):
        for j in range(1, m):
            if dp[i][j] != -1:
                dp[i][j] = (max(0, dp[i - 1][j]) + max(0, dp[i][j - 1])) % (10 ** 9 + 7)
    #print_map(dp)
    answer = dp[-1][-1]
    return answer

solution(4, 3, [[2, 2]])