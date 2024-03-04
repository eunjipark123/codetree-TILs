string = input()

for i in range(len(string)):
    if string[i] == 'e':
        result = string[:i] + string[i+1:]
        break

print(result)