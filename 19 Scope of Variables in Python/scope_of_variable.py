# Global Variable
company_name = "TechCorp"

class Employee:
    def __init__(self, name, age):
        # Instance Variables
        self.name = name
        self.age = age

    def show_details(self):
        # Local Variable
        message = "Employee details below:"
        print(message)  # Local variable
        print("Name:", self.name)
        print("Age:", self.age)
        print("Company:", company_name)  # Global variable used here
emp1 = Employee("Ameen", 25)
emp1.show_details()
