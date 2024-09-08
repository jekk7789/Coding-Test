A,B = map(int, input().split())

A >= -10000 & B <= 10000 

if A > B :
    print(">")
elif A < B:
    print("<")
else:
    print("==")