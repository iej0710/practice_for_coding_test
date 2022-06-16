import sys
def print_mat(A):
    for i in range(len(A)):
        print(A[i])
    print()
T = int(input())

for test_case in range(T):
    K = int(input())
    A = list(map(int, sys.stdin.readline().rstrip().split()))

    res = [[float('inf')] * K for i in range(K)]
    res[0][0] = A[0]
    simple = [0] * K

    for i in range(K):
        simple[i] = simple[i - 1] + A[i]
        res[i][i] = 0

    for d in range(1, K):
        for i in range(K - d):
            j = i + d
            for k in range(i, j):
                #print(res[i][j], res[i][k], res[k + 1][j], simple[j], simple[i])
                res[i][j] = min(res[i][j], res[i][k] + res[k + 1][j] + simple[j] - simple[i] + A[i])

    print(res[0][-1])
