word = input().upper()
word_list = list(set(word)) #set함수를 사용하여 중복된 문자값 제거 후 변수에 저장
cnt = []
for i in word_list:
    cnt.append(word.count(i))
if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(word_list[cnt.index(max(cnt))])
