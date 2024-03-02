string = input()
back_str = []
for i in range(len(string)):
    if i % 2 == 1:
        back_str.append(string[i])
    
for elem in back_str[::-1]:
    print(elem, end = "")