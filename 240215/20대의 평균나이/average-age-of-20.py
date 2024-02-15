sum_val = 0
cnt = 0

# while True:
#     n = int(input())

#     if n >= 20 and n < 30:
#         cnt += 1
#         sum_val += n
#     else:
#         break

# avg = sum_val / cnt

# print(f"{avg:.2f}")

while True:
    n = int(input())

    if n >= 30 or n < 20:
        print(f"{sum_val/cnt:.2f}")
        break
    
    cnt += 1
    sum_val += n