import sys
input = sys.stdin.readline
N, M = map(int, input().split())

graph = {}
for i in range(M):
    A, B, C = map(int, input().split())
    if A not in graph:
        graph[A] = {}
    graph[A][B] = C
    if B not in graph:
        graph[B] = {}
    graph[B][A] = C

start, end = map(int, input().split())
visited = [False]*(N+1)
result = []
def dfs(begin, end, weight):
    global visited
    visited[begin] = True
    if begin == end:
        result.append(weight)
        if len(result) >= 3:
            return

    for i in graph[begin]:
        if visited[i] == False:
            if weight < graph[begin][i]:
                big_weight = graph[begin][i]
            else:
                big_weight = weight
            dfs(i, end, big_weight)
        if start == begin:
            visited = [False] * (N + 1)

print(result)
dfs(start, end, 0)
print(max(result))


