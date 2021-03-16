import sys

N = int(sys.stdin.readline())

trophy = []
for i in range(N):
    trophy.append(int(sys.stdin.readline()))
max = trophy[0]

def ascending(trophy):
    max = trophy[0]
    count = 1

    for i in trophy:
        if i > max:
            count += 1
            max = i
    return count

print(ascending(trophy))
trophy.reverse()
print(ascending(trophy))

