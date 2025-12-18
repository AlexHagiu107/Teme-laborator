input_str = input("Introdu valori separate prin virgula: ")

# Cream tupla
tupla = tuple(int(x.strip()) for x in input_str.split(","))

valoare = int(input("Introdu valoarea cautata: "))

if valoare in tupla:
    index = tupla.index(valoare)
    print("Tupla:", tupla)
    print(f"{valoare} se regaseste in tupla la indexul {index}.")
else:
    print("Tupla:", tupla)
    print(f"{valoare} NU se regaseste in tupla.")
