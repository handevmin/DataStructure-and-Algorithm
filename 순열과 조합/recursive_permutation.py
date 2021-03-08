items = [1,2,3,4]
k = 2

def permutation(items, k):
    result = []

    if k == 1:
        for i in items:
            result.append([i])
    elif k >1:
        for i in range(len(items)):
            temp = [i for i in items]
            temp.remove(items[i])
            for j in permutation(temp, k-1):
                result.append([items[i]]+j)
    return result

print(permutation(items, k))