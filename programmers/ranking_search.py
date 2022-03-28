from itertools import combinations

def binary_search(arr, src, dst, target):
    mid = (src + dst) // 2
    if src > dst:
        return mid

    if arr[mid] >= target:
        return binary_search(arr, src, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, dst, target)

def solution(info, query):
    answer = []
    data = {}
    cond = [0, 1, 2, 3]
    for i in range(len(info)):
        info[i] = info[i].split()
        score = int(info[i][-1])
        for j in range(5):
            for c_set in list(combinations(cond, j)):
                idx = 0
                idc = 0
                k = ''
                while idx < 4:
                    if idc < len(c_set) and c_set[idc] == idx:
                        k += info[i][c_set[idc]]
                        idx += 1
                        idc += 1
                    else:
                        k += '-'
                        idx += 1
                try:
                    data[k].append(score)
                except:
                    data[k] = [score]

    for key in data.keys():
        data[key].sort()

    for q in query:
        q = q.split()
        count = 0
        cond = ''
        target = int(q[-1])
        del q[-1]
        for word in q:
            if word == 'and':
                continue
            else:
                cond += word
        try:
            idx = binary_search(data[cond], 0, len(data[cond]) - 1, target)
            answer.append(len(data[cond]) - idx - 1)
        except:
            answer.append(0)
    return answer

ex = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
q = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(ex, q))