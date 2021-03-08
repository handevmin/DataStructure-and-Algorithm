items = [1,2,3,4]
k = 2
result = []
checklist = [False]*len(items)
result = [0] * k

def dfs(depth, start):
    if depth == k:
        print(result)
        return
    for i in range(len(items)):
        result[depth] = items[i]
        checklist[i] = True
        dfs(depth+1, start+1)
        checklist[i] = False

dfs(0,0)