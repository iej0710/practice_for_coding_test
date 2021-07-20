import sys
from itertools import combinations

N = int(input())
S = []
for i in range(N):
    S.append(list(map(int,sys.stdin.readline().rstrip().split())))

people = set(range(N))
team_case = combinations(people,int(N / 2))

min_ability = 100 * (N**2)

for case in team_case:
    other = people - set(case)
    s1 = 0
    s2 = 0
    for i1,i2 in zip(case,other):
        for j1,j2 in zip(case,other):
            s1 += S[i1][j1]
            s2 += S[i2][j2]
    if abs(s1-s2) == 0:
        print(case, other, s1, s2)
    min_ability = min(min_ability,abs(s1-s2))

print(min_ability)