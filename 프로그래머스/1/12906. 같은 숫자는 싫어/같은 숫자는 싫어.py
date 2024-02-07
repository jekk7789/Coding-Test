def solution(arr):
    answer = []
    for i in range(len(arr)):
        answer.append(arr[i])
        if[arr[i]] == arr[i+1: i+2]:
            answer.pop()
    return answer
result = solution([1,1,3,3,0,1])
print(result)