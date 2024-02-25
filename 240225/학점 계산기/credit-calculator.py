n = int(input())
arr = map(float, input().split())
sum_val = 0

for i in arr:
    sum_val += i

avg = sum_val / n
if avg >= 4.0:
    grade = "Perfect"
elif avg >= 3.0:
    grade = "Good"
else:
    grade = "Poor"

print(f"{avg:.1f}")
print(grade)