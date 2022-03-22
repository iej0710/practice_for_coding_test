n = int(input())

count = 0
i, j = 1, 2
summation = 1
while i <= j and j <= n + 1:
    if summation > n:
        summation -= i
        i += 1
    elif summation == n:
        count += 1
        summation += j
        j += 1
    else:
        summation += j
        j += 1


print(count)
