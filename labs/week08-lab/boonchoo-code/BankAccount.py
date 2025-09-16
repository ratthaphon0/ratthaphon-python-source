class BankAccount:
    
    def __init__(self, account_number, initial_balance=0):# (constructer method     )
        self.account_number = account_number
        self.__balance = initial_balance  # Private attribute
        self.__transaction_history = []   # Private attribute
    
    # Public method to access private balance
    def get_balance(self):
        return self.__balance
     
    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transaction_history.append(f"Deposit: +${amount}")
            return True
        return False
    
    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transaction_history.append(f"Withdrawal: -${amount}")
            return True
        return False
    
    # Property decorator for read-only access
    @property
    def transaction_history(self):
        return self.__transaction_history.copy()
    
    def __str__(self): #__ชื่อ__ เป็นmethod ที่ทำให้ printข้อมูลที่อยู่ใน class ได้(account)
        return f"Account {self.account_number}: Balance ${self.__balance}"

# Usage example
account = BankAccount("12345", 1000)
account.balance = 500000 
"""อันนี้คือ การ hack ข้อมูล โปรแกแรมที่ดีไม่ควรเปิดโอกาศให้เข้าถึงแก้ไขข้อมูลได้ง่าย 
ใช้ __หน้าชื่อตัวแปรทำให้เข้าถึงข้อมูลโดยตรงไม่ได้
Encapsulation ใน oop ช่วยในการปกป้องข้อมูลอ่อนไหมได้ แต่ถ้าไม่ใช้ oop ต้องป้องกันเอง """

print(account.get_balance())  # 1000
account.deposit(500)
account.withdraw(200)
print(account)  # Account 12345: Balance $1300