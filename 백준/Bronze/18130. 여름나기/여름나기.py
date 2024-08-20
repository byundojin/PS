import sys
n, q = map(int, sys.stdin.readline().split())
num = 0
price = 2 ** 64
max_price = 2 ** 64
for i in range(n):
    p, k, c = map(int, sys.stdin.readline().split())
    x = q // k
    if q % k == 0:
        x -= 1
    p += ((x + 1) * x // 2) * c
    if p < price:
        price = p
        num = i + 1
print(num, price)