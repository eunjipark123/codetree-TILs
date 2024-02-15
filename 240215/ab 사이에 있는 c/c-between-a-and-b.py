arr = input().split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

exists = False

for i in range(a, b + 1):
    if i % c == 0:
        exists = True
        break
    
print("YES") if exists == True else print("NO")