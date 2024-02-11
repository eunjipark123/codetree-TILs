a = int(input())

# if a >= 3 and a < 6:
#     print("Spring")
# elif a >= 6 and a < 9:
#     print("Summer")
# elif a >= 9 and a < 12:
#     print("Fall")
# else:
#     print("Winter")

if a >= 12 or a < 3:
    print("Winter")
elif a < 6:
    print("Spring")
elif a < 9:
    print("Summer")
else:
    print("Fall")