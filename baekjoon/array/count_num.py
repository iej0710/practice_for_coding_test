res = 1
for i in range(3):
    res *= int(input())

num_count = {i:0 for i in range(10)}

while (res != 0):
    tmp = res % 10
    num_count[tmp] += 1
    res //= 10

for i in num_count.keys():
    print(num_count[i])