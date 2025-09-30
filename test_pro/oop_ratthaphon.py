class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def Deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Transaction successful: {amount} deposited. Current balance is now: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def Withdrawal(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Transaction successful: {amount} withdrawn. Remaining balance: {self.balance}")
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def bankFees(self):
        fee_percentage = 5/100
        fees = self.balance * fee_percentage
        self.balance -= fees
        print(f"Bank fees of {fees} applied to your account. Updated balance: {self.balance}")

    def display(self):
        print("\n--- Account Details ---")
        print(f"Account Number: {self.accountNumber}")
        print(f"Account Owner: {self.name}")
        print(f"Current Balance: {self.balance}")
        print("---------------------")


if __name__ == "__main__":
    account1 = BankAccount(2519, "Ashif Khan", 1000)
    account1.display()
    account1.Deposit(500)
    account1.Withdrawal(200)
    account1.Withdrawal(2000)
    account1.bankFees()
    account1.display()