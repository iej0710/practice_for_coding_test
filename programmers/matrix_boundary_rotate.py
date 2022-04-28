def print_mat(A):
    for i in range(len(A)):
        print(A[i])
    print()

def solution(rows, columns, queries):
    answer = []
    table = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    for case in queries:
        x1, y1, x2, y2 = case[0] - 1, case[1] - 1, case[2] - 1, case[3] - 1
        min_res = rows * columns + 2
        tmp = table[x1][y1]
        for i in range(1, y2 - y1 + 1):
            min_res = min(min_res, table[x1][y1 + i])
            table[x1][y1 + i], tmp = tmp, table[x1][y1 + i]

        for i in range(1, x2 - x1 + 1):
            min_res = min(min_res, table[x1 + i][y2])
            table[x1 + i][y2], tmp = tmp, table[x1 + i][y2]

        for i in range(1, y2 - y1 + 1):
            min_res = min(min_res, table[x2][y2 - i])
            table[x2][y2 - i], tmp = tmp, table[x2][y2 - i]

        for i in range(1, x2 - x1 + 1):
            min_res = min(min_res, table[x2 - i][y1])
            table[x2 - i][y1], tmp = tmp, table[x2 - i][y1]
        answer.append(min_res)

    return answer

ex = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(6,6,ex))