import sys
N, S, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
dp = [False] * (M + 1)
dp[S] = True
for i in arr:
    is_change = False
    l = [False] * (M + 1)
    for j in [k for k in range(M + 1) if dp[k]]:
        if j - i >= 0:
            is_change = True
            l[j-i] = True
        if j + i <= M:
            is_change = True
            l[j+i] = True
    dp = l
    if not is_change:
        print(-1)
        exit(0)
result = 0
for i in range(M, 0, -1):
    if dp[i]:
        result = i
        break
print(result)
