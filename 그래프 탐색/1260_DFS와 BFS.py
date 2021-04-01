import sys
from collections import deque
N, M, V = map(int, sys.stdin.readline().split())

graph = []

for i in range(M):
    graph.append(list(map(int, sys.stdin.readline().split())))

visited = [False] * (N+1)
dfs_result = ""
bfs_result = ""

def dfs(v):
    visited[v] = True
    global dfs_result
    dfs_result += (str(v)+' ')
    min_vertex = []

    for i in sorted(graph):
        if v == i[0]:
            min_vertex.append(i[1])
        if v == i[1]:
            min_vertex.append(i[0])
    sorted_vertex = sorted(min_vertex, reverse=True)

    while sorted_vertex:
        data = sorted_vertex.pop()
        if not visited[data]:
            dfs(data)

def bfs(v):
    global bfs_result
    queue = deque([])
    queue.append(v)
    visited[v] = True
    min_vertex = []

    while queue:
        data = queue.popleft()
        bfs_result += (str(data)+ ' ')
        for i in sorted(graph):
            if i[0] == data:
                min_vertex.append(i[1])

            elif i[1] == data:
                min_vertex.append(i[0])

        sorted_vertex = sorted(min_vertex, reverse=True)
        while sorted_vertex:
            val = sorted_vertex.pop()
            if not visited[val]:
                queue.append(val)
                visited[val] = True



dfs(V)
print(dfs_result)
visited = [False] * (N+1)
bfs(V)
print(bfs_result)
