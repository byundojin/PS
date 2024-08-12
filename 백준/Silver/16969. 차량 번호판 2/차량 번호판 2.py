import sys
n = sys.stdin.readline().strip()
c = 1
r = 1
p = 1
pc = ''
for i in n:
    if pc != i:
        if i == 'd':
            p = 10
            pc = 'd'
        else:
            p = 26
            pc = 'c'
        r*=c
        r%=1000000009
        c = 0
    if c:
        c//=p
        c*=(p-1) 
    else:
        c=1
    c*=p
r*=c
r%=1000000009
print(r)