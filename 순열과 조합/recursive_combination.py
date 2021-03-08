nums = [1, 0, -1, 0, -2, 2]
k = 3
result = []
index = 0


def combination(lst, n):
    ret = []

    if n == 1:
        for i in lst:
            ret.append([i])
    elif n > 1:
        for i in range(len(lst) - n + 1):
            for temp in combination(lst[i + 1:], n - 1):
                ret.append([lst[i]] + temp)

    return ret

print(combination(nums, k))