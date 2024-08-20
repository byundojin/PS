n = int(input())
for i in range(-n+1, n):
    x = abs(i)
    print(" "*(n-x-1),end="")
    print("*"*(x*2+1),end="")
    print()