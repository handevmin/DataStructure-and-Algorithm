import sys

n = int(sys.stdin.readline())
memory = [0]*1000001
memory[1] = 1
memory[2] = 2
for i in range(3,n+1):
    memory[i] = (memory[i-1] + memory[i-2]) %15746
print(memory[n])
