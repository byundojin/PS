N = int(input())
arr = [0, 0, 0]
c = 0
result = 1
for _ in range(N):
    result += sum(arr) - arr[c] + 1
    arr[c] += 1
    c += 1
    if c == 3:
        c = 0
print(result)