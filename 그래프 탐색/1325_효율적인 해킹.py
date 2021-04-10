import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())

graph = {}
result = [0]*(N+1)
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if b not in graph:
        graph[b] = [a]
    else:
        graph[b].append(a)

def bfs(v):
    global count
    visited[v] = True
    queue = deque([v])

    while queue:
        data = queue.popleft()
        if data in graph:
            for i in graph[data]:
                if not visited[i]:
                    visited[i] = True
                    count += 1
                    queue.append(i)



for i in graph:
    visited = [False]*(N+1)
    count = 0
    bfs(i)
    result[i] = count

for i, v in enumerate(result):
    if v == max(result):
        print(i, end=' ')

