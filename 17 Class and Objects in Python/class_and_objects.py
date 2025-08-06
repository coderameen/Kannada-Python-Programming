#Class: Class is a blueprint or a template.
#Object: Specific Instance created from the template
class Student:
    school = "Oxford High School"
    def show_student_details(self, name, grade):
        print(f"The name of student is: {name} and grade is {grade} and school is {self.school}")

  
# Create an object of Student
student1 = Student()

# Set student details
print(student1.school)
student1.show_student_details("Ameen", "10th")



#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
class Employee:
    company = "HP"

    def get_salary(self):
        print("Slary: 70,000")
    

emp1 = Employee()
print(emp1.company)
emp1.get_salary()


emp2 = Employee()
print(emp2.company)
emp2.get_salary()

#----------------------------------------------------


