y = int(input())

def leap_year(y):
    if y % 4 != 0:
        return False

    if y % 100 != 0:
        return True

    if y % 400 == 0:
        return True

    return False

if leap_year(y):
    print("true")
else:
    print("false")
    
# def is_leap_year(y):
#     if y % 4 != 0:
#         return False
    
#     if (y % 100) == 0 and (y % 400) != 0 :
#         return False
    
#     return True

# print("true") if is_leap_year(y) else print("false")
# def is_perfect_number(n):
#     if n % 2 == 0:
#         return False
#     if n % 10 == 5:
#         return False
#     if n % 3 == 0 and n % 9 != 0:
#         return False
    
#     return True

# if is_perfect_number(9):
#     print("Y")
# else:
#     print("N")