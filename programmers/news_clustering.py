from collections import Counter
import math

def solution(str1,str2):
    answer = 0
    str1 = str1.upper()
    str2 = str2.upper()

    str1set = [str1[i:i+2] for i in range(len(str1)-1)]
    str2set = [str2[i:i+2] for i in range(len(str2)-1)]
    ## for i in range(len(str1)-1) if str1[i:i+2].isalpha()로 알파벳이 아닌 문자를 가지고 있는 조각들을 제거할 수 있음
    ## line 13-34 구간 -> isalpha()
    delslice = []
    for i in range(len(str1set)):
        if str1set[i][0] == ' ' or str1set[i][1] == ' ':
            delslice.append(i)
            continue
        if ord(str1set[i][0]) < ord('A') or ord(str1set[i][0]) > ord('Z'):
            delslice.append(i)
        elif ord(str1set[i][1]) < ord('A') or ord(str1set[i][1]) > ord('Z'):
            delslice.append(i)
    for i in reversed(delslice):
        del str1set[i]
    delslice = []
    for i in range(len(str2set)):
        if str2set[i][0] == ' ' or str2set[i][1] == ' ':
            delslice.append(i)
            continue
        if ord(str2set[i][0]) < ord('A') or ord(str2set[i][0]) > ord('Z'):
            delslice.append(i)
        elif ord(str2set[i][1]) < ord('A') or ord(str2set[i][1]) > ord('Z'):
            delslice.append(i)
    for i in reversed(delslice):
        del str2set[i]

    str1dict = Counter(str1set)
    str2dict = Counter(str2set)

    intersections = set(str1dict.keys()).intersection(set(str2dict.keys()))
    unions = set(str1dict.keys()).union(set(str2dict.keys()))
    if len(unions) == 0 and len(intersections) == 0:
        return 65536

    tmp = 0
    for i in intersections:
        tmp += min(str1dict[i],str2dict[i])
    tmp2 = 0
    for i in unions:
        tmp2 += max(str1dict[i],str2dict[i])

    answer = math.floor(tmp / tmp2 * 65536)
    return answer

example = ['E=M*C^2','e=m*c^2']
print(solution(example[0],example[1]))