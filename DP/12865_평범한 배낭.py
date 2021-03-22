import sys

N, K = map(int, sys.stdin.readline().split())
item = []
for i in range(N):
    item.append(list(map(int, sys.stdin.readline().split())))

print(item)