cnt = 0
while True:
    n = int(input())
    
    if n % 2 == 1:
        continue
    
    cnt += 1
    print(n//2)
    
    if cnt >= 3:
        break