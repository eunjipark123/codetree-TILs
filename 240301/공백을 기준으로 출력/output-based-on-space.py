a = input()
b = input()
c = a + b

for elem in c:
    if elem == " ":
        print("", end = "")
    else:
        print(elem, end = "")