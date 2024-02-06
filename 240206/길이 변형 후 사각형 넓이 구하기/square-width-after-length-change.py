# # 사칙연산 다른 표현으로 사용하기
# a, b = 9, 4
# a += 5
# print(a)
# a %= b
# print(a, b)
# b *= 3
# print(b)


# 입력 받기 
arr = input().split()
a = int(arr[0])
b = int(arr[1])

# 가로, 세로 길이 변경 
a += 8
b *= 3

# 출력
print(a)
print(b)
print(a * b)