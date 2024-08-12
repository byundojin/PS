import sys
n = int((ip:=sys.stdin.readline)())
price = list(map(int, ip().split()))
m = int(ip())
dp = [None] * (m+1)

def tonum(arr):
    r = 0
    for i in sorted(arr, reverse=True):
        r *= 10
        r += i
    return r

for i in range(n):
    if m >= (p:=price[i]):
        if dp[p] == None or tonum(dp[p]) < i:
            dp[p] = [i] 

for i in range(n):
    for j in range(m+1-(p:=price[i])):
        if dp[j] == None:
            continue
        if dp[j+p] == None:
            pass
        elif tonum(dp[j+p]) >= tonum(dp[j]+[i]):
            continue
        dp[j+p] = dp[j] + [i]

r = 0
for i in dp:
    if i == None:
        continue
    r = max(r, tonum(i))

print(r)