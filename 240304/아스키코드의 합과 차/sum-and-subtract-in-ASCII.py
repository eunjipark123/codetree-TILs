a, b = input().split()

ord_a = ord(a)
ord_b = ord(b)

print(ord_a + ord_b, end = " ")
print(ord_a - ord_b) if ord_a >= ord_b else print(ord_b - ord_a)