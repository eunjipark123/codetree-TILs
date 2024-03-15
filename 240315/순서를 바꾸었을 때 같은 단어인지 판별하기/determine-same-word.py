a = input()
b = input()

dict_a = {}
dict_b = {}

for elem in a:
    if elem not in dict_a:
        dict_a[elem] = 1
    
    else:
        dict_a[elem] += 1
    
for elem in b:
    if elem not in dict_b:
        dict_b[elem] = 1
    else:
        dict_b[elem] += 1

if dict_a == dict_b:
    print("Yes")
else:
    print("No")

# # 입력 
# a = input()
# b = input()



# # 정렬
# a = sorted(a)
# b = sorted(b)

# # 정렬된 값이 일치하면 조건을 만족
# if a == b:
#     print("Yes")
# else:
#     print("No")