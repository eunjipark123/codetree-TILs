students = []
for _ in range(5):
    name, h, w = input().split()
    h, w  = int(h), float(w)
    students.append((name, h, w))

# 이름 순
students.sort(key=lambda x: x[0])
print("name")
for name, h, w in students:
    print(f"{name} {h} {w:.1f}")

print()

students.sort(key=lambda x: -x[1])
print("height")
for name, h, w in students:
    print(f"{name} {h} {w:.1f}")