class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def total_salary(self):
        hra = self.salary * 0.20
        da = self.salary * 0.10
        return self.salary + hra + da

emp = Employee("Rahul", 50000)

print("Employee:", emp.name)
print("Salary:", emp.total_salary())