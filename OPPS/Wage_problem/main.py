# You are asked to create a class structure for employees in a company. The company has general employees and hourly employees.

class Employee:
    def __init__(self , emp_name , emp_id):
        self.emp_name = emp_name
        self.emp_id = emp_id

    def calculate_wage(self):
        return 0
    

class Hourly_Employee(Employee):
    def __init__(self, emp_name, emp_id , hour_of_work , hourly_rate):
        super().__init__(emp_name, emp_id)
        self.hour_of_work = hour_of_work
        self.hourly_rate = hourly_rate

    
    def calculate_wage(self):
        return self.hour_of_work * self.hourly_rate
    

class Normal_Employee(Employee):
    def __init__(self, emp_name, emp_id,monthly_salary):
        super().__init__(emp_name, emp_id)
        self.monthly_salary = monthly_salary

    def calculate_wage(self):
        return self.monthly_salary
    


hr_emp_obj = Hourly_Employee("Dogesh", 101, 40, 20)
nr_emp_obj = Normal_Employee("King", 102, 5000)

print(f"{hr_emp_obj.emp_name} and his salary is: {hr_emp_obj.calculate_wage()}")
print(f"{nr_emp_obj.emp_name} and his salary is: {nr_emp_obj.calculate_wage()}")
