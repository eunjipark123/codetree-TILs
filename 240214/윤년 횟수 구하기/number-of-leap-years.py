# 입력값 받기
n = int(input())

# cnt변수 초기화 설정
cnt = 0

for i in range(1, n+1):
    if i % 400 == 0:
        cnt += 1
    elif i % 100 == 0:
        cnt += 0
    elif i % 4 == 0:
        cnt += 1

print(cnt)