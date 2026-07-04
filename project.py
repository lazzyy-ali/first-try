class Employee:
    salary = 3000  # Class Variable

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return self.first_name + " " + self.last_name


# ساخت شیء
emp1 = Employee("Ali", "Pakdaman")

# نمایش نام و نام خانوادگی
print("Name:", emp1.full_name())

# نمایش حقوق
print("Salary:", Employee.salary)