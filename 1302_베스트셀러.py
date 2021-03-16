import sys

amount = int(sys.stdin.readline())
sell = {}
bestseller = []
for i in range(amount):
    book = sys.stdin.readline().rstrip()
    if book not in sell:
        sell[book] = 1
    else:
        sell[book] +=1

for j in sell:
    if sell[j] == max(sell.values()):
        bestseller.append(j)
bestseller.sort()
print(bestseller[0])