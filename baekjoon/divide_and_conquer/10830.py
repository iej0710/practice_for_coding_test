import sys

def mat_mul(A, B):
    res = [[0] * len(B[0]) for i in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                res[i][j] += A[i][k] * B[k][j]

    return res

n, b = map(int, input().split())
A = []
for i in range(n):
    A.append(list(map(int, sys.stdin.readline().rstrip().split())))

tmp = b / 2
res = A
while tmp > 1:
    res = mat_mul(res, res)
    tmp /= 2

if b % 2 == 1:
    res = mat_mul(res, A)

for i in range(len(res)):
    for j in range(len(res[0])):
        print(res[i][j] % 1000, end=' ')
    print()