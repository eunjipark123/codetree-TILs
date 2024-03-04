# 입력
a = input()
b = input()

# 숫자만 가져오기
str_a = "".join(char for char in a if char >= '0' and char <= '9')        
str_b = "".join(char for char in b if char >= '0' and char <= '9')

# 정수화
num_a = int(str_a)
num_b = int(str_b)

# 출력
print(num_a + num_b)