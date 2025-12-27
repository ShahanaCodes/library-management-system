#atm.__balance
'''class Employee:
    def __init__(self, emp_id, name, salary):
        self.__emp_id = emp_id  #private
        self.__name = name
        self.__salary = salary
    #getter methods
    def get_employee_info(self):
        return (f"ID: {self.__emp_id}, Name: {self.__name}, salary:{self.__salary}"
    def get_salary(self):
        return self.__salary


    #setter methods (with validation)
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
            print(f"salary updated to {new_salary}")
        else:
            print("invalid salary amount")
#encapsulation bonus calculation
    def calculate_bonus(self, performance_rating):
        if performance_rating == "excellent":
            return self.__salary * 0.2
        elif performance_rating == "good":
            return self.__salary * 0.1
        else:
            return self.__salary * 0.05

#using the class
emp1 = Employee(emp_id: 101, name: "saha", salary: 50000)

print(emp1.get_employee_info())  #access safely

emp1.set_salary(55000)
print(emp1.get_employee_info()) #update safely

bonus = emp1.calculate_bonus("excellent")'''  #invalid


'''class Employee:
    def __init__(self, emp_id, name, salary):
        self.__emp_id = emp_id      # private
        self.__name = name          # private
        self.__salary = salary      # private

    # getter method
    def get_employee_info(self):
        return f"ID: {self.__emp_id}, Name: {self.__name}, Salary: {self.__salary}"

    def get_salary(self):
        return self.__salary

    # setter method (with validation)
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
            print(f"Salary updated to {new_salary}")
        else:
            print("Invalid salary amount")

    # encapsulated bonus calculation
    def calculate_bonus(self, performance_rating):
        if performance_rating == "excellent":
            return self.__salary * 0.2
        elif performance_rating == "good":
            return self.__salary * 0.1
        else:
            return self.__salary * 0.05


# using the class
emp1 = Employee(emp_id=101, name="Saha", salary=50000)

# safely access private data through getter
print(emp1.get_employee_info())

# safely update salary through setter
emp1.set_salary(55000)
print(emp1.get_employee_info())

# calculate bonus based on performance
bonus = emp1.calculate_bonus("excellent")
print(f"Bonus for excellent performance: {bonus}")'''

class Mobile:
    def __init__(self, number , balance):
        self.__number = number
        self.__balance = balance

    def get_mobile_info(self):
        return f"Number: {self.__number}, balance: {self.balance}"

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        if new_balance > 0:
            self.__balance = new_balance
            print(f"balance updated to {new_balance}")
        else:
            print("invalid balance amount")
    def recharge(self, amount):









