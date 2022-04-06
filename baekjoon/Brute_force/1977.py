import math

m = int(input())
n = int(input())

bottom = math.ceil(math.sqrt(m))
top = math.ceil(math.sqrt(n))
if top == math.sqrt(n):
    top += 1

summation = 0
for item in range(bottom, top):
    summation += item ** 2

if summation == 0:
    print(-1)
else:
    print(summation)
    print(bottom ** 2)