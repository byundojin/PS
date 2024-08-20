import math
H, Y = map(int, input().split())
dp = [0] * (Y + 1)
dp[0] = H
for i in range(1, Y + 1):
    dp[i] = max(dp[i], math.floor(dp[i - 1] * 1.05))
    if 3 <= i:
        dp[i] = max(dp[i], math.floor(dp[i - 3] * 1.2))
    if 5 <= i:
        dp[i] = max(dp[i], math.floor(dp[i - 5] * 1.35))

print(math.floor(dp[Y]))