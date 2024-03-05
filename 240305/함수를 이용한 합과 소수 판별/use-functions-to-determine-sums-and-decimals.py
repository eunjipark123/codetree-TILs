a, b = tuple(map(int, input().split()))

def is_prime(n):
    if n == 1:
        return False    
    for i in range(2, n):
        if n % i == 0:
            return False        
    return True 

def sum_digit(n):
    sum_digit = 0
    while n > 0:
         sum_digit += n % 10
         n //= 10
    
    return sum_digit

cnt = 0
for i in range(a, b + 1):
    if sum_digit(i) % 2 == 0 and is_prime(i):
        cnt += 1

print(cnt)