N = int(input())
for i in range(1, N+1):
    r = sum(int(i) for i in str(i)) + i
    if r == N:
        break
else:
    print(0)
    exit(0)
print(i)