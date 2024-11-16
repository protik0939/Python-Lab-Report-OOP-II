# Scenario: A company has two types of employees: PermanentEmployee and ContractEmployee.
# Both employee types have some shared details, such as name and id, but differ in how their
# salaries are calculated. Permanent employees have a fixed monthly salary, while contract
# employees are paid based on the number of hours worked.
#---------------------------
# Question:
# Define a base class Employee with attributes name and id. Create two derived classes,
# PermanentEmployee and ContractEmployee, that inherit from Employee. The
# PermanentEmployee class should have a method calculate_salary() that returns a fixed monthly
# salary, while ContractEmployee should have a method calculate_salary() that calculates salary
# based on hourly rate and hours worked. Demonstrate this setup with appropriate test data.
#---------------------------
# Answer:
#---------------------------


# Base class
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_details(self):
        return f"Employee Name: {self.name}, ID: {self.emp_id}"

# Derived class for permanent employees
class PermanentEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

# Derived class for contract employees
class ContractEmployee(Employee):
    def __init__(self, name, emp_id, hourly_rate, hours_worked):
        super().__init__(name, emp_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

# Test data
# Permanent Employee
perm_emp = PermanentEmployee(name="Mr X", emp_id=4, monthly_salary=5000)
print(perm_emp.display_details())
print(f"Permanent Employee Monthly Salary: ${perm_emp.calculate_salary()}")

# Contract Employee
cont_emp = ContractEmployee(name="Mr Y", emp_id=3, hourly_rate=20, hours_worked=120)
print(cont_emp.display_details())
print(f"Contract Employee Salary: ${cont_emp.calculate_salary()}")
