def solution(n, results):
    answer = 0
    mat = [[0 for i in range(n)] for j in range(n)]

    for res in results:
        mat[res[0] - 1][res[1] - 1] = 1
        mat[res[1] - 1][res[0] - 1] = -1
    change = 1
    while change != 0:
        change = 0
        for i in range(n):
            for j in range(n):
                if mat[i][j] == 0 and i != j:
                    for k in range(n):
                        if mat[k][j] == 1 and mat[i][k] == 1:
                            mat[i][j] = 1
                            change += 1
                            break
                        elif mat[k][j] == -1 and mat[i][k] == -1:
                            mat[i][j] = -1
                            change += 1
                            break

    for i in range(n):
        win_count = 0
        lose_count = 0
        for j in range(n):
            if mat[i][j] > 0:
                win_count += 1
            elif mat[i][j] < 0:
                lose_count += 1
        if win_count + lose_count == n - 1:
            answer +=1

    return answer

print(solution(5, [[1, 4], [4, 2], [2, 5], [5, 3]]))