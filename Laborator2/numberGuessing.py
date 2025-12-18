import random

numar_secret = random.randint(1, 20)
incercari = 5

print("Am ales un numar intre 1 si 20. Ai 5 incercari sa-l ghicesti!")

for i in range(incercari):
    ghicire = int(input("Introdu numarul tau: "))

    if ghicire < numar_secret:
        print("Prea mic")
    elif ghicire > numar_secret:
        print("Prea mare")
    else:
        print("Corect! Ai ghicit numarul!")
        break
else:
    print("Ai ramas fara incercari. Numarul era:", numar_secret)
