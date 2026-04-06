class BankAccount:
    bank_name = "Hassan Bank"
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposite(self,amount):
        self.balance += amount
        print(f"{amount} Deposited. New Balance: {self.balance}")
    def withdraw(self,amount):
        if amount > self.balance:
            print(f"Insufficient Balance. Your available balance: {self.balance}")
        else:
            self.balance -= amount
            print(f"{amount} withdraw. New Balance: {self.balance}")
    def show_info(self):
        print(f"\nAccount Owner: {self.owner}")
        print(f"Balance: {self.balance}")
        print(f"Bank Name: {BankAccount.bank_name}")
acc1 = BankAccount("Hassan",80000)
acc1.show_info()
acc1.deposite(20000)
acc1.show_info()
acc1.withdraw(50000)
acc1.show_info()
acc2 = BankAccount("Mohsan",80000)
acc2.show_info()