def solution(weights, head2head):
    outcome = {i: 0 for i in range(len(weights))}
    count_heavier = {i: 0 for i in range(len(weights))}
    game = {i: len(weights) for i in range(len(weights))}
    for i in range(len(weights)):
        for j in range(len(head2head[i])):
            if head2head[i][j] == 'W':
                outcome[i] += 1
                if weights[i] < weights[j]:
                    count_heavier[i] += 1
            elif head2head[i][j] == 'N':
                game[i] -= 1
    #info_boxer = [[i+1, outcome[i] / game[i], count_heavier[i], weights[i]] for i in range(len(weights))]
    info_boxer = []
    for i in range(len(weights)):
        if game[i] > 0:
            info_boxer.append([i+1, outcome[i] / game[i], count_heavier[i], weights[i]])
        else:
            info_boxer.append([i + 1, 0, count_heavier[i], weights[i]])

    info_boxer = sorted(info_boxer, key=lambda x: (x[1], x[2], x[3], -x[0]),reverse=True)
    return [info_boxer[i][0] for i in range(len(info_boxer))]

print(solution([50,82,75,120],["NLWL","WNLL","LWNW","WWLN"]))
print(solution([60,70,60],["NNN","NNN","NNN"]))
