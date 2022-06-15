import sys
def print_mat(A):
    for i in range(len(A)):
        print(A[i])
    print()

N = int(input())

res = [[float('inf')] * (N + 1) for i in range(N + 1)]
for i in range(1, N + 1):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    res[0][i] = tmp[1]
    res[i][0] = tmp[0]

for i in range(1, N):
    res[i][i + 1] = res[i][0] * res[0][i] * res[0][i + 1]
    res[i][i] = 0
res[0][0], res[-1][-1] = 0, 0

for d in range(1, N + 1):
    for i in range(1, N - d):
        j = i + d + 1
        for k in range(i, j):
            res[i][j] = min(res[i][j], res[i][k] + res[k + 1][j] + res[i][0] * res[0][k] * res[0][j])
    print_mat(res)

print(res[1][-1])