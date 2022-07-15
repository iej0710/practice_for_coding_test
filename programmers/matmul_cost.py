def solution(matrix_sizes):
    answer = 0

    dp = [[float('inf')] * (len(matrix_sizes) + 1) for i in range(len(matrix_sizes) + 1)]
    for i in range(1, len(dp)):
        dp[i][0] = matrix_sizes[i - 1][0]
        dp[0][i] = matrix_sizes[i - 1][1]

    for i in range(1, len(dp) - 1):
        dp[i][i + 1] = dp[i][0] * dp[0][i] * dp[0][i + 1]
        dp[i][i] = 0
    dp[0][0], dp[-1][-1] = 0, 0

    for d in range(1, len(dp)):
        for i in range(1, len(dp) - d - 1):
            j = d + i + 1
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + dp[i][0] * dp[0][k] * dp[0][j])

    return dp[1][-1]