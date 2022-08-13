from collections import Counter

text = input()

char = Counter(list(text))
flag = 1
try:
    if char['U'] >= 1 and char['C'] >= 2 and char['P'] >= 1:
        flag = 1
    else:
        flag = 0
except:
    flag = 0

if flag == 0:
    print('I hate UCPC')
else:
    j = 0
    flag = 0
    target = ['U', 'C', 'P', 'C']
    for alphabet in text:
        if alphabet == target[j]:
            j += 1
        if j == len(target):
            print('I love UCPC')
            flag = 1
            break
    if flag == 0:
        print('I hate UCPC')