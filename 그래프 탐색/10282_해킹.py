import sys
import heapq

T = int(sys.stdin.readline())

def dijkstra(v):
    queue = []
    heapq.heappush(queue, (v, 0))
    distance[v] = 0
    while queue:
        now, dist = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (i[0], cost))

for i in range(T):
    n, d, c = map(int, sys.stdin.readline().split())

    graph = [[] for i in range(n+1)]
    visited = [False] * (n+1)
    distance = [int(1e9)] * (n+1)

    count = 0
    time = 0

    for j in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        graph[b].append((a,s))

    dijkstra(c)
    for k in distance:
        if k != int(1e9):
            count +=1
            if k > time:
                time = k

    print(count, time)


