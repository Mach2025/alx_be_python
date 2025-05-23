# Personal Finance Calculator

monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: ")) 
monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings are: {monthly_savings}")
annual_savings = monthly_savings * 12

# Print the annual savings in a formatted string: “Your annual savings are: [annual_savings]”.
print(f"Your annual savings are: {annual_savings}")