while True:    
    word = input()
    result = 0
    if word == '#':
        break
    for i in word:
        if i in ['a','e','i','o','u','A','E','I','O','U']:
            result += 1
    print(result)