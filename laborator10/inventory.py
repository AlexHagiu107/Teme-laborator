def adauga_produs(inventar, nume, cantitate):
    if cantitate < 0:
        raise ValueError("Cantitatea nu poate fi negativă!")
    if nume in inventar:
        raise ValueError("Produsul există deja! Folosește opțiunea de actualizare.")
    inventar[nume] = cantitate


def cauta_produs(inventar, nume):
    if nume not in inventar:
        raise KeyError("Produs inexistent!")
    return inventar[nume]


def actualizeaza_cantitate(inventar, nume, cantitate):
    if nume not in inventar:
        raise KeyError("Produs inexistent!")
    if cantitate < 0:
        raise ValueError("Cantitatea nu poate fi negativă!")
    inventar[nume] = cantitate


def afiseaza_inventar(inventar):
    if not inventar:
        print("Inventarul este gol.")
        return
    print("\n--- INVENTAR ---")
    for nume, cantitate in inventar.items():
        print(f"{nume}: {cantitate}")
    print("----------------\n")


inventar = {}

while True:
    print("Meniu:")
    print("1. Adaugă produs")
    print("2. Caută produs după nume")
    print("3. Actualizează cantitatea unui produs")
    print("4. Afișează inventarul")
    print("0. Ieșire")

    optiune = input("Alege o opțiune: ").strip()

    try:
        if optiune == "1":
            nume = input("Nume produs: ").strip()
            cantitate = int(input("Cantitate: "))
            adauga_produs(inventar, nume, cantitate)
            print("Produs adăugat cu succes!")

        elif optiune == "2":
            nume = input("Nume produs de căutat: ").strip()
            cant = cauta_produs(inventar, nume)
            print(f"Produsul '{nume}' are cantitatea: {cant}")

        elif optiune == "3":
            nume = input("Nume produs de actualizat: ").strip()
            cantitate = int(input("Noua cantitate: "))
            actualizeaza_cantitate(inventar, nume, cantitate)
            print("Cantitate actualizată cu succes!")

        elif optiune == "4":
            afiseaza_inventar(inventar)

        elif optiune == "0":
            print("La revedere!")
            break

        else:
            print("Opțiune invalidă! Încearcă din nou.")

    except ValueError as e:
        print("Eroare:", e)
    except KeyError as e:
        print("Eroare:", e)
