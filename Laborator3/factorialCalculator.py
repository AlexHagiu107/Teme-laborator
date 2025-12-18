def factorial(n):
    if n < 0:
        return None
    rezultat = 1
    for i in range(1, n + 1):
        rezultat *= i
    return rezultat

numar = int(input("Introdu un număr întreg: "))
fact = factorial(numar)

if fact is None:
    print("Factorialul nu este definit pentru numere negative.")
else:
    print(f"Factorialul lui {numar} este {fact}.")
