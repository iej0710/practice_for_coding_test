n = int(input())

T = 15 * 10**5
R = [0] * T
R[1] = 1
for i in range(2, T):
    R[i] = (R[i - 1] + R[i - 2]) % (10 ** 6)
    if i == n:
        break

print(R[n % T])
