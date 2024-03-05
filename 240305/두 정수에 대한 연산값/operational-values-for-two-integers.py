a, b = tuple(map(int, input().split()))

def calcuator(a, b):
    if a > b:
        a += 25
        b *= 2
    
    else:
        a *= 2
        b += 25
    
    return a, b

a, b = calcuator(a, b)
print(a, b)