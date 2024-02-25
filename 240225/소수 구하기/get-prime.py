n = int(input())

# for i in range(1, n + 1):
#     cnt = 0
#     for j in range(2, i):
#         if i % j == 0:
#             cnt += 1
    
#     if cnt == 0 and i != 1:
#         print(i, end = " ")
    

for i in range(1, n + 1):
    if i == 1:
        continue
    
    isprime = True

    for j in range(2, i):
        if i % j == 0:
            isprime = False
        
    if isprime:
        print(i, end =" ")