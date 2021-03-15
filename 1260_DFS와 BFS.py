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
def dfs(v, graph):
    visited[v]= True
    print(v)
    for i in graph:
        print("graph",graph[i])
        if graph[i].isdigit():
            print("awefawef")
            return
        for j in graph[i]:
            print(j)
            if visited[j] != True:
                print(j, graph[i])
                dfs(j, graph[i])

dfs(V, graph)