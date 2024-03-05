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

def judge_number(n):
    if sum_digit(i) % 2 == 0 and is_prime(i):
        return True
    
    return False 

cnt = 0
for i in range(a, b + 1):
    if judge_number(i):
        cnt += 1

print(cnt)