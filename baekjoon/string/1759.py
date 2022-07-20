from itertools import combinations
from collections import Counter
l, c = map(int, input().split())

char = sorted(input().split())
aeiou = ['a','e','i','o', 'u']
c = [chr(i) for i in range(ord('a'), ord('z') + 1)]

for case in combinations(char, l):
    if len(set(case).intersection(set(aeiou))) >= 1 and len(set(case).intersection(set(c) - set(aeiou))) >= 2:
        print("".join(case))