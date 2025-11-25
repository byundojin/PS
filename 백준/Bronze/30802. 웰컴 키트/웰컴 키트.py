import math
N = int(input())
li = map(int, input().split())
T, P = map(int, input().split())

res = 0
for i in li:
    res += i//T 
    res += (i%T)>0

print(res)
print(N//P, N%P)