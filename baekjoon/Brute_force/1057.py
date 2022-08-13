N, a, b = map(int, input().split())

count = 1

while (a - 1) // 2 != (b - 1) // 2:
    a = a // 2 + a % 2
    b = b // 2 + b % 2

    count += 1
    if count >= N:
        break

if count >= N:
    print(-1)
else:
    print(count)
