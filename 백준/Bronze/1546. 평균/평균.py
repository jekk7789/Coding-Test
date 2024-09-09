x = int(input())
n = list(map(float, input().split()))
result = 0
m = max(n)

for i in range(x):
    result += n[i]/m*100

print(result/x)