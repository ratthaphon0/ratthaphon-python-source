"""
Personal Finance Calculator
Student: Ratthaphon Khan
Date: 22/07/2568
Purpose: Calculate monthly budget and savings
"""
def get_user_input():
    monthly_income = float(input("User's monthly income in THB : "))
    rent_cost = float(input("Monthly rent/housing cost : "))
    food_budget = int(input("Monthly food budget in THB : "))
    transportation_cost = float(input("Monthly transportation expenses : "))
    entertainment_budget = int(input("Monthly entertainment budget : "))
    emergency_fund_percent = float(input("Percentage to save for emergency (e.g., 10.5) : "))
    investment_percent = float(input("Percentage to invest (e.g., 15.0) : "))
    return monthly_income, rent_cost, food_budget, transportation_cost, entertainment_budget, emergency_fund_percent,investment_percent

def total_fixed_expenses(rent_cost,transportation_cost):
    return rent_cost + transportation_cost


def total_variable_expenses(food_budget,entertainment_budget):
    return food_budget + entertainment_budget

    
def total_expenses(total_fixed_expenses,total_variable_expenses):
    return total_fixed_expenses + total_variable_expenses

    
def remaining_income(monthly_income,total_expenses):
    return monthly_income - total_expenses


def calculate_savings(monthly_income,emergency_fund_percent,investment_percent,remaining):
    emergency = monthly_income * (emergency_fund_percent / 100)
    investment = monthly_income * (investment_percent / 100)
    available = remaining - emergency - investment
    return emergency, investment, available

    
def expense_ratio(total_expenses,monthly_income):
    expense_ratio = (total_expenses / monthly_income) * 100
    return expense_ratio
    
    
def main():
    monthly_income, rent_cost, food_budget, transportation_cost, entertainment_budget, emergency_fund_percent,investment_percent = get_user_input()
    fixed = total_fixed_expenses(rent_cost,transportation_cost)
    variable = total_variable_expenses(food_budget, entertainment_budget)
    total_exp = total_expenses(fixed, variable)
    remaining = remaining_income(monthly_income, total_exp)
    emergency, investment, available = calculate_savings(monthly_income,emergency_fund_percent,investment_percent,remaining)
    
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
    
main()