
self_number = set([i for i in range(1,10001)])
def d(n):
    res = n
    if n > 10000:
        return 0
    while 1:
        res += n % 10
        if res > 10000:
            return 0
        if n // 10 != 0:
            n = n // 10
        else:
            break
    self_number.discard(res)
    #d(res)
    return res


for i in range(10000):
    tmp = d(i+1)

for i in range(len(self_number)):
    print(list(self_number)[i])

