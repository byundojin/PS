import sys

dp_fac = [0] * 100
dp_fac[1] = 1

def fac(n):
    if dp_fac[n]:
        return dp_fac[n]
    return n * fac(n-1)

def catalan(n):
    return fac(2*n)//(fac(n+1) * fac(n))

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        exit(0)
    print(catalan(n))