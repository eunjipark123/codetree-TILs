# 홀수여야 함
# 일의 자리가 5이면 안 됨
# 3으로 나눠떨어지지만 9로는 나눠떨어지지 않음

n = int(input())

for i in range(1, n + 1):
    if i % 2 != 0 and i % 10 != 5 and (i % 9 == 0 or i % 3 != 0):
        print(i, end = " ")
        continue