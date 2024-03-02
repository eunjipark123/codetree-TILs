str_all = ""

n = int(input())

string = input().split()

for s in string:
    str_all += s

leng = len(str_all)    

for i in range(leng):
    print(str_all[i], end ="")
    if (i + 1) % 5 == 0:
        print()

# n = int(input())

# string = input().split()
# new_string = ""
# for i in string:
#     new_string += i 

# if len(new_string)%5 == 0:
#     n = len(new_string) // 5
    
#     for i in range(n):
#         for j in range(5):
#             print(new_string[i * 5 + j], end = "")
#         print()

# else:
#     n = len(new_string) // 5 + 1
#     m = len(new_string) % 5

#     for i in range(n):
#         if i < n-1:
#             for j in range(5):
#                 print(new_string[i * 5 + j], end = "")

#         else:
#             for j in range(m):
#                 print(new_string[i * 5 + j], end = "")
        
#         print()