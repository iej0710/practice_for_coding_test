def fibo_mat_mul(A, n):
    if n == 1:
        return A
    res = fibo_mat_mul(mat_mul(A, A), n // 2)
    if n % 2 == 1:
        res = mat_mul(res, A)
    return res

def mat_mul(A, B):
    res = [[0] * len(A) for i in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                res[i][j] += A[i][k] * B[k][j]
            res[i][j] %= 1000000007
    return res

n = int(input())
A = [[1, 1], [1, 0]]

ans = fibo_mat_mul(A, n)

print(ans[0][1])