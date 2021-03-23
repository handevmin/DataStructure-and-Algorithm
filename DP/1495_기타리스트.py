import sys

N, S, M = map(int, sys.stdin.readline().split())
control = list(map(int, sys.stdin.readline().split()))
volumn_list = [-1]
def dfs(volumn, level):
    if level == N:
        volumn_list.append(volumn)
        return

    for i in range(level, len(control)):
        if volumn+control[i] > M:
            pass
        else:
            dfs(volumn+control[i], level+1)

        if volumn-control[i] < 0:
            return
        else:
            dfs(volumn-control[i], level+1)
dfs(S, 0)
print(max(volumn_list))