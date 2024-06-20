import sys
n = int(sys.stdin.readline())
def f():
    _, *arg = map(int, sys.stdin.readline().split())
    return sum(arg)
arr = [f() for _ in range(n)]
arr.sort()
result = 0
for i in range(n):
    result += arr[i] * (len(arr) - i)
print(result)