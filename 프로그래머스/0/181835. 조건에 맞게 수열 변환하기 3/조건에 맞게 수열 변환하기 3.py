def solution(arr, k):
    answer = []
    for i in range(len(arr)):
        if(k % 2 == 0):
            answer.append(k + arr[i])
        else:
            answer.append(k * arr[i])
    return answer