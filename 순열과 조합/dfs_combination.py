def DFS (L, start):

    #종료조건
    if L == r:
        print(result)
    else:
        for i in range(start, len(nums)):
            result[L] = nums[i]
            DFS(L+1, i+1)

nums = [1,2,3]
r = 2
result = [0]*r

DFS(0,0)