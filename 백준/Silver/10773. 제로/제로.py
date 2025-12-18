import sys
from collections import deque
ip = lambda:int(sys.stdin.readline())
K = ip()
q = deque([])
for _ in range(K):
    n = ip()
    if n == 0:
        q.pop()
    else:
        q.append(n)

r = 0
while len(q) > 0:
    r += q.pop()

print(r)