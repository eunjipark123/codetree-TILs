a, b = tuple(map(int, input().split()))

def is_prime(n):
    if n == 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False    

    return True

def prime_sum(a, b):
    sum_val = 0
    for i in range(a, b + 1):
        if is_prime(i):
            sum_val += i
    
    return sum_val

print(prime_sum(a, b))

# n = 17

# # is_prime = True
# # for i in range(2, n):
# #     if n % i == 0:
# #         is_prime = False
    
# # if is_prime:
# #     print("Prime")
# # else:
# #     print("Not Prime")

# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
    
#     return True

# if is_prime(n):
#     print("Prime")
# else:
#     print("Not Prime")