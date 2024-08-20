import random

def solution():
    r, c = map(lambda x: int(x), input().split(" "))
    mine = []
    for i in range(r):
        mine.append(list(input()))

    lm = [[-1 for j in range(c)] for i in range(r)]
    rm = [[-1 for j in range(c)] for i in range(r)]

    for y in range(r):
        for x in range(c):
            if lm[y][x] == -1:
                if mine[y][x] == '1':
                    k = 0
                    while x - (k + 1) >= 0 and y + (k + 1) < r and mine[y + (k + 1)][x - (k + 1)] == "1":
                        k += 1
                    for i in range(k + 1):
                        lm[y + i][x - i] = k - i + 1
                else:
                    lm[y][x] = 0

            if rm[y][x] == -1:
                if mine[y][x] == '1':
                    k = 0
                    while x + (k + 1) < c and y + (k + 1) < r and mine[y + (k + 1)][x + (k + 1)] == "1":
                        k += 1
                    for i in range(k + 1):
                        rm[y + i][x + i] = k - i + 1
                else:
                    rm[y][x] = 0


    result = 0
    for y in range(r):
        for x in range(c):
            v = lm[y][x] if lm[y][x] < rm[y][x] else rm[y][x]
            if v == 0:
                continue
            elif v == 1:
                if result == 0:
                    result = 1
                continue
            count = 1
            for i in range(1, v):
                if lm[y + i][x + i] > i and rm[y + i][x - i] > i:
                    count = i + 1
            if result < count:
                result = count

    return result

print(solution())