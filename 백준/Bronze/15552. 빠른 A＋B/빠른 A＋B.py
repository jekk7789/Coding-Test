import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    result = 0
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)

   