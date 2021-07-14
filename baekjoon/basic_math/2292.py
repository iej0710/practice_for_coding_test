x = int(input())
n = 1
while 3*(n**2)+3*n+1 < x:
    n += 1

if x == 1:
    print(n)
else:
    print(n+1)