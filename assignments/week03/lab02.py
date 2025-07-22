# Complete this ATM simulation
# we use for when we know how many time we want to loop // and we use while when we don't know how many time we need to loop 
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print()
        print("=" * 50)
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        print("=" * 50)
        choice = input("Choose option: ")
        if choice == "1" :
            print(f"Your current balances are {balance}")
        elif choice == "2" :
            withdraw = float(input("Enter amount you want to withdraw : "))
            balance_temp = balance - withdraw 
            while True:
                if balance_temp < 0 :
                    print()
                    print("=" * 50)
                    print("Input Invalid, Please enter amount to withdraw again.")
                    withdraw = float(input("Enter amount you want to withdraw : "))
                    print("=" * 50)
                    balance_temp = balance - withdraw 
                else :
                    balance = balance_temp
                    print(f"Your current balance = {balance}")
                    print("-" * 50)
                    break 
        elif choice == "3" : 
            print("=" * 50)
            deposit = float(input("Enter amount you want to deposit : "))
            balance = balance + deposit
            print("=" * 50)
            print(f"Your current balance = {balance}")
            print("-" * 50)
        elif choice == "4" : 
            break
        else :
            print("Input Invalid")
            continue
                    
else:
    print("Invalid PIN")
