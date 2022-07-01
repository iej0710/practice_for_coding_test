def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res = res * i % (10 ** 9 + 7)
    return res

def power(x, y):
    if y == 0:
        return 1
    elif y % 2 == 1:
        return power(x, y - 1) * x % (10 ** 9 + 7)
    tmp = power(x, y // 2)
    return tmp * tmp % (10 ** 9 + 7)


n, k = map(int, input().split())

res = [[1] * (n + 1) for i in range(n + 1)]

denominator = factorial(n)
nominator = factorial(k) * factorial(n - k)

result = denominator * power(nominator, 10 ** 9 + 5)

print(result % (10 ** 9 + 7))