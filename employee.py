class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        return f"Name: {self.name}, Salary: ${self.salary}"
