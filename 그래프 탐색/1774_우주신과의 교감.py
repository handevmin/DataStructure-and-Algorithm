import sys
import math

def get_parent(parent, n):
    if parent[n] == n:
        return n
    return get_parent(parent, parent[n])

def find_parent(parent, a, b):
    # 왜 이런식으로 find() 함수만을 이용하게 되면 틀릴까?
    # def find():
    #   if parent[x] == x:
    #       return x
    #   else:
    #       find(parent, parent[x])
    # return parent[x]
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a == b:
        return True
    else:
        return False

def union(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, sys.stdin.readline().split())
coordinate = []
for i in range(N):
    coordinate.append(list(map(int, sys.stdin.readline().split())))
connect_list = []
distance = [[0]*N for i in range(N)]
result = 0
parent = [0]*N
# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(N):
    parent[i] = i

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    connect_list.append([x,y])
    connect_list.append([y,x])
    d = math.sqrt((coordinate[x-1][0] - coordinate[y-1][0])**2 + (coordinate[x-1][1] - coordinate[y-1][1])**2)
    distance[x-1][y-1] = d
    distance[y-1][x-1] = d

edges = []
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        else:
            if distance[i][j] == 0:
                d = math.sqrt((coordinate[i][0] - coordinate[j][0]) ** 2 + (coordinate[i][1] - coordinate[j][1]) ** 2)
                distance[i][j] = d
                distance[j][i] = d

for i in range(N):
    for j in range(i,N):
        if i == j:
            continue
        edges.append((distance[i][j], i, j))

edges.sort()

for i in connect_list:
    cost, a, b = distance[i[0]-1][i[1]-1], i[0]-1, i[1]-1
    union(parent, a, b)

for edge in edges:
    cost, a, b = edge
    if not find_parent(parent,a,b):
        union(parent, a, b)
        result += cost

print('%.2f' % result)
