import sys
n, m = map(int, (ip:=sys.stdin.readline)().split())
cmp = 1
def ch(n):
    if n==cmp:
        return True
    elif n==0:
        return False
    print(0)
    exit(0)

while n or m:
    cp = cmp * 3
    n_s = n%cp
    m_s = m%cp
    if not ch(n_s) ^ ch(m_s):
        print(0)
        exit(0)
    if m_s == cmp:
        m -= cmp
    if n_s == cmp:
        n -= cmp
    cmp *= 3

print(1)