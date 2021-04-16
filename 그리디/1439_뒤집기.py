import sys

S = sys.stdin.readline()

count_one = 0
count_zero = 0

flag_one = False
flag_zero = False

for i in S:
    if i == '1':
        flag_zero = False
        if flag_one == False:
            count_one += 1
        flag_one = True
    elif i == '0' and flag_zero == False:
        flag_one = False
        if flag_zero == False:
            count_zero += 1
        flag_zero = True

print(min(count_one, count_zero))