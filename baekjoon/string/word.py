d = ord('a') - ord('A')

t = input()

count_char = {}

for i in range(len(t)):
    tmp = t[i]
    if ord(tmp) > ord('Z'):
        tmp = chr(ord(t[i]) - d)

    if tmp not in count_char.keys():
        count_char[tmp] = 1
    else:
        count_char[tmp] += 1

m = max(list(count_char.values()))

c = 0
for i in count_char.keys():
    if count_char[i] == m:
        res = i
        c += 1

if c > 1:
    print('?')
else:
    print(res)

