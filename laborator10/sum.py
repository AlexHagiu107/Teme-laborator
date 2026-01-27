def suma_din_fisier(nume_fisier):
    suma = 0.0

    try:
        with open(nume_fisier, "r", encoding="utf-8") as f:
            for nr_linie, linie in enumerate(f, start=1):
                linie = linie.strip()
                if linie:
                    suma += float(linie)  # ValueError va opri programul
        return suma

    except FileNotFoundError:
        print("Eroare: fișierul nu există!")
    except OSError as e:
        print(f"Eroare la citirea fișierului: {e}")


# codul rulează direct
nume = input("Introdu numele fișierului (ex: numere.txt): ").strip()
rezultat = suma_din_fisier(nume)

if rezultat is not None:
    print("Suma numerelor este:", rezultat)
