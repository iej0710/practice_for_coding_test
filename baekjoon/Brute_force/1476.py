e, s, m = map(int, input().split())
year = 1
while e * s * m != 1:
    year += 1
    e -= 1
    s -= 1
    m -= 1
    if e == 0:
        e += 15
    if s == 0:
        s += 28
    if m == 0:
        m += 19

print(year)