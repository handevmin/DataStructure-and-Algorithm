items = [1,3,4,2,3,4]
k = 4
result = []
def dfs(items, k):
    result = []

    if k == 1:
        for i in items:
            result.append([i])
    else:
        for i in range(len(items)-k+1):
            for j in dfs(items[i+1:], k-1):
                result.append([items[i]]+j)
    return result

print(dfs(items, k))