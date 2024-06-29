import sys 

n, k = map(int, sys.stdin.readline().split())
ls = [0] * (k + 1)
rs = [0] * (k + 1)

c = 0
for i in map(int, sys.stdin.readline().split()):
    if c < n:
        ls[i] += 1
    else:
        rs[i] += 1
    c += 1

result = 0

for i in range(1, k + 1):
    result += ls[i] * (n - rs[i])

print(result)
