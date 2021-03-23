import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
count = [1]*n

for i in range(1,n):
    for j in range(0,i):
        if array[i] > array[j]:
            count[i] = max(count[j]+1, count[i])

print(max(count))


