N = int(input())
dp = [None] * (N + 2)
dp[0] = 1
dp[1] = 1

def f(n):
    if dp[n]:
        return dp[n]
    result = 0
    if n % 2 == 1:
        result += f(n//2) ** 2
    for i in range(0, n//2):
        result += f(i) * f(n-1-i) * 2
    dp[n] = result
    return result

print(f(N))