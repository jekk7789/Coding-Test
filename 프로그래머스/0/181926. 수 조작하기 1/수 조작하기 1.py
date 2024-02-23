def solution(n, control):
    m = list(control)
    for i in range(len(m)):
        if(m[i] == "w"):
            n += 1
        elif(m[i] == "s"):
            n -= 1
        elif(m[i] == "d"):
            n += 10
        elif(m[i] == "a"):
            n -= 10

    return n