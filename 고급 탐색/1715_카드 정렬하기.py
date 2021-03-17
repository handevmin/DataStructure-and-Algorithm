import heapq
import sys
heap = []
n = int(sys.stdin.readline())
for i in range(n):
    data = int(sys.stdin.readline())
    heapq.heappush(heap, data)
if n == 1:
    print(0)
else:
    result = 0
    while len(heap)!=1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        sum_value = first + second
        result += sum_value
        heapq.heappush(heap, sum_value)
    print(result)