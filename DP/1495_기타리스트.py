import sys

N, S, M = map(int, sys.stdin.readline().split())
control = list(map(int, sys.stdin.readline().split()))

volumn_list = [False] * (M+1)
volumn_list[S] = True
update_volumn_list = [False] * (M+1)
result =0

def dfs(volumn_list, level):
    global result
    update_volumn_list = [False] * (M+1)
    if level == N:
        for i in reversed(range(len(volumn_list))):
            if volumn_list[i] == True:
                result = i
                return
            else:
                result = -1
        return

    for i, v in enumerate(volumn_list):
        if v == True:
            if 0 <= i+control[level] <= M :
                update_volumn_list[i+control[level]] = True
            if 0 <= i-control[level] <= M :
                update_volumn_list[i-control[level]] = True
    dfs(update_volumn_list, level+1)


dfs(volumn_list, 0)
print(result)
