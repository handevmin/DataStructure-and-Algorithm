import sys

N, M, V = map(int, input().split())
graph = {}
for i in range(M):
    x, y = map(int, input().split())
    if x not in graph:
        graph[x] = [y]
    else :
        graph[x].append(y)

visited = [False]*(N+1)
def dfs(v):
    visited[v]= True
    print(v)
    if v in graph:
        for j in graph[v]:
            if visited[j] != True:
                dfs(j)

dfs(V)