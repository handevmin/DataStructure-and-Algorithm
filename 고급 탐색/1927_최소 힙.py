import heapq
import sys

n = int(sys.stdin.readline())
heap = []
result = []

for i in range(n):
    data = int(sys.stdin.readline())
    if data == 0:
        if heap == []:
            result.append(0)
        else:
            result.append(heapq.heappop(heap))
    else:
        heapq.heappush(heap, data)

for data in result:
    print(data)
