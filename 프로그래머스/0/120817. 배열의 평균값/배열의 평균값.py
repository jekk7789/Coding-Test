def solution(numbers):
    answer = 0
    for i in numbers:
        answer += i
    numbers_len = len(numbers)
    answers = answer / numbers_len
    return float(answers)