class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

n = int(input())

tree = {}
find_root = [False]*(n+1)
for i in range(n):
    data, left, right = map(int, input().split())
    tree[data] = Node(data,left, right)
    if left != -1:
        if find_root[left] != True:
            find_root[left] = True
    if right != -1:
        if find_root[right] != True:
            find_root[right] = True

root = find_root[1:].index(False)+1

count = 0
in_order_level = {}
def in_order(Node, level):
    global count
    if Node.left != -1:
        in_order(tree[Node.left], level+1)
    count += 1
    if level not in in_order_level:
        in_order_level[level] = [count]
    else:
        in_order_level[level].append(count)
    if Node.right != -1:
        in_order(tree[Node.right],  level+1)

in_order(tree[root], 1)
min_level = 10000
max_width = 0
for i in in_order_level:
    width = max(in_order_level[i])-min(in_order_level[i])
    if width > max_width:
        max_width = width
        min_level = i
    elif max_width == width:
        if i < min_level:
            min_level = i
        else:
            continue

print(min_level, max_width+1)