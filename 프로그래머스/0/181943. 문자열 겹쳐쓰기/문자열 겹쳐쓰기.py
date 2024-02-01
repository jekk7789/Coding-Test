def solution(my_string, overwrite_string, s):
    str1 = my_string[:s]
    str2 = my_string[s+len(overwrite_string):]
    answer = str1 + overwrite_string + str2
    return answer