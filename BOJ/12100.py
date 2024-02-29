import sys
from pprint import pprint
N = int(sys.stdin.readline())
arr = [[0] * (N + 1)]
for _ in range(N):
    arr.append([0]+list(map(int, sys.stdin.readline().split())))

class Max():
    n = 0

def slide(li:list):
    i = 1
    while len(li) - 1 > i:
        if li[i] == li[i + 1]:
            li.pop(i)
            li[i] *= 2
            Max.n = max(li[i], Max.n)
        i += 1

    while len(li) < N + 1:
        li.append(0)

    

def move(arr, x = 0, y = 0):
    result = [[0]*(N + 1)]
    for i in range(1, N + 1):
        li = [0]
        for j in range(1, N + 1):
            if x == 0:
                n = arr[j*y][i]
            elif y == 0:
                n = arr[i][j*x]
            if n == 0:
                continue
            li.append(n)
        slide(li)
        result.append(li)

    pprint(result)
    pprint("============================")
    return result

def dfs(arr, d = 0):
    d += 1
    if d == 6:
        return
    # dfs(move(arr, 1, 0), d)
    dfs(move(arr, -1, 0), d)
    dfs(move(arr, 0, 1), d)
    dfs(move(arr, 0, -1), d)

dfs(arr)

if Max.n == 0:
    print(max([max(i) for i in arr]))
else:
    print(Max.n)

"""
10
16 16 8 32 32 0 0 8 8 8
16 0 0 0 0 8 0 0 0 16
0 0 0 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
"""