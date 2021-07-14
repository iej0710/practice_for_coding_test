n = int(input())

for i in range(n):
    res = input()
    point = 0
    p = 0
    for j in range(len(res)):
        if res[j] == 'O':
            p += 1
            point += p
        else:
            p = 0
    print(point)