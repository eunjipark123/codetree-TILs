m = int(input())

for _ in range(m):
    n = int(input())
    cnt = 0
    # while True:
    #     if n == 1:
    #         print(cnt)
    #         break
    #     elif n % 2 == 0:
    #         n //= 2
    #     else:
    #         n = n * 3 + 1
    #     cnt += 1


    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
        
        cnt += 1
    
    print(cnt)