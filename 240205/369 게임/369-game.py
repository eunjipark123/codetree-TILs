# n = int(input())

# for i in range(1,n+1):
#     if i%3==0 or '3' in str(i) or '6' in str(i) or '9' in str(i):
#         print(0, end = ' ')
#     else:
#         print(i, end= ' ')


n = int(input())

for i in range(1, n+1):
    if i % 3 == 0:
        print("0", end=" ")
    elif i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        print("0", end=" ")
    elif i // 10 == 3 or i // 10 == 6 or i // 10 == 9:
        print("0", end=" ")
    else:
        print(i, end = " ")