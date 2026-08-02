
class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def introduce(self):
        print(f"My name is {self.name}.")
        print(f"I work in {self.department}.")

employee = Employee("Trung", "IT")
employee.introduce()
