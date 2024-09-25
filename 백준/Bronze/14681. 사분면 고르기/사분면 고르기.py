x = int(input())
y = int(input())


if(x > 0 and y > 0):
    print("1") # 제 1사분면
elif(x < 0 and y > 0):
    print("2") # 제 2사분면
elif(x < 0 and y < 0):
    print("3") #제 3사분면
else:
    print("4") #제 4사분면
