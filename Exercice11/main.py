## Écrivez votre code ici !
class BankAccount:
    
    def __init__(self, account_holder, balance):
        self.account_holder=str(account_holder)
        self.balance=float(balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Le depot ne peut etre inferieur ou egal a zero")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Le montant de retrait depasse votre balance")

    def display_balance(self):
        print(f"Titulaire : {self.account_holder}")
        print(f"Solde : {self.balance:.2f}€")
