while True:
    data = list(map(int, input())) 
    if data == [0]:
        break

    if data == list(reversed(data)):
        print("yes")
    else:
        print("no")
