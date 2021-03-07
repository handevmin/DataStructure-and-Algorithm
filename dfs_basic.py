# 과제 5번 코드란
N, M, V = 4, 5, 1
edges = [[1, 2], [1, 3], [1,4], [2, 3], [3, 4]]
visited = [False] * (N+1)
print(visited)
def solution(N, M, V, edges):
    def dfs(start):
        visited[start] = True
        print(start)
        for i in(edges):
            if not visited[i[1]] and start == i[0]:
                dfs(i[1])
    dfs(V)

solution(N, M, V, edges)