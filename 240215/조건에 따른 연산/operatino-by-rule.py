n = int(input())

cnt = 0

while True:
    if n >= 1000:
        print(cnt)
        break
    
    cnt += 1
    
    if n % 2 == 0:
        n = 3 * n + 1

    else:
        n = n * 2 + 2