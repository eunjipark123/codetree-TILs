n = int(input())
arr = map(float, input().split())
sum_val = 0

# for i in arr:
#     sum_val += i

# avg = sum_val / n
# if avg >= 4.0:
#     grade = "Perfect"
# elif avg >= 3.0:
#     grade = "Good"
# else:
#     grade = "Poor"

# print(f"{avg:.1f}")
# print(grade)

sum_val = sum(arr)
avg = sum_val / n

print(f"{avg:.1f}")

if avg >= 4.0:
    print("Perfect")
elif avg >= 3.0:
    print("Good")
else:
    print("Poor")