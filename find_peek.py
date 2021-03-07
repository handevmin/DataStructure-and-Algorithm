
def find_peek(k):
    if x[k-1] < x[k] and x[k+1]< x[k]:
        return x[k]
    return find_peek(k+1)

x = [-4, -4, -2, 0, 0, 2, 4, 5, 6, 3, 2, -4, -6]
print(find_peek(1))