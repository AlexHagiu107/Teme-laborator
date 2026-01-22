class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance  # atribut protejat (encapsulation)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print("Depunere reușită!")
        else:
            print("Suma trebuie să fie pozitivă")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print("Retragere reușită!")
        else:
            print("Fonduri insuficiente")

    def get_balance(self):
        return self._balance



initial_balance = float(input("Introdu soldul inițial: "))
account = BankAccount(initial_balance)

amount_deposit = float(input("Introdu suma pentru depunere: "))
account.deposit(amount_deposit)

amount_withdraw = float(input("Introdu suma pentru retragere: "))
account.withdraw(amount_withdraw)

print("Sold curent:", account.get_balance())
