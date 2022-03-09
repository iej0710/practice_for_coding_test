import sys

def recursive(A, n):
    if n == 1:
        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] %= 1000
        return A
    res = recursive(mat_mul(A, A), n // 2)
    if n % 2 == 1:
        res = mat_mul(res, A)
    return res

def mat_mul(A, B):
    res = [[0] * len(A[0]) for i in range(len(B))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                res[i][j] += A[i][k] * B[k][j]
            res[i][j] %= 1000
    return res

n, b = map(int, input().split())
A = []
for i in range(n):
    A.append(list(map(int, sys.stdin.readline().rstrip().split())))

res = recursive(A, b)

for i in range(len(res)):
    for j in range(len(res[0])):
        print(res[i][j], end=' ')
    print()