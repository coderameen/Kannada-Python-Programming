#CONDITIONAL STEMENTS allows you to execute code based on certian conditions
'''
if
if else
elif
match
'''

'''
syntax:
if condition:
    statement execution
'''
#Indentation and : for if statement
# age = int(input("Enter your name"))
age = 24
if age >= 18:
    print("He is Adult")
else:
    print("He is not adult!")

#greater of 3 number
a = 10
b = 40
c = 20

if a > b and a > c:
    print(a," is greater")
elif b > a and b > c:
    print(b," is greater")
else:
    print(c," is greater")

#NOTE: Match (newly introduced in 3.10+ version of python)
'''
Run Below code in python online compiler

grade = input("Enter the Grade: ").lower()

match grade:
    case 'c': print("Just Pass")
    case 'b': print("First Class")
    case 'a': print("Distinction!!")
    case _: print("Please enter the grade properly!!")

'''