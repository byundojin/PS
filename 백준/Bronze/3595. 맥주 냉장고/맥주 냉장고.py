n = int(input())
r = 100000000000
p = []
if n == 1:
    print(1,1,1)
    exit(0)
for x in range(1, n + 1):
    if n % x != 0:
        continue
    for y in range(1, (xd:=n//x)):
        if xd % y != 0:
            continue

        z = (xd // y)
        if (rc := x*y+x*z+y*z) < r:
            r = rc
            p = [x, y, z]

print(*p)
