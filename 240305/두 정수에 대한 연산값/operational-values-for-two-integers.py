a, b = tuple(map(int, input().split()))

def calcuator(a, b):
    b += 25
    a *= 2
    
    return a, b

a, b = calcuator(a, b)
print(a, b)