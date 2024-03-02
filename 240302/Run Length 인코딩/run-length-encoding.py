# 입력 받기 
string = input()
leng = len(string)

# 글자와 길이를 담을 리스트 만들기
letters = []
length = []

# 변수 설정
cnt = 1
val = ""

# letters, length 넣기
for i in range(leng):
    # 처음에는 글자만 넣어주기
    if i == 0:
        letters.append(string[i])
        continue
    
    # 다른 문자로 변경했을 때 리스트에 문자와 cnt수 추가
    if string[i] != string[i-1]:
        letters.append(string[i])
        length.append(cnt)
        cnt = 1    
        continue
    cnt += 1

# 마지막 글자 수 추가
length.append(cnt)

# run_length_encoding 만들어주기
for i in range(len(letters)):
    # letters, length 모두 
    val += str(letters[i]) 
    val += str(length[i])

# 출력
print(len(val))
print(val)