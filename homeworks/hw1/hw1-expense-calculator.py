"""
Personal Finance Calculator
Student: Ratthaphon Khan
Date: 22/07/2568
Purpose: Calculate monthly budget and savings
"""

#function to get income and outcome from user
def get_user_input(): 
    monthly_income = float(input("User's monthly income in THB : "))
    rent_cost = float(input("Monthly rent/housing cost : "))
    food_budget = int(input("Monthly food budget in THB : "))
    transportation_cost = float(input("Monthly transportation expenses : "))
    entertainment_budget = int(input("Monthly entertainment budget : "))
    emergency_fund_percent = float(input("Percentage to save for emergency (e.g., 10.5) : "))
    investment_percent = float(input("Percentage to invest (e.g., 15.0) : "))
    return monthly_income, rent_cost, food_budget, transportation_cost, entertainment_budget, emergency_fund_percent,investment_percent

#function to calculate total fixed expenses per month
def total_fixed_expenses(rent_cost,transportation_cost): 
    return rent_cost + transportation_cost

#function to calculate total variable expenses per month 
def total_variable_expenses(food_budget,entertainment_budget):
    return food_budget + entertainment_budget

#function to calculate total expenses (fixed + variable) per month    
def total_expenses(total_fixed_expenses,total_variable_expenses):
    return total_fixed_expenses + total_variable_expenses

#function to calculate remaining income after subtract total expenses
def remaining_income(monthly_income,total_expenses):
    return monthly_income - total_expenses

#function to calculate emergency and investment fund per month then will tell remaining money for saving
def calculate_savings(monthly_income,emergency_fund_percent,investment_percent,remaining):
    emergency = monthly_income * (emergency_fund_percent / 100) #calculate emergency fund from user emergency percentage given
    investment = monthly_income * (investment_percent / 100)#calculate investment fund from user investment percentage given
    available = remaining - emergency - investment #calculate available money after deducted emergency and investment fund
    return emergency, investment, available

#function to calculate expense ratio
def expense_ratio(total_exp,monthly_income):
    return (total_exp / monthly_income) * 100
    
#main function
def main():
    #call function and store values in each variable
    monthly_income, rent_cost, food_budget, transportation_cost, entertainment_budget, emergency_fund_percent,investment_percent = get_user_input()
    fixed = total_fixed_expenses(rent_cost,transportation_cost)
    variable = total_variable_expenses(food_budget, entertainment_budget)
    total_exp = total_expenses(fixed, variable)
    remaining = remaining_income(monthly_income, total_exp)
    emergency, investment, available = calculate_savings(monthly_income,emergency_fund_percent,investment_percent,remaining)
    expense_rat = expense_ratio(total_exp,monthly_income)
    
    #display to user
    print("=== MONTHLY BUDGET REPORT ===")
    print(f"\nIncome: {monthly_income:.2f} THB")
    print(f"Fixed Expenses: {fixed:.2f} THB")
    print(f"Variable Expenses: {variable:.2f} THB")
    print(f"Total Expenses: {total_exp:.2f} THB")
    print(f"Remaining: {remaining:.2f} THB")
    print("\n\n=== SAVINGS BREAKDOWN ===")
    print(f"Emergency Fund ({emergency_fund_percent}): {emergency:.2f} THB")
    print(f"Investment ({investment_percent}): {investment:.2f} THB")
    print(f"Available for Savings: {available:.2f} THB")
    print("\n=== ANALYSIS ===")
    print(f"Expense Ratio: {expense_rat:.2f}%")   
    
#call function main
main()