# Input statements
salary = float(input(1250.0))
numDependents = float(input(2))

taxRate = 0.065
federalRate = 0.28
dependentRate = 0.025

stateTax = salary * taxRate
federalTax = salary * federalRate
dependentDeduction = salary * dependentRate
totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding

# output statements
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))