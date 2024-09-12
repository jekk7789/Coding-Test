k = int(input())
ls = []
-1 <= k <= 100000

for i in range (k):
    n = int(input())
    if n == 0:
        ls.pop()
    else:
        ls.append(n)
result = sum(ls)

print(result)
