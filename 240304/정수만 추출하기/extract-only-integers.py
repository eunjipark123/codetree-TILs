a, b = input().split()


new_a = ""
new_b = ""
 
for char in a:
    if not char.isdecimal():
        break
    
    new_a += char


for char in b:
    if not char.isdecimal():
        break
    
    new_b += char

new_a = int(new_a)
new_b = int(new_b)

print(new_a + new_b)