nums = [1, 0, -1, 0, -2, 2]
target = 0
result = []

def combination(nums, target):
    if len(result) == 1:
        return nums[0]
    else:
        combination(nums[1:], target)

print(combination(nums, target))