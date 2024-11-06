data = int(input())

for i in range(data):
    number = int(input())
    for j in range(2, 1_000_001):
        if(number % j == 0):
            print("NO")
            break
        if(j == 1_000_000):
            print("YES")
