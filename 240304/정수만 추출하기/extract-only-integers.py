# 인덱스로 푸는 방식
a, b = input().split()

idx1 = 0
idx2 = 0

# a
for elem in a:
    if elem <= '9' and elem >= '0':
        idx1 += 1
    else:
        break

# b
for elem in b:
    if elem <= '9' and elem >= '0':
        idx2 += 1
    else:
        break

str1 = a[:idx1]
str2 = b[:idx2]

#숫자화
str1 = int(str1)
str2 = int(str2)

# 합계
print(str1 + str2)

# a, b = input().split()


# new_a = ""
# new_b = ""
 
# for char in a:
#     if not char.isdecimal():
#         break
    
#     new_a += char


# for char in b:
#     if not char.isdecimal():
#         break
    
#     new_b += char

# new_a = int(new_a)
# new_b = int(new_b)

# print(new_a + new_b)