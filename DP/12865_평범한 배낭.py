import sys

N, K = map(int, sys.stdin.readline().split())
<<<<<<< HEAD
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
=======
item = []
for i in range(N):
    item.append(list(map(int, sys.stdin.readline().split())))

print(item)
>>>>>>> origin/master
