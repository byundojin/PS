import sys
ip = lambda:int(sys.stdin.readline())
N = ip()
r = sorted(
    (ip() for _ in range(N))
)

for i in r:
    print(i)