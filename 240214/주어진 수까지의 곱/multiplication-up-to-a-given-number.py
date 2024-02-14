# 조건을 만족하는 곱 구하기
# prod 변수 설정
# for문에서 i값이 짝수일 때만 prod 값에 해당하는 숫자를 곱해주기
# prod를 1로 초기화하기

arr = input().split()
a, b = int(arr[0]), int(arr[1])
prod = 1

for i in range(a, b + 1):
    prod *= i

print(prod)