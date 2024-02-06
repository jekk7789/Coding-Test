def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[j]+numbers[i])
            answer = sorted(set(answer))
    return answer
result = solution([2,1,3,4,1])
print(result)