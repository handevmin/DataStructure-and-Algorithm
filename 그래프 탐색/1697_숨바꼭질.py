import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

location = [0]*100001

def search(v):
    queue = deque([v])
    while queue:
        now = queue.popleft()
        if now == K:
            return location[now]
        if 0 <= now-1 <= 100000:
            if not location[now-1]:
                location[now - 1] = location[now] + 1
                queue.append(now - 1)
        if 0 <= now + 1 <= 100000:
            if not location[now+1]:
                location[now + 1] = location[now] + 1
                queue.append(now + 1)
        if 0 <= 2 * now <= 100000:
            if not location[2*now]:
                location[2*now] = location[now] + 1
                queue.append(2 * now)


print(search(N))
