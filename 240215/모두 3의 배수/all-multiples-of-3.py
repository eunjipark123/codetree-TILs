satisfied = True

for _ in range(5):
    n = int(input())

    if n % 3 != 0:
        satisfied = False
        break
    
print(1) if satisfied == True else print(0)