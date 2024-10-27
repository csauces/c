employee_name = input("enter employee's name: ")
employee_shift_count = input("enter number of shifts employee has: ")
number_of_transactions = input("enter employees number of transactions: ")
dollar_value = input("enter transaction dollar value of employee: ")

#productivity score dividing an employees transactions dollar value number of transactions then dividing by the number of shifts worked.

employee_productivity = (dollar_value / number_of_transactions)
productivity_score = (employee_productivity / employee_shift_count)

print("Employee Name:" + employee_name)
print("Employee Bonus:" + productivity_score)
