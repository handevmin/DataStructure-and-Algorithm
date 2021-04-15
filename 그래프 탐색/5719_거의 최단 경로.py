import sys
import heapq
from collections import deque

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (start, 0))
    distance[start] = 0
    while queue:
        now, dist = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            if distance[i[0]] > dist + i[1]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(queue, (i[0], dist + i[1]))

def bfs(v):
    q = deque([v])
    while q:
        data = q.popleft()
        for i in track[data]:
            if distance[data]-i[1] == distance[i[0]] and [data,i] not in dropped:
                q.append(i[0])
                dropped.append([data, i])
                for index, value in enumerate(graph[i[0]]):
                    if value[0] == data and value[1] == i[1]:
                        graph[i[0]][index][1] = int(1e9)

while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break
    S, D = map(int, sys.stdin.readline().split())

    graph = [[] for i in range(N)]
    distance = [int(1e9)] * (N)
    track = [[]for i in range(N)]
    dropped = []
    for i in range(M):
        u,v,p = map(int, sys.stdin.readline().split())
        graph[u].append([v, p])
        track[v].append([u,p])
    dijkstra(S)
    bfs(D)
    distance = [int(1e9)] * (N)
    dijkstra(S)
    print(distance[D] if distance[D] != int(1e9) else -1)