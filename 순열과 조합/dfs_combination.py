def dfs(depth, start):

    #종료조건
    if depth == k:
        print(result)
    else:
        for i in range(start, len(nums)):
            result[depth] = nums[i]
            checklist[i] = True
            dfs(depth+1, i+1)
            checklist[i] = False

nums = [1,2,3]
k = 2
result = [0] * k
checklist= [False] * len(nums)

dfs(0,0)