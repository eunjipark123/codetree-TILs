a_arr = input().split()
b_arr = input().split()

a_math = int(a_arr[0])
a_eng = int(a_arr[1])

b_math = int(b_arr[0])
b_eng = int(b_arr[1])

# if a_math > b_math:
#     print("A")
# elif a_math < b_math:
#     print("B")
# elif a_eng > b_eng:
#     print("A")
# else:
#     print("B")

if a_math > b_math or (a_math == b_math and a_eng > b_eng):
    print("A")
else:
    print("B")