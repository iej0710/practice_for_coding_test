n = int(input())

src, dst = 0, n

while src <= dst:
    mid = (src + dst) // 2

    if mid ** 2 < n:
        src = mid + 1

    else:
        dst = mid - 1

print(src)