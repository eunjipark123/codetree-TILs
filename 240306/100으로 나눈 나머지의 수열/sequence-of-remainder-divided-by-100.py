n = int(input())

def divider(a):
    if a == 1:
        return 2
    if a == 2:
        return 4

    num = divider(a-1) * divider(a-2)
    
    return num % 100


print(divider(n))