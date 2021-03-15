import sys

N = int(sys.stdin.readline())
count = 0
while N != 0:
    for i in range(1,N+1):
        if N >= i:
            N-=i
            count+=1
        else:
            break
print(count)