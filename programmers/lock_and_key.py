import copy


def rotate(key):
    return list(zip(*key[::-1]))


def unlock(lock):
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0:
                return False
    return True


def solution(key, lock):
    answer = True
    for d in range(4):
        for i in range(-len(key) + 1, len(lock)):
            for j in range(-len(key) + 1, len(lock)):
                tmp = copy.deepcopy(lock)

                for x in range(len(key)):
                    flag = 1
                    for y in range(len(key)):
                        if 0 <= i + x < len(tmp) and 0 <= j + y < len(tmp) and key[x][y] * tmp[i + x][j + y] == 0:
                            tmp[i + x][j + y] += key[x][y]
                        elif 0 <= i + x < len(tmp) and 0 <= j + y < len(tmp) and key[x][y] * tmp[i + x][j + y] == 1:
                            flag = 0
                            break
                    if flag == 0:
                        break

                if unlock(tmp):
                    return True
        key = rotate(key)
    return False