# Input values
employee_name = "Jenna Jerkins"
number_of_shifts = 15
number_of_transactions = 30
transaction_dollar_value = 25000

# Calculate productivity score
productivity_score = (transaction_dollar_value / number_of_transactions) / number_of_shifts

# Determine bonus using nested if statements
if productivity_score <= 30:
    bonus = 50.00
elif 31 <= productivity_score <= 69:
    bonus = 75.00
elif 70 <= productivity_score <= 199:
    bonus = 100.00
else:
    bonus = 200.00

# Output the results
print(f"Employee Name: {employee_name}")
print(f"Employee Bonus: ${bonus:.2f}")
