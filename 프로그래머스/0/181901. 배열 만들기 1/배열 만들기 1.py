def solution(n, k):
    answer = []
    for i in range(n):
        m = k * (i+1)
        
        if(m > n):
            break
        answer.append(m)
    return answer