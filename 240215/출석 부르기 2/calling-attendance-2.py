pre = {1: 'John', 2: 'Tom', 3: 'Paul', 4: 'Sam'}

while True:
    n = int(input())
    
    if n in pre.keys():
        print(f"{pre[n]}")

    else:
        print("Vacancy")    
        break