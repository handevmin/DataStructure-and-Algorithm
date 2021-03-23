import sys

N, K = map(int, sys.stdin.readline().split())
dp = [[0] * (K) for i in range(N)]
print(dp)
for i in range(N):
    W, V = map(int, sys.stdin.readline().split())
    for j in range(K):
        if j < W:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W]+V)
print(dp)
print(dp[N-1][K-1])
