def scoring(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80 and avg < 90:
        return 'B'
    elif avg >= 70 and avg < 80:
        return 'C'
    elif avg >= 50 and avg < 70:
        return 'D'
    else:
        return 'F'

def solution(scores):
    answer = ''
    res = 0
    for i in range(len(scores)):
        score = list(zip(*scores))[i]
        tmp_max = max(score[:i]+score[i+1:])
        tmp_min = min(score[:i]+score[i+1:])
        if scores[i][i] > tmp_max or scores[i][i] < tmp_min:
            res = sum(score[:i]+score[i+1:]) / (len(scores) - 1)
        else:
            res = sum(score) / len(scores)
        answer += scoring(res)
    return answer

example = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]

print(solution(example))