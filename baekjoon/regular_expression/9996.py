n = int(input())
pattern = input()

for i in range(n):
    x = input()
    pos = 0
    direction = 1
    count = 0
    a_pos = 0
    for j in range(len(pattern)):
        if ord(pattern[pos]) != 42 and x[pos] == pattern[pos] and a_pos < len(x) + pos + 1:
            pos += direction * 1
            count += 1
        elif ord(pattern[pos]) == 42:
            a_pos = pos
            pos = -1
            direction = -1
    if count == len(pattern) - 1:
        print('DA')
    else:
        print('NE')