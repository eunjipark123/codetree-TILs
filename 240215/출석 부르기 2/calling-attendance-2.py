# pre = {1: 'John', 2: 'Tom', 3: 'Paul', 4: 'Sam'}

# while True:
#     n = int(input())
    
#     if n in pre.keys():
#         print(f"{pre[n]}")

#     else:
#         print("Vacancy")    
#         break


while True:
    n = int(input())

    if n == 1:
        print("John")
    elif n == 2:
        print("Tom")
    elif n == 3:
        print("Paul")
    elif n == 4:
        print("Sam")
    else:
        print("Vacancy")
        break