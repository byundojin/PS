import sys
n, m = map(int, (ip:=sys.stdin.readline)().split())
arr = list(map(int, ip().split()))

r=0
p=arr[0]
c = 1
for i in arr[1:]:
    p += m
    x = p-i
    if x >= 0:
        r += x
    else:
        r += -x * c 
        p = i
    c += 1

print(r)