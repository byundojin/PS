import sys
ip = lambda:int(sys.stdin.readline())
N = ip()
li = sorted((ip() for _ in range(N)))

s=sum(li)
if s<0:
    r = -int((abs(s))/N+0.5)
else:
    r = int(s/N+0.5)
print(r)
print(li[N//2])

n=li[0]
c=0
r=0
p1=n
p2=None
for i in li:
    if i == n:
        c += 1
        continue
    if r < c:
        r = c
        p1 = n
        p2 = None
    elif p2 is None and r == c:
        p2 = n
    c = 1
    n = i
if r < c:
    r = c
    p1 = n
    p2 = None
elif p2 is None and r == c:
    p2 = n
print(p2 if p2 is not None else p1)

print(li[-1] - li[0])