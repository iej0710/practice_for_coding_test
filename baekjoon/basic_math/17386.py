def CCW(pos):
    res = 0
    for i in range(len(pos) - 1):
        res += pos[i][0] * pos[i + 1][1] - pos[i + 1][0] * pos[i][1]
    res += pos[-1][0] * pos[0][1] - pos[0][0] * pos[-1][1]
    return res


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

ABC = CCW([[x1, y1], [x2, y2], [x3, y3]])
ABD = CCW([[x1, y1], [x2, y2], [x4, y4]])

CDA = CCW([[x3, y3], [x4, y4], [x1, y1]])
CDB = CCW([[x3, y3], [x4, y4], [x2, y2]])

if ABC * ABD < 0 and CDA * CDB < 0:
    print(1)
else : print(0)