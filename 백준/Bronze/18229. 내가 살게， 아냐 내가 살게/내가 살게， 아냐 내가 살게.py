import sys
n, m, k = map(int, sys.stdin.readline().split())
result = (0, 101)
for j in range(n):
    c=0
    r=0
    for i in map(int, sys.stdin.readline().split()):
        c+=1
        r+=i
        if r >= k:
            if c < result[1]:
                result = (j+1, c)
            break
print(*result)