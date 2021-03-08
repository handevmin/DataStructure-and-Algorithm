def DFS (L, start):

    #종료조건
    if L == r:
        if value not in result:
            print(value)
        result.append(value)
    else:
        for i in range(start, len(nums)):
            value[L] = nums[i]
            visited[i] = True
            DFS(L+1, i+1)
            visited[i] = False

nums = [1,1,1,1,1,1]
r = 4
value = [0]*r
visited = [False] * len(nums)
result = []
DFS(0,0)

