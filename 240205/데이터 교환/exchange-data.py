# a, b, c = 5, 6, 7
# temp_c = c
# c = b
# b = a
# a = temp_c

# print(a)
# print(b)
# print(c)

a, b, c = 5, 6, 7
a, b, c = c, a, b

print(a)
print(b)
print(c)