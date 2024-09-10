a,b = map(int, input().split())
s_max = max(a,b)
s_min = min(a,b)
n = s_max - s_min
sum = (n*(n+1))//2
print(sum+s_min*(n+1))