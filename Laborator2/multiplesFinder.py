x = int(input("Introdu numarul x: "))
y = int(input("Introdu numarul y: "))

print(f"Multiplii lui {x} mai mici decat {y} sunt:")

for i in range(x, y, x):
    print(i)
