import sys

document = sys.stdin.readline().rstrip()
target = sys.stdin.readline().rstrip()
count =0
skip = 0
for i in range(len(document)):
    if skip == 0 and document[i:len(target)+i] == target:
        count+=1
        if len(target)!=1:
            skip = len(target)-1
    else:
        if skip ==0:
            continue
        else:
            skip-=1
print(count)


