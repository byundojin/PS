import sys
n, m = map(int, sys.stdin.readline().split())
arr = sorted(map(int, sys.stdin.readline().split()), reverse=True)
arr_sum = sum(arr)

v = 0
c = 0
while v < (arr_sum / 2): 
    v += arr[c]
    c += 1
    
print(m // (c+1))