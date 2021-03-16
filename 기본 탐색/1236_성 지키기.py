import sys

N, M = map(int, sys.stdin.readline().split())
castle = []
for i in range(N):
    castle.append(list(sys.stdin.readline().rstrip()))

def counting(castle, row_num):
    result = 0
    for i in castle:
        count = 0
        for j in i:
            if j == 'X':
                break
            else:
                count+=1
        if count == row_num:
            result +=1
    return result

col_result = counting(castle, M)

trans_castle = []
for i in range(M):
    trans_castle_row = []
    for j in range(N):
        trans_castle_row.append(castle[j][i])
    trans_castle.append(trans_castle_row)

row_result = counting(trans_castle, N)

print(max(col_result, row_result))