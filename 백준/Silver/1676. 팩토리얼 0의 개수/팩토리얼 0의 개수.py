N = int(input())
r = 1
for i in range(1, N+1):
    r *= i

print(len(str(r)) - len(str(r).strip("0")))