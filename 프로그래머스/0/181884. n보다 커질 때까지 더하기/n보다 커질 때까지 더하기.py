def solution(numbers, n):
    answer = 0
    for i in range(len(numbers)):
        answer += numbers[i]
        if(answer > n):
            return answer
        elif(answer < n):
            continue
    return answer