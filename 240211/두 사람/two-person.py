arr_a = input().split()
arr_b = input().split()

a_age, a_sex = int(arr_a[0]), arr_a[1]
b_age, b_sex = int(arr_b[0]), arr_b[1]

if (a_age >= 19 and a_sex == 'M') or (b_age >= 19 and b_sex == 'M'):
    print(1)
else:
    print(0)