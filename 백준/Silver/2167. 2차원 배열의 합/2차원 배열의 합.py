import sys
ips = lambda:map(int, sys.stdin.readline().split())

N, M = ips()

def f():
    p = 0
    return [0, *((p:=i+p) for i in ips())]

li = [
    f()
    for _ in range(N)
]

K, *_ = ips()

for _ in range(K):
    y1, x1, y2, x2 = ips()

    res = 0
    for y in range(y1-1, y2):
        res += li[y][x2] - li[y][x1-1]
    print(res)