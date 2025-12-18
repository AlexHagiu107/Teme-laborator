numbers = input("Introdu lista de numere separate prin spațiu: ")
numbers = [int(x) for x in numbers.split()]
target = int(input("Introdu valoarea țintă: "))

pairs = set()
seen = set()

for num in numbers:
    complement = target - num
    if complement in seen:
        pairs.add(tuple(sorted((num, complement))))
    seen.add(num)

print("Perechi unice:", pairs)
