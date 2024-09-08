n = int(input())
x = list(map(int, input().split()))
data = int(input())
result = 0
for i in x:
    if(i == data):
        result+=1
print(result)

    

