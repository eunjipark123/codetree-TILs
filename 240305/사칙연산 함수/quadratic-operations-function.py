a, o, c = input().split()
a, c = int(a), int(c)

def basic_operations(a, o, c):
    if o not in ('+', '-', '/', '*'):
        print(False)
    
    if o == '+':
        print(f"{a} + {c} = {a + c}")
    
    elif o == '-':
        print(f"{a} - {c} = {a - c}")

    elif o == '/':
        print(f"{a} / {c} = {a // c}")

    elif o == '*':
        print(f"{a} * {c} = {a * c}")

basic_operations(a, o, c)