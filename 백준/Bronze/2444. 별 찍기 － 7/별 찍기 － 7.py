x = int(input())
for i in range(1, x):
    print(" " * (x-i) + "*" * (2*i-1))

for j in range(x, 0, -1):
    print(" " * (x-j) + "*" * (2*j-1))