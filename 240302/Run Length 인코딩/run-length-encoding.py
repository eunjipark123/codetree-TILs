string = input()
leng = len(string)
letters = []
length = []
run_length = []
cnt = 1

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

for i in range(len(letters)):
    run_length.append(letters[i])
    run_length.append(length[i])

print(len(run_length))
for elem in run_length:
    print(elem, end = "")