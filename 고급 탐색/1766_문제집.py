import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
array = [[] for i in range(N+1)]
indegree = [0]*(N+1)

heap = []
result = []

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    array[x].append(y)
    indegree[y]+=1

for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

result = []

while heap:
    data = heapq.heappop(heap)
    result.append(data)
    for i in array[data]:
        indegree[i] -=1
        if indegree[i] == 0:
            heapq.heappush(heap, i)

for i in result:
    print(i, end= ' ')