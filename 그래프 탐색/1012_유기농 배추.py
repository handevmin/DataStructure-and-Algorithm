import sys
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0,0,-1,1]

T = int(sys.stdin.readline())

def bfs(i,j, M, N):
    global count
    queue = deque([[i,j]])
    while queue:
        data = queue.popleft()
        board[data[0]][data[1]] = 0

        for i in range(4):
            if 0<= data[0]+dr[i] < N and 0<= data[1]+dc[i] < M and not visited[data[0]+dr[i]][data[1]+dc[i]]:
                if board[data[0]+dr[i]][data[1]+dc[i]] == 1:
                    visited[data[0]+dr[i]][data[1]+dc[i]] = True
                    queue.append([data[0]+dr[i], data[1]+dc[i]])
    count+=1


for i in range(T):
    count = 0

    M, N, K = map(int, sys.stdin.readline().split())

    board = [[0]*M for i in range(N)]
    visited = [[False] * (M) for i in range(N)]

    for i in range(K):
        r, c = map(int, sys.stdin.readline().split())
        board[c][r] = 1

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                bfs(i,j, M, N)

    print(count)
