import sys
n = int((ip:=sys.stdin.readline)())
dp = [None] * 1001
dp[0] = 0
for i in map(int, ip().split()):
    for j in range(i):
        if dp[j] == None:
            continue
        if dp[i] == None:
            pass
        elif dp[j] + i < dp[i]:
            continue
        dp[i] = dp[j] + i

r = 0
for i in dp:
    if i:
        r = max(r, i)
print(r)