combination_result = []
permutation_result = []
items = list(range(4))

for i in list(itertools.combinations(items, 2)):
    combination_result.append(i)

for j in list(itertools.permutations(items, 2)):
    permutation_result.append(i)

print("combination result: ", combination_result)
print()
print("permutation result: ", permutation_result)