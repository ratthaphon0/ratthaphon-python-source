"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""
currency = int(input("THB to USD(type 1) or USD to THB(type 2) : "))
amount = float(input("Enter amount of your money you want to convert : "))
if currency == 1 :
    converted = amount / 35.5
    print(f"{amount} / 35.5 = {converted:.2f}")
elif currency == 2 :
    converted = amount * 35.5
    print(f"{amount} * 35.5 = {converted:.2f}")
else :
    print("Input Error")
