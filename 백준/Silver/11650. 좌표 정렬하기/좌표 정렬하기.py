import sys
ips = lambda:map(int, sys.stdin.readline().split())

N, *_ = ips()
for x, y in sorted((tuple(ips()) for _ in range(N))):
    print(x, y)
