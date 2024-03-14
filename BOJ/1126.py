import sys,math
inf=math.inf
input=sys.stdin.readline
a=int(input())
l=list(map(int,input().split()))
dp=[[-1 for g in range(500002)] for i in range(a+1)]
if a==1:print(-1);sys.exit()
if a==2:
    if l[0]==l[1]:print(l[0])
    else:print(-1)
    sys.exit()
for i in range(a,-1,-1):
    for j in range(500002):
        if j==500001:dp[i][j]=-inf
        if i==a:
            if j==0:dp[i][j]=0
            else:dp[i][j]=-inf
        else:
            dp[i][j]=max([dp[i+1][j],dp[i+1][min(500001,j+l[i])],dp[i+1][abs(l[i]-j)]+min(l[i],j)])
ans=dp[0][0]
print('-1'if ans==0 else ans)