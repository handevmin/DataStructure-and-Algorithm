from collections import deque

N, M, V = 4, 5, 1
edges = [[2, 3], [1, 3], [1,4], [2, 3], [3, 4]]
visited = [False] * (N+1)
graph = {}
for i in edges:
    if i[0] not in graph:
        graph[i[0]] = [i[1]]
    else:
        graph[i[0]].append(i[1])

print(graph)

def bfs(start):
    global visited
    global graph

    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v)
        if v in graph:
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

bfs(1)
