# input statements
salary = float(input())
numDependents = float(input())

# calculate taxes here
# the decimals are the tax rates
stateTax = 0.065 * salary
federalTax = 0.28 * salary
dependentDeduction = 0.025 * salary * numDependents
totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding

# output statements
# I followed the salary and take home pay print formating for the others
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependents: $" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))