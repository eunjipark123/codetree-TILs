arr_a = input().split()
arr_b = input().split()
arr_c = input().split()

a_sym, a_temp = arr_a[0], int(arr_a[1])
b_sym, b_temp = arr_b[0], int(arr_b[1])
c_sym, c_temp = arr_c[0], int(arr_c[1])

p = 0

# if a_sym == "Y" and a_temp >= 37:
#     p += 1
# if b_sym == "Y" and b_temp >= 37:
#     p += 1    
# if c_sym == "Y" and c_temp >= 37:
#     p += 1        

# if p >= 2:
#     print("E")
# else:
#     print("N")


if a_sym == 'Y' and a_temp >= 37:
    if (b_sym == 'Y' and b_temp >= 37) or (c_sym == 'Y' and c_temp >= 37):
        print("E")
    else:
        print("N")
else:
    if (b_sym == 'Y' and b_temp >= 37) and (c_sym == 'Y' and c_temp >= 37):
        print("E")
    else:
        print("N")