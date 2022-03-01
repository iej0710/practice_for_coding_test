import sys

def mat_mul(A, B):
    res = [[0] * len(B[0]) for i in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                res[i][j] += A[i][k] * B[k][j]
    return res


n, m  = map(int, input().split())
A = []
for i in range(n):
    A.append(list(map(int, sys.stdin.readline().rstrip().split())))

m, k = map(int, input().split())
B = []
for i in range(m):
    B.append(list(map(int, sys.stdin.readline().rstrip().split())))

C = mat_mul(A, B)

for i in range(n):
    for j in range(k):
        print(C[i][j], end=' ')
    print()
