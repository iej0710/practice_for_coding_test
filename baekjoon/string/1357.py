def Rev(x):
    x = reversed(list(str(x)))
    res = ''
    for  char in x:
        res += char
    return int(res)

X, Y = map(int, input().split())
print(Rev(Rev(X) + Rev(Y)))
