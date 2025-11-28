N = int(input())

if N == 1:
    print(1)
    exit(0)

N -= 1

r = 1
while r*6 < N:
    N -= r*6
    r+=1

print(r+1)