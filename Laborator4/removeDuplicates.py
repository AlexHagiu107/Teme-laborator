input_str = input("Introdu numere separate prin virgula: ")

numere = [int(x.strip()) for x in input_str.split(",")]

lista_unica = []
for numar in numere:
    if numar not in lista_unica:
        lista_unica.append(numar)

print("Lista fara duplicate:", lista_unica)
