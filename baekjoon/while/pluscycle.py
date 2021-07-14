src = int(input())
n = src
l = 1

while True:
    a = n // 10
    b = n % 10
    n = b * 10 + (a + b) % 10
    if n != src:
        l += 1
    else:
        print(l)
        break
