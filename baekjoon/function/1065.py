def f(n):
    if n < 100:
        return 1
    else:
        a = n // 100
        b = (n % 100) // 10
        c = n % 10
        if a - b == b - c:
            return 1
        else:
            return 0

x = int(input())

count = 0
for i in range(1,x+1):
    count += f(i)

print(count)