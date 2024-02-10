arr_a = input().split()
arr_b = input().split()

a_math = int(arr_a[0])
a_english = int(arr_a[1])

b_math = int(arr_b[0])
b_english = int(arr_b[1])

print(1 if a_math > b_math and a_english > b_english else 0)