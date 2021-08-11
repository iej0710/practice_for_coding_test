def solution(gems):
    gems_dict = set(gems)
    src = 0
    dst = 0
    gems_count = {}
    shortest = len(gems)
    answer = [src,dst]
    while dst < len(gems):
        if gems[dst] in gems_count.keys():
            gems_count[gems[dst]] += 1
        else:
            gems_count[gems[dst]] = 1
        if len(gems_count.keys()) == len(gems_dict):
            for idx in range(src,dst + 1):
                if gems_count[gems[idx]] > 1:
                    gems_count[gems[idx]] -= 1
                elif gems_count[gems[idx]] == 1:
                    if dst - idx < shortest:
                        shortest = dst - idx
                        answer = [idx + 1, dst + 1]
                    break
            src = idx
        dst += 1

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["DIA", "EM", "EM", "RUB", "DIA"]))
print(solution(["A","B","B","B","B","B","B","C","B","A"]))
print(solution(["A","A","A","B","B"]))
print(solution(["A", "B", "C", "B", "F", "D", "A", "F", "B", "D", "B"]))
print(solution(["A"]))