from collections import Counter
from itertools import permutations, combinations
def solution(orders, course):
    answer = []
    each_menu = [set(list(order)) for order in orders]
    menu_pattern = []
    for items in permutations(each_menu,2):
        temp = items[0].intersection(items[1])
        for k in range(len(items[0].intersection(items[1]))):
            for c in combinations(items[0].intersection(items[1]),k+1):
                menu_pattern.append(''.join(sorted(c)))
    menu_pattern = Counter(menu_pattern)

    length_pattern = {l:[] for l in course}
    for length in course:
        for key in menu_pattern.keys():
            if length == len(key) and menu_pattern[key] > 1:
                length_pattern[length].append(key)

    for l in length_pattern.keys():
        if len(length_pattern[l]) == 0:
            continue
        tmp = max([menu_pattern[length_pattern[l][i]] for i in range(len(length_pattern[l]))])

        for c in length_pattern[l]:
            if tmp == menu_pattern[c]:
                answer.append(c)
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))