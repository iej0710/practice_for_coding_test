import math
N = int(input())
if N == 1:
    print(0)
elif N == 2:
    print(1)
else:
    prime_status = [True] * N
    prime_status[0] = False
    num = []
    for i in range(1, N + 1):
        if prime_status[i - 1]:
            num.append(i)
            for j in range(2 * i, N + 1, i):
                    prime_status[j - 1] = False

    idx = 3
    i, j = 0, 1
    res = 0
    partial_sum = num[i] + num[j]
    while i <= j:
        if partial_sum == N:
            res += 1
            j += 1
            if j < len(num):
                partial_sum += num[j]
            else:
                break
        elif partial_sum < N:
            j += 1
            if j < len(num):
                partial_sum += num[j]
            else:
                break
        else:
            partial_sum -= num[i]
            i += 1

    print(res)