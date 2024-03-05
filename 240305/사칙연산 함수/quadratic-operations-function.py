a, o, c = input().split()
a, c = int(a), int(c)

def plus(a, o, c):
    return a + c

def minus(a, o, c):
    return a - c

def devide(a, o, c):
    return a // c

def multiple(a, o, c):
    return a * c    

if o == "+":
    print(f"{a} + {c} = {plus(a, o, c)}")

elif o == "-":
    print(f"{a} - {c} = {minus(a, o, c)}")

elif o == "*":
    print(f"{a} * {c} = {multiple(a, o, c)}")    

elif o == "/":
    print(f"{a} / {c} = {devide(a, o, c)}")

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