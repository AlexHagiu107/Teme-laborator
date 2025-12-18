principal = float(input("Introdu suma initiala (principalul): "))
rata = float(input("Introdu rata anuala a dobanzii (%): "))
timp = float(input("Introdu timpul (in ani): "))

dobanda = (principal * rata * timp) / 100

print("Dobanda calculata este:", dobanda)
