N = int(input())
if N == 1:
    print(1)
    print(1, 1)
    exit(0)

print(2*N-2)
for i in range(N-1):
    print(1, i+2)
    print(N, i+2)