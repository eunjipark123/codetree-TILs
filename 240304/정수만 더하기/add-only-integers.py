a = input()

sum_val = 0 

for char in a:
    if char.isnumeric():
        sum_val += int(char)

print(sum_val)