# cnt 0으로 초기화
cnt = 0

# 반복문을 통해 홀수만 카운트하도록 설정
for _ in range(10):
    n = int(input())
    if n % 2 == 1:
        cnt += 1

print(cnt)