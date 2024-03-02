arr = [input() for _ in range(10)]
letter = input()

for elem in arr:
    if elem[-1] == letter:
        print(elem)