n = int(input())
def print_star_front(n):
    if n == 0:
        return

    print_star_front(n - 1)
    print(n, end = " ")

def print_star_backward(n):
    if n == 0:
        return

    print(n, end = " ")
    print_star_backward(n - 1)
    
def print_big_star(n):
    print_star_front(n)
    print()
    print_star_backward(n)

print_big_star(n)

# n = int(input())
# def print_triangle(n):
#     if n == 0:
#         return

#     print_triangle(n - 1)
#     print("*" * n)

# def print_triangle_backward(n):
#     if n == 0:
#         return

#     print("*" * n)
#     print_triangle_backward(n - 1)

# def print_triangle_set(n):
#     if n == 0:
#         return

    
#     print_triangle_set(n - 1)
#     print("*" * n)
#     print_triangle_set(n - 1)

# print_triangle(n)
# print()
# print_triangle_backward(n)
# print()
# print_triangle_set(n)