import sys
p = [i for i in range(10000001)]
p[0] = None
p[1] = None
for i in range(2, 1000):
    is_prime=True
    for j in range(2, i):
        if i % j == 0:
            is_prime=False
            break
    if is_prime:
        for k in range(i*2, 10000001, i):
            p[k] = None
n = int((ip := sys.stdin.readline)())
result = 1
for i in set(map(int ,ip().split())):
    if p[i]:
        result *= i
if result == 1:
    print(-1)
else:
    print(result)
