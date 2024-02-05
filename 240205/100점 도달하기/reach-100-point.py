# score = int(input())

# while score <= 100:
#     if score >= 90:
#         print("A", end=" ")
#     elif score >= 80:
#         print("B", end=" ")
#     elif score >= 70:
#         print("C", end=" ")
#     elif score >= 60:
#         print("D", end=" ")
#     else:
#         print("F", end=" ")

#     score = score + 1

score = int(input())

for i in range(score, 101):
    if i >= 90:
        print("A", end=" ")
    elif i>= 80:
        print("B", end=" ")
    elif i>= 70:
        print("C", end=" ")
    elif i>= 60:
        print("D", end=" ")
    else:
        print("F", end=" ")