a, o, c = input().split()
a, c = int(a), int(c)

def plus(a, c):
    return a + c

def minus(a, c):
    return a - c

def devide(a, c):
    return a // c

def multiple(a, c):
    return a * c    

if o == "+":
    print(f"{a} + {c} = {plus(a, c)}")

elif o == "-":
    print(f"{a} - {c} = {minus(a, c)}")

elif o == "*":
    print(f"{a} * {c} = {multiple(a, c)}")    

elif o == "/":
    print(f"{a} / {c} = {devide(a, c)}")

else:
    print(False)

# 틀린 풀이 
# def basic_operations(a, o, c):
#     if o not in ('+', '-', '/', '*'):
#         print(False)
    
#     if o == '+':
#         print(f"{a} + {c} = {a + c}")
    
#     elif o == '-':
#         print(f"{a} - {c} = {a - c}")

#     elif o == '/':
#         print(f"{a} / {c} = {a // c}")

#     elif o == '*':
#         print(f"{a} * {c} = {a * c}")

# basic_operations(a, o, c)