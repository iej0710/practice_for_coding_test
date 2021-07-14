N = int(input())

n = 1
while ((n**2)+n)/2 < N:
    n += 1

if n % 2 == 0:
    side = '+'
else:
    side = '-'

x = n
y = 1
n = n // 2

if side == '+':
    pos = 2 * (n ** 2) - n + 1
else:
    pos = 2 * (n ** 2) + 3 * n + 1

while pos != N:
    x -= 1
    y += 1
    if side == '+':
        pos += 1
    else: pos -= 1

print('{}/{}'.format(y,x))
