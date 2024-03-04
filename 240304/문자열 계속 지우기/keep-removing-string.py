# # 문자열 입력 
# a = input()
# b = input()
# len_b = len(b)

# while True:   
#     flag = False
#     for i in range(len(a)):
#         if a[i:i + len_b] == b:            
#             flag = True
#             a = a[:i] + a[i+len_b:]
                            
#     if not flag:
#         print(a)
#         break


# 문자열 입력 
a = input()
b = input()

while a.find(b) != -1:
    start_idx = a.find(b)
    a = a[:start_idx] + a[start_idx + len(b):]

print(a)