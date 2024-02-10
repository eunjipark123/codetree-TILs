arr = input().split()
h = int(arr[0])
w = int(arr[1])
bmi = int(w / ((h/100)**2))

print(bmi)
if bmi >= 25:
    print("Obesity")