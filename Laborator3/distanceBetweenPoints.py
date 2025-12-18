input_str = input("Introdu numere separate prin virgula: ")

# Convertim inputul intr-o lista de intregi
numere = [int(x.strip()) for x in input_str.split(",")]

maxim = max(numere)
minim = min(numere)

print("Lista:", numere)
print("Maximul este:", maxim)
print("Minimul este:", minim)
