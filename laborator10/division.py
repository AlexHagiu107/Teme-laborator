def imparte(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Eroare: nu se poate împărți la zero!")
        return None


a = float(input("Introdu primul număr (a): "))
b = float(input("Introdu al doilea număr (b): "))

rezultat = imparte(a, b)
if rezultat is not None:
    print("Rezultat:", rezultat)
