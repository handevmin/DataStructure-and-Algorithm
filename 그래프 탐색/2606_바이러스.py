import sys

computer_num = int(sys.stdin.readline())

v = int(sys.stdin.readline())

graph = {}
for i in range(v):
    x, y = map(int, sys.stdin.readline().split())
    if x not in graph:
        graph[x] = [y]
    else:
        graph[x].append(y)
    if y not in graph:
        graph[y] = [x]
    else:
        graph[y].append(x)

visited= [False] * (computer_num+1)
count = 0
def dfs(v):
    global count
    visited[v] = True
    for i in graph[v]:
        if visited[i] != True:
            count += 1
            dfs(i)
dfs(1)
print(count)
