n = int(input())
# share = n

# for i in range(1, n + 1):
#     if share // i <= 1:
#         print(i)
#         break
#     share //= i 

i = 1
while n > 1:
    n //= i
    i += 1

print(i-1)