import sys

N, C = map(int, sys.stdin.readline().split())
houses = []

for i in range(N):
    houses.append(int(sys.stdin.readline()))

houses.sort()

min = 1
max = houses[-1] - houses[0]
mid = (min + max) // 2
next = 0
count = 1

if C == 2:
    print(max)
else:
    while True:
        next = 0
        shares = [houses[0]]
        for i in (houses):
            if i >= next+mid:
                if i not in shares:
                    shares.append(i)
                next = i
        if len(shares)<C:
            max = mid-1
            mid = (min + max) //2
        else:
            break
    result = 1000000000
    shares.sort()
    for i in range(len(shares)-1):
        if shares[i+1] - shares[i]<result:
            result = shares[i+1] - shares[i]
    print(result)
