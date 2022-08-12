#timeout

def position(x):
    global count
    if x == len(info):
        count += 1
    else:
        for i in range(len(info)):
            info[x] = i
            flag = 1
            for j in range(x):
                if info[j] == info[x] or abs(info[j] - info[x]) == x - j:
                    flag = 0
            if flag == 1:
                position(x + 1)

N = int(input())
count = 0
info = [0] * N
position(0)
print(count)