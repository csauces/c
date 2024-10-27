employee_name = input("enter employee's name: ")
employee_shift_count = int(input("enter number of shifts employee has: "))
number_of_transactions = int(input("enter employees number of transactions: "))
dollar_value = float(input("enter transaction dollar value of employee: "))

employee_productivity = dollar_value / number_of_transactions

productivity_score = employee_productivity / employee_shift_count
if productivity_score <= 30:
    productivity_score = 50.00
elif 31 <= productivity_score <= 69:
    productivity_score = 75.00
elif 70 <= productivity_score < 200:
    productivity_score = 100.00
elif productivity_score >= 200:
    productivity_score = 200.00

print("Employee Name:" + employee_name)
print("Employee Bonus:" + "$" + str(productivity_score))
