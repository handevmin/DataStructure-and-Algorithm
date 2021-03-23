import sys

origin_seq = sys.stdin.readline().rstrip()
target_seq = sys.stdin.readline().rstrip()
length = [[0] * (len(origin_seq)+1) for j in range(len(target_seq)+1) ]
max_length = [0]*len(origin_seq)
k = 0
for i in range(1, len(target_seq)+1):
    for j in range(1, len(origin_seq)+1):
        if origin_seq[j-1] == target_seq[i-1]:
            k = length[i-1][j-1]+1
            length[i][j] = k
            max_length[j - 1] = max(max_length[j - 1], max(length[i][:j + 1]))
            continue
        max_length[j-1] = max(max_length[j-1], max(length[i][:j+1]))
        length[i][j] = max_length[j-1]
print(length[len(target_seq)][len(origin_seq)])
