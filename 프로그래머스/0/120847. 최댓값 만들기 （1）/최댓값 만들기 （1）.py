def solution(numbers):
    numbers.sort() 
    answer = 0
    a = numbers[-1]
    b = numbers[-2]
    answer = a*b
    return answer