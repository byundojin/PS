N = int(input())
dp = [-1] * 1000
dp[1] = 0
dp[2] = 1
def f(n):
    if dp[n] != -1:
        return dp[n]
    n1 = n // 2
    n2 = n // 2
    if n % 2 == 1:
        n1 += 1
    result = (n1 * n2) + f(n1) + f(n2)
    dp[n] = result
    return result

print(f(N))
    