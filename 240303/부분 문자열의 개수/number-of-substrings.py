# 입력값 
a = input()
b = input()

# 입력 문자의 길이
len_a = len(a)
len_b = len(b)

# 갯수 셀 변수
cnt = 0

# 갯수 세기 : 범위가 일치하면 cnt 에 1을 추가하는 방식으로 카운트
for i in range(len_a - len_b + 1):
    if a[i:i+len_b] == b:
        cnt += 1

print(cnt)