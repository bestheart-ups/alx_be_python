monthly_income = int(input("enter your monthly income;" ))
monthly_expenses = int(input("enter your total monthly expenses:" ))
monthly_savings = monthly_income - monthly_expenses
project_savins = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print(f"your monthly savings are ${monthly_savings}")
print(f"projected savings after one year, with interest is: ${projected_savings}")